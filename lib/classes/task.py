from classes.__init__ import CURSOR, CONN
from classes.post import Post
#from classes.status import Status
from classes.reviewer import Reviewer
from datetime import datetime


STATUS_TYPES = {
    1 : 'In Process',
    2 : 'Failed Verification',
    3 : 'Verfied'}

now = datetime.now()
date = now.strftime("%m/%d/%Y")

class Task:
    all = {}

    def __init__(self, status, created_at, updated_at, post_id, reviewer_id, id=None):
        self.status = status
        self.created_at = date
        self.updated_at = date
        self.post_id = post_id
        self.reviewer_id = reviewer_id
        self.id = id

    def __repr__(self):
        return (
            f"<Task {self.id},"
            + f"Status {self.status},"
            + f"Created {self.created_at},"
            + f"Last Updated {self.updated_at},"
            + f"Post: {self.post_id},"
            + f"Assigned Reviewer: {self.reviewer_id}>"
        )

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if not isinstance(status, str):
            raise ValueError("Invalid status.")
        else:
            self._status = status

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        if not isinstance(created_at, str):
            raise ValueError("updated_at must be a DateTime string")
        else: self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at 

    @updated_at.setter
    def updated_at(self, updated_at):
        if not isinstance(updated_at, str):
            raise ValueError("updated_at must be a DateTime string")
        else:
            self._updated_at = updated_at

    @property
    def post_id(self):
        return self._post_id

    @post_id.setter
    def post_id(self, post_id):
            self._post_id = post_id

    def post(self):
        if not isinstance((Post.find_by_id(post_id)), Post):
            raise ValueError("post_id not found")
        else:
            self._post_id = post_id

    @property
    def reviewer_id(self):
        return self._reviewer_id

    @reviewer_id.setter
    def reviewer_id(self, reviewer_id):
        if not isinstance((Reviewer.find_by_id(reviewer_id)), Reviewer):
            raise ValueError("reviewer_id not found")
        else:
            self._reviewer_id = reviewer_id

    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    INSERT INTO tasks (status, created_at, updated_at, post_id, reviewer_id) VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        self.status,
                        self.created_at,
                        self.updated_at,
                        self.post_id,
                        self.reviewer_id,
                    )
                )
                CONN.commit()
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
            return self
        except Exception as e:
            return e

    @classmethod
    def create(cls, status, created_at, updated_at, post_id, reviewer_id):
        try:
            with CONN:
                new_task = cls(status, created_at, updated_at, post_id, reviewer_id)
                new_task.save()
            return new_task
        except Exception as e:
            return e

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    UPDATE tasks 
                    SET status = ?, 
                        created_at = ?,
                        updated_at = ?, 
                        post_id = ?, 
                        reviewer_id = ?
                    WHERE id = ?
                    """,
                    (
                        self.status,
                        self.created_at,
                        self.updated_at,
                        self.post_id,
                        self.reviewer_id,
                        self.id,
                    ),
                )
                return self
        except Exception as e:
            return e

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DELETE FROM tasks WHERE id = ?
                    """,
                    (self.id,),
                )
        except Exception as e:
            return e

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        status TEXT,
                        created_at TEXT,
                        updated_at TEXT,
                        post_id INTEGER,
                        reviewer_id INTEGER,
                        FOREIGN KEY (post_id) REFERENCES posts(id),
                        FOREIGN KEY (reviewer_id) REFERENCES reviewers(id)
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

#CLI and Association Methods
def update_task_status():
    id_ = input("Enter the Task Id Number: ")
    if task := Task.find_by_id(id_):
        try:         
            status = input("Enter 2 for Status = In Process, 3 for Failed Verification, or 4 for Verified")
            task.status = status
            print(f'Status Changed to: {status}')
        except Exception as e:
            print("Error updating statu: ",e)
    else:
        print(f'Task{id} not found')

    @classmethod #create new instantance of Post based on info in db
    def new_from_db(cls, row):
        try:
            post = cls(row[1], row[2], row[3], row[4], row[5], row[0])
            cls.all[task.id] = task
            return task
        except Exception as e:
            return e