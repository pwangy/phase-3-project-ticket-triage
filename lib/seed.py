#!/user/bin/env python3
from faker import Faker
from classes.post import Post
from classes.reviewer import Reviewer
from classes.task import Task

fake = Faker()

CONTENT_TYPES = [
    'Picture',
    'Video',
    'Text'
]

STATUS_TYPES = [
    1, # assigned
    2, # in_progress
    3, # closed
    4 # unassigned
]

def drop_tables():
    Task.drop_table()
    Reviewer.drop_table()
    Post.drop_table()
    
def create_tables():
    Post.create_table()
    Reviewer.create_table()
    Task.create_table()

def seed_tables():
    for _ in range(10):
        try:
            Reviewer.create(fake.name())
            print('Created reviewer')
        except Exception as e:
            print("Failed to create Reviewer: ", e)

    for _ in range(10): #create non-viral posts
        try:
            number = fake.random_int(min=1, max=3499999)
            Post.create(number, fake.random_element(elements=CONTENT_TYPES), review_badge=None)
            print('Created post')
        except Exception as e:
            print("Failed to create Post: ", e)

    for _ in range(250): #create viral posts
        try:
            number = fake.random_int(min=3500000, max=200000000)
            Post.create(number, fake.random_element(elements=CONTENT_TYPES), review_badge=None)
            print('Created post')
        except Exception as e:
            print("Failed to create Post: ", e)

def seed_tasks():
    posts = Post.get_all()
    for post in posts:
        try:
            post.task()
            print('Created task for post: ', post.id)
        except Exception as e:
            print("Failed to create Task: ", e)

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed reviewers and posts!")
    seed_tasks()
    print("Finished seeding Tasks! ticket_triage.db has been seeded!")
    import ipdb; ipdb.set_trace()
