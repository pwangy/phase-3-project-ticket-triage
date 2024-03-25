#!/user/bin/env python3

# from classes.__init__ import CONN, CURSOR
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task
from faker import Faker
fake = Faker()

def drop_tables():
    Task.drop_table()
    Post.drop_table()
    Reviewer.drop_table()
    
def create_tables():
    Reviewer.create_table()
    Post.create_table()
    Task.create_table()

def seed_tables():
    for _ in range(10):
        try:
            Reviewer.create(fake.name())
            Post.create()
            print("Created reviewer and post")
        except Exception as e:
            return e
    for _ in range(10):
        try:
            reviewers = Reviewer.get_all()
            posts = Post.get_all()
            Task.create(
                #enter the fake stuff
            )
            print("Created task")
        except Exception as e:
            return e

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")
    import ipdb; ipdb.set_trace()
