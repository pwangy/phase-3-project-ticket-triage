from classes.__init__ import CURSOR, CONN

class Reviewer:
    def __init__(self, name, id=None):
        self.name = name
        self.posts = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        elif len(name) <= 2:
            raise ValueError("Name must be at least two chars inclusive.")
        else:
            self._name = name

    @classmethod
    def create_table(cls):
        try:
            sql = """
                CREATE TABLE IF NOT EXISTS reviewers (
                id INTEGER PRIMARY KEY,
                name TEXT
                )
            """
            CURSOR.execute(sql)
            CONN.commit()
        except Exception as e:
            return e
        
    @classmethod
    def drop_table(cls):
        try:
            sql = """
                DROP TABLE IF EXISTS reviewers;
            """
            CURSOR.execute(sql)
            CONN.commit()
            self.id = CURSOR.lastrowid
            return self
        except Exception as e:
            CONN.rollback()
            return e
    

    def save(self):
        try:
            sql = """
                INSERT INTO reviewers (name)
                VALUES (?)
            """
            CURSOR.execute(sql, (self.name,))
            CONN.commit()
            self.id = CURSOR.lastrowid
            return self
        except Exception as e:
            CONN.rollback()
            return e

    @classmethod
    def create(cls, name):
        try:
            with CONN:
            reviewer = cls(name)
            rev = reviewer.save()
            return rev
        except Exception as e:
            return e

    def update(self):
        try:
            sql = """
                UPDATE reviewers
                SET name = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()
                type(self).all[self.id] = self
                return self
        except Exception as e:
            return e

    def delete(self):
        try:
            sql = """
                DELETE FROM reviewers
                WHERE id = ?
                    """,
                    (self.id,),
                )
                CONN.commit()
                del type(self).all[self.id]
                self.id = None
            return self
        except Exception as e:
            return e
        
    @classmethod
    def find_by_id(cls, id):
        try:
            CURSOR.execute(
                f"""
                SELECT * FROM reviewers
                WHERE id = ?;
            """,
            (id,)
            )
            row = CURSOR.fetchone()
            return cls(row[0]) if row else None
        except Exception as e:
            return e

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    SELECT * FROM reviewers;
                    """
                )
                rows = CURSOR.fetchall()
                return [cls(row[1], row[0]) for row in rows]
        except Exception as e:
            return e

    def save(self):
        try:
            with CONN:
                CURSOR.execute(
            """
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
            return self
        except Exception as e:
            return e
        
    # def tasks(self):
    #     from classes.task import Task
    
