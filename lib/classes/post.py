#lib/post.py
from __init__ import CURSOR, CONN
from datetime import datetime

CONTENT_TYPES = [
    'Picture',
    'Video',
    'Text',
]

class Post:
    all = {} # dict of all posts in db
    
    def __init__(self, total_interactions, content_type, datetime, id=None):
        self.total_interactions = total_interactions
        self.content_type = content_type
        self.created = datetime
        self.id = id
        # self.title = post title, is this needed? or fake link?
        # self.author = author
        # status badges factual, false, use with caution

    def __repr__(self):
        return (
            f'<Post {self.id}: {self.created}, {self.total_interactions}, {self.content_type}>'
        )

    @property
    def total_interactions(self):
        return self._total_interactions

    @total_interactions.setter
    def total_interactions(self, total_interactions):
        if not isinstance(total_interactions, int):
            raise ValueError(f'Total Interactions must be an integer.')
        else:
            self._total_interactions = total_interactions

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        if not content_type in CONTENT_TYPES:
            raise ValueError(f'Content Type must be in list of CONTENT_TYPES.')
        else:
            self._content_type = content_type

    @property
    def created(self):
        return self._created
    
    @created.setter
    def created(self, created): #! this needs fixing!
        # timestamp = datetime.datetime.now()
        if not isinstance(created, str):
            raise TypeError(f'Date Created must be a string.')
        else:
            self._created = created

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
                        created TEXT
                    );
                    """
                )
        except Exception as e:
            print(f'Error creating table:', e)

    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CURSOR.execut(
                    """
                    DROP TABLE IF EXISTS posts;
                    """
                )
        except Exception as e:
            print(f'Error dropping table:', e)

    @classmethod
    def create(cls, total_interactions, content_type, created):
        try:
            with CONN:
                new_post = cls(total_interactions, content_type, created)
                new_post.save()
                return new_post
        except Exception as e:
            print(f'Error creating doctor:', e)

    @classmethod
    def new_from_db(cls, row):
        try:
            post = cls(row[1], row[2], row[3], row[0])
            cls.all[post.id] = post
            return post
        except Exception as e:
            print(f'Error creating post from database:', e)

    @classmethod
    def get_all(cls):
        try:
            CURSOR.exceute(
                """
                SELECT * FROM posts;
                """
            )
            rows = CURSOR.fetchall()
            return [cls(row[1], row[2], row[3], row[0]) for row in rows]
        except Exception as e:
            print(f'Error getting posts:', e)

    @classmethod
    def find_by_id(cls, id):
        try:
            CURSOR.execute(
                """
                SELECT * FROM posts
                WHERE id is ?;
                """
                (id,),
            )
            row = CURSOR.fetchone()
            return cls(row[1], row[2], row[3], row[0]) if row else None
        except Exception as e:
            print(f'Error finding or creating post:', e)

    #method to check for virality