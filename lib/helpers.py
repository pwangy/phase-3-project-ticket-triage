# lib/helpers.py
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task


def exit_program():
    print("Thanks for reviewing!")
    exit()

# def help():
#     print("Welcome to the Help section!")
#     print("Here are the available options:")
#     print("0: View your tasks")
#     print("1: Manage posts")
#     print("2: Manage reviewers")
#     print("3: Exit the program")
#     print("4: Display this help message")

#Reviewer
def list_reviewers():
    reviewers = Reviewer.get_all()
    for reviewer in reviewers:
        print(reviewer)
    
def find_reviewer_by_id():
    id_ = input("Enter the reviewer's id: ")
    reviewer = Reviewer.find_by_id(id_)
    print(reviewer) if reviewer else print(f'Reviewer {id_} not found')

def find_reviewer_by_name():
    name = input("Enter the reviewer's name: ")
    reviewer_by_name = [reviewer for reviewer in Reviewer.get_all() if reviewer.name.lower() == name.lower()]
    import ipdb; ipdb.set_trace()
    if reviewer_by_name:
        for reviewer in reviewer_by_name:
            print(reviewer)
    else:
        print(f'Reviewer {name} not found')

def create_reviewer():    
    user_is_not_created = True
    while(user_is_not_created):
        name = input("Enter the new reviewer's name: ")
        if len(name) < 2:
            print("Name must be at least 2 characters.")
        else:
            try:
                reviewer = Reviewer.create(name)
                print(f'Successfully Added: {reviewer}')
                user_is_not_created = False
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

