#!/usr/bin/env python3
# lib/debug.py

# from classes.__init__ import CONN, CURSOR
from classes.post import Post
# from classes.task import Task
from classes.reviewer import Reviewer
# from faker import Faker
# fake = Faker()

def reset_database():
  # Task.drop_table()
  Post.drop_table()
  Reviewer.drop_table()
  
  Reviewer.create_table()
  Post.create_table()
  # Task.create_table()

# Create seed data
  reviewer1 = Reviewer.create('Jasmine Patel')
  reviewer2 = Reviewer.create('Bob Ross')
  reviewer3 = Reviewer.create('Liam Thompson')
  reviewer4 = Reviewer.create('Ethan Chang')
  reviewer5 = Reviewer.create('Olivia Jensen')
  reviewer6 = Reviewer.create('Noah Martinez')
  reviewer7 = Reviewer.create('Ava Nguyen')
  reviewer8 = Reviewer.create('Lucas Rodriguez')
  reviewer9 = Reviewer.create('Isabella Khan')
  reviewer10 = Reviewer.create('Mason Kim')

  post1 = Post.create(5200000, 'Text', 'Debunked')
  post2 = Post.create(23400000, 'Video', 'Verified')
  post3 = Post.create(6000, 'Picture', None)

  # Task.create(reviewer1.id, post1.id)

  print('herro!')
  print(reviewer1)

if __name__ == '__main__':
  reset_database()
  print('Seed database')
  import ipdb; ipdb.set_trace()