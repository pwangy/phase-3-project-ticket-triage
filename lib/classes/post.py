#!/usr/bin/env python3
#lib/classes.post.py
from classes.__init__ import CURSOR, CONN
from datetime import datetime

CONTENT_TYPES = [
    'Picture',
    'Video',
    'Text'
]

FACT_CHECKED = [
    'Verified',
    'Debunked',
    'Caution'
]

class Post:
    all = {} # dict of all posts in db

    def __init__(self, total_interactions, content_type, id=None):
        self.total_interactions = total_interactions
        self.content_type = content_type
        self.created_at = datetime.now()
        self._review_badge = None
        self._is_viral = self.calculate_virality(total_interactions)
        self.task = None
        self.id = id

    def __repr__(self):
        return (
            f"""<Post {self.id}: Creation Date: {self.created_at}, Interactions: {self.total_interactions}, Content Type: {self.content_type}, Viral: {self.is_viral}, Review Badge: {self.review_badge}>"""
        )

    @staticmethod # belongs to class, not its instances. can be called without creating an instance
    def calculate_virality(total_interactions):
        return total_interactions >= 3500000

    #! Attributes and Props
    @property
    def total_interactions(self):
        return self._total_interactions

    @total_interactions.setter
    def total_interactions(self, total_interactions):
        if not isinstance(total_interactions, int):
            raise ValueError("total_interactions must be an integer.")
        else:
            self._total_interactions = total_interactions

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        if not content_type in CONTENT_TYPES:
            raise ValueError("content_type must be in list of CONTENT_TYPES.")
        else:
            self._content_type = content_type

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError("'created_at' must be a valid datetime object.")
        else:
            self._created_at = value

    @property
    def review_badge(self):
        return self._review_badge

    @review_badge.setter
    def review_badge(self, new_review_badge):
        if not new_review_badge in FACT_CHECKED:
            raise ValueError("review_badge must be in list FACT_CHECKED.")
        else:
            self._review_badge = new_review_badge

    @property
    def is_viral(self):
        return self._is_viral

    @is_viral.setter
    def is_viral(self, value):
        self._is_viral = value

#! Association Methods
    def task(self):
        from classes.task import Task
        if not self.is_viral:
            raise AttributeError("A post must be viral in order to create a task.")
        Task.create(self.id, status=4)

    #! ORM Class Methods
    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY,
                        total_interactions INTEGER,
                        content_type TEXT,
                        created_at TEXT,
                        review_badge TEXT,
                        task INTEGER,
                        is_viral TEXT
                    );
                    """
                )
        except Exception as e:
            return("Error creating table: ", e)

    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DROP TABLE IF EXISTS posts;
                    """
                )
        except Exception as e:
            return("Sorry! Could not drop table: ", e)

    @classmethod
    def create(cls, total_interactions, content_type, review_badge):
        try:
            with CONN:
                post = cls(total_interactions, content_type, review_badge)
            return post.save()
        except Exception as e:
            return("Could not create new post: ", e)

    @classmethod #create new instantance of Post based on info in db
    def new_from_db(cls, row):
        try:
            post = cls(
                total_interactions=row[1],
                content_type=row[2],
                review_badge=row[4],
                id=row[0]
            )
            cls.all[post.id] = post
            return post
        except Exception as e:
            return e

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM posts;
                    """
                )
                rows = CURSOR.fetchall()
                posts = []
                for row in rows:
                    try:
                        post = cls(row[1], row[2], row[0])
                        posts.append(post)
                    except Exception as e:
                        print("Error creating Post instance from database row:", e)
                return posts
        except Exception as e:
            return("Sorry! Could not fetch all posts: ", e)

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM posts
                    WHERE id = ?;
                    """,
                    (id,)
                )
                row = CURSOR.fetchone()
            return cls._create_post_from_row(row) if row else None
        except Exception as e:
            return e

    @classmethod
    def find_by(cls, attr, val):
        try:
            CURSOR.execute(
                f"""
                SELECT * FROM posts
                WHERE {attr} = ?;
                """,
                (val,)
            )
            row = CURSOR.fetchone()
            return cls._create_post_from_row(row) if row else None
        except Exception as e:
            return e

    @classmethod # datetime helper. Parses datetime str
    def _create_post_from_row(cls, row):
        if row:
            # created_at = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            return cls(row[1], row[2], row[0], created_at, row[4], row[5])
        return None

    #! ORM Instance Methods
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    INSERT INTO posts (total_interactions, content_type, created_at, review_badge, is_viral)
                    VALUES (?, ?, ?, ?, ?);
                    """,
                    (self.total_interactions, self.content_type, self.created_at, self.review_badge, self.is_viral)
                )
                CONN.commit()
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
            return self
        except Exception as e:
            return e

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    UPDATE posts 
                    SET total_interactions = ?, content_type = ?, review_badge = ?, is_viral = ?
                    WHERE id = ?
                    """,
                    (self.total_interactions, self.content_type, self.review_badge, self.is_viral, self.id)
                )
                CONN.commit()
                type(self).all[self.id] = self
                return self
        except Exception as e:
            return e

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DELETE FROM posts
                    WHERE id = ?
                    """,
                    (self.id,)
                )
                CONN.commit() #rm memoized obj
                del type(self).all[self.id]
                self.id = None #nullify id
            return self
        except Exception as e:
            return e
