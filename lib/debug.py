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
print('herro!')
Reviewer.create('Liam Thompson')
Reviewer.create('Ethan Chang')
Reviewer.create('Olivia Jensen')
Reviewer.create('Noah Martinez')
Reviewer.create('Ava Nguyen')
Reviewer.create('Lucas Rodriguez')
Reviewer.create('Isabella Khan')
Reviewer.create('Mason Kim')
ipdb.set_trace()