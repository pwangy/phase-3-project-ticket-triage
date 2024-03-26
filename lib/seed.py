#!/usr/bin/env python3

from faker import Faker
import random
from classes.post import Post
from classes.reviewer import Reviewer
from classes.task import Task


fake = Faker()
#CONN = sqlite3.connect("ticket_triage.db")
#CURSOR = CONN.cursor()

##def drop_tables():
##    # Drop existing tables
##    Task.drop_table()
##    Reviewer.drop_table()
##    Post.drop_table()

#def create_tables():
#    Post.create_table()
#    Reviewer.create_table()
    #Task.create_table()

def seed_tables(): 
    for _ in range(10):
        try:
            Reviewer.create(fake.name())
        except Exception as e:
            return e

    for _ in range(10):
        try:
            Post.create(fake.number())
        except Exception as e:
            return e

    
    CURSOR.execute('''CREATE TABLE IF NOT EXISTS tasks (status TEXT, created_at TEXT, updated_at TEXT, post_id INTEGER, reviewer_id INTEGER)''')
    for _ in range(200):
        CURSOR.execute('INSERT INTO tasks VALUES (?, ?, ?, ?, ?)', (
            random.choice(['Unseen', 'In_Review', 'Completed']),
            fake.date(),
            fake.date(),
            random.randint(1, 1000000),
            random.randint(1, 20)
        ))

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")
    import ipdb; ipdb.set_trace()
