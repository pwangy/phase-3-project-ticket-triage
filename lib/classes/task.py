#!/usr/bin/env python3
#lib/classes.task.py
from classes.__init__ import CURSOR, CONN
from datetime import datetime

STATUS_TYPES = [
    1, # assigned
    2, # in_progress
    3, # closed
    4 # unassigned
]

class Task:
    all = {}

    def __init__(self, post_id, status=4, id=None):
        self.post_id = post_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviewer_id = None
        self.status = status
        self.id = id

    def __repr__(self):
        return (
            f"<Task {self.id}, Status: {self.status}, Created: {self.created_at}, Updated: {self.updated_at}, Post: {self.post_id}, Reviewer: {self.reviewer_id}>"
        )

    #! Attributes and Props
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
    def updated_at(self):
        return self._updated_at 

    @updated_at.setter
    def updated_at(self, value):
        if not isinstance(value, datetime):
            raise TypeError("'created_at' must be a valid datetime object.")
        else:
            self._updated_at = value

    def status(self, new_status):
        if not new_status in STATUS_TYPES:
            raise ValueError("'status' must be in list of STATUS_TYPES")
        else:
            self.status = new_status

#! Association Methods
    def post_id(self):
        from classes.post import Post
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM post
                    WHERE post_id = ?
                    """,
                    (self.id,),
                )
                rows = CURSOR.fetchall()
                return [Post(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
        except Exception as e:
            return e

    def reviewer_id(self):
        from classes.reviewer import Reviewer
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM reviewer
                    WHERE reviewer_id = ?
                    """,
                    (self.id,),
                )
                rows = CURSOR.fetchall()
                return [Reviewer(row[1], row[0]) for row in rows]
        except Exception as e:
            return e

    #! ORM Class Methods
    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        post_id INTEGER,
                        created_at TEXT,
                        updated_at TEXT,
                        reviewer_id INTEGER,
                        status INTEGER
                    );
                    """
                )
        except Exception as e:
            return e

    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CURSOR.execute("DROP TABLE IF EXISTS tasks")
        except Exception as e:
            return e

    @classmethod
    def create(cls, post_id, reviewer_id, status):
        try:
            with CONN:
                new_task = cls(post_id, reviewer_id, status)
                new_task.save()
            return new_task
        except Exception as e:
            return (f"{e} Task was not created")

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM tasks;
                    """
                )
                rows = CURSOR.fetchall()
                return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM tasks
                    WHERE id = ?;
                    """,
                    (id,)
                )
                row = CURSOR.fetchone()
            return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None
        except Exception as e:
            return e

    @classmethod
    def find_by(cls, attr, val):
        try:
            CURSOR.execute(
                f"""
                SELECT * FROM tasks
                WHERE {attr} = ?;
                """,
                (val,)
            )
            row = CURSOR.fetchone()
            return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None
        except Exception as e:
            return e

    #! ORM Instance Methods
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    INSERT INTO tasks (post_id, created_at, updated_at, reviewer_id, status)
                    VALUES (?, ?, ?, ?, ?);
                    """,
                    (
                        self.post_id,
                        self.created_at,
                        self.updated_at,
                        self.reviewer_id,
                        self.status
                    )
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
                    UPDATE tasks 
                    SET status = ?, created_at = ?, updated_at = ?, post_id = ?, reviewer_id = ?
                    WHERE id = ?
                    """,
                    (self.post_id, self.created_at, self.updated_at, self.reviewer_id, self.status,self.id,)
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
                    DELETE FROM tasks
                    WHERE id = ?
                    """,
                    (self.id,),
                )
                CONN.commit() #rm memoized obj
                del type(self).all[self.id]
                self.id = None #nullify id
            return self
        except Exception as e:
            return e

    #! should this live in helpers?
    # def update_task_status():
    #     id_ = input("Enter the Task Id Number: ")
    #     if task := Task.find_by_id(id_):
    #         try:         
    #             status = input("Enter 2 for Status = In Process, 3 for Failed Verification, or 4 for Verified")
    #             task.status = status
    #             print(f'Status Changed to: {status}')
    #         except Exception as e:
    #             print("Error updating statu: ",e)
    #     else:
    #         print(f'Task{id_} not found')
