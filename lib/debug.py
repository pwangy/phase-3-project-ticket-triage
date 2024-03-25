#!/usr/bin/env python3
# lib/debug.py

from classes.__init__ import CONN, CURSOR
from classes.post import Post
# from classes.task import Task
from classes.reviewer import Reviewer
import ipdb

def reset_database():
  # Task.drop_table()
  Post.drop_table()
  Reviewer.drop_table()
  Reviewer.create_table()
  Post.create_table()
  # Task.create_table()

# Create seed data
reviewer_1 = Reviewer.create('Jasmine Patel')
reviewer_2 = Reviewer.create('Bob Ross')
reviewer_3 = Reviewer.create('Liam Thompson')
reviewer_4 = Reviewer.create('Ethan Chang')
reviewer_5 = Reviewer.create('Olivia Jensen')
reviewer_6 = Reviewer.create('Noah Martinez')
reviewer_7 = Reviewer.create('Ava Nguyen')
reviewer_8 = Reviewer.create('Lucas Rodriguez')
reviewer_9 = Reviewer.create('Isabella Khan')
reviewer_10 = Reviewer.create('Mason Kim')

post1 = Post.create(5200000, 'Text', 'Debunked')
post2 = Post.create(23400000, 'Video', 'Verified')
post3 = Post.create(6000, 'Picture', None)

print('herro!')

print(reviewer_1)
print(reviewer_2)
print(reviewer_3)
print(reviewer_4)
print(reviewer_5)
print(reviewer_6)
print(reviewer_7)
print(reviewer_8)
print(reviewer_9)
print(reviewer_10)

print(post1)
print(post2)
print(post3)

reset_database()
ipdb.set_trace()