#!/usr/bin/env python3
# lib/debug.py

from classes.__init__ import CONN, CURSOR
import ipdb
from classes.post import Post
from classes.task import Task
from classes.reviewer import Reviewer

Task.drop_table()
Reviewer.drop_table()
Post.drop_table()

Reviewer.create_table()
Post.create_table()
Task.create_table()

r = Reviewer.create('Jasmine Patel')
arr = Reviewer('Bob Ross')
arr.save()
post1 = Post.create(5200000, 'Text')
post2 = Post.create(23400000, 'Video')
post3 = Post.create(6000, 'Picture')

print('herro!')
print(post1)
print(post2)
print(post3)

ipdb.set_trace()