# lib/helpers.py
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task

def welcome():
    print("Welcome Reviewer!")
    exit()

def exit_program():
    print("Goodbye!")
    exit()

def help():
    print("Help")

#Reviewer
def list_reviewers():
    reviewers = Reviewer.get_all()
    for reviewer in reviewers:
        return reviewer
    
def find_reviewer_by_id():
    id_ = ("Enter the reviewer's id: ")
    reviewer = Reviewer.find_by_id(id_)
    print(reviewer) if reviewer else print(f'Reviewer {id_} not found')

def create_reviewer():
    id = input("Enter the reviewer's id: ")
    name = input("Enter the reviewer's name: ")
    try:
        reviewer = Reviewer.create(id, name)
        print(f'Success: {reviewer}')
    except Exception as e:
        return e

def update_reviewers():
    id_ = input("Enter the reviewer's id: ")
    if reviewer := Reviewer.find_by_id(id_):
        try:
            name = input("Enter the reviewer's new name: ")
            reviewer.name = name
            reviewer.update()
            print(f'Success: {reviewer}')
        except Exception as e:
            return e
    else:
        print(f'Reviewer {id_} not found')

def delete_reviewer():
    id_ = input("Enter the reviewer's id: ")
    if reviewer := Reviewer.find_by_id(id_):
        reviewer.delete()
        print(f'Reviewer {id_} deleted')
    else:
        print(f'Reviewer {id_} not found')

#Post
def list_posts():
    posts = Post.get_all()
    for post in posts:
        return post

def find_post_by_id():
    id_ = input("Enter the post's id: ")
    post = Post.find_by_id(id_)
    print(post) if post else print(f'Post {id_} not found')
    
def update_post_badge():
    new_badge = Post.review_badge()
    if new_badge:
        new_badge.rev

#Task
#! There is no get all method. we need that.
def list_tasks():
    tasks = Task.get_all()
    if tasks:
        for tasks in tasks:
            return tasks
    else:
        print("I am sorry, it looks like we have no tasks in our system")

def list_tasks_by_user():
    pass

#by date (oldest to newest) ((sort))
#something that updates the task [1] assigned, [2] in progress, [3] closed, [4] unassigned
#sort by status, sort by date, create task, update task

def update_task():
    pass

def sort_task_by_status(tasks):
    return sorted(tasks, key=lambda x: x.status)

def sort_task_by_date(tasks):
    return sorted(tasks, key=lambda x: x.created_at)

def update_task_status(task_id, new_status):
    task = Task.find_by_id(task_id)
    if task:
        task.update_status(new_status)
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Task {task_id} not found.")
