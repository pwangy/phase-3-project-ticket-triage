# lib/helpers.py
from rich import print
from rich.table import Table
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task

STATUS_TYPES = [
    1, # assigned
    2, # in_progress
    3, # closed
    4 # unassigned
]

def exit_program():
    print("[bold magenta]Thanks for reviewing![/]")
    exit()

#! Reviewer Helpers
def list_reviewers():
    reviewers = Reviewer.get_all()
    if reviewers:
        table = Table(title="Reviewers")
        table.add_column("ID", justify="right")
        table.add_column("Name")
        for reviewer in reviewers:
            table.add_row(str(reviewer.id), reviewer.name)
        print(table)
    else:
        print("No reviewers found")

def find_reviewer_by_id():
    id_ = input("Enter the reviewer's ID: ")
    reviewer = Reviewer.find_by_id(id_)
    print(reviewer) if reviewer else print(f'Reviewer {id_} not found')

def find_reviewer_by_name():
    name = input("Enter the reviewer's full name: ")
    reviewer_by_name = [reviewer for reviewer in Reviewer.get_all() if reviewer.name.lower() == name.lower()]
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
            print("Name must be at least 2 characters")
        else:
            try:
                reviewer = Reviewer.create(name)
                print(f'Successfully Added: {reviewer}')
                user_is_not_created = False
            except Exception as e:
                return e

def update_reviewers():
    id_ = input("Enter the reviewer's ID: ")
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
    id_ = input("Enter the reviewer's ID: ")
    if reviewer := Reviewer.find_by_id(id_):
        reviewer.delete()
        print(f'Reviewer {id_} deleted')
    else:
        print(f'Reviewer {id_} not found')

#! Post Helpers
def list_posts():
    posts = Post.get_all()
    if posts:
        for post in posts:
            print(post)
    else:
        print("No posts found.")

def find_posts_by_reviewer(reviewer_id):
    tasks = Task.find_by("reviewer_id", reviewer_id)
    if tasks:
        post_ids = [task.post_id for task in tasks]
        posts = [Post.find_by_id(post_id) for post_id in post_ids if post_id is not None]
        if posts:
            for post in posts:
                print(post)
        else:
            print(f"No posts found for reviewer {reviewer_id}")
    else:
        print(f"No tasks found for reviewer {reviewer_id}")

def find_posts_by_post_id(post_id):
    tasks = Task.find_by("post_id", post_id)
    if tasks:
        post_ids = [task.post_id for task in tasks]
        posts = [Post.find_by_id(post_id) for post_id in post_ids if post_id is not None]
        if posts:
            for post in posts:
                print(post)
        else:
            print(f"No posts found for post {post_id}")
    else:
        print(f"No tasks found for post {post_id}")

def sort_post_by_interactions():
    posts = Post.get_all()
    if posts:
        sorted_posts = sorted(posts, key=lambda x: x.is_viral, reverse=True)
        for post in sorted_posts:
            print(post)
    else:
        print("No posts found")

def sort_post_by_newest():
    posts = Post.get_all()
    if posts:
        sorted_posts = sorted(posts, key=lambda x: x.created_at, reverse=True)
        for post in sorted_posts:
            print(post)
    else:
        print("No posts found")

def find_post_by_id():
    id_ = input("Enter the post's ID: ")
    try:
        id_int = int(id_)
    except ValueError:
        print("Please enter a valid integer ID.")
        return
    post = Post.find_by_id(id_int)
    if post:
        print(post)
    else:
        print(f'Post {id_int} not found')

def update_post_badge():
    post_id = input("Enter the post's ID: ")
    post = Post.find_by_id(post_id)
    if post:
        new_badge = input("Enter the new review badge (Verified, Debunked, Caution): ")
        try:
            if new_badge:
                post.review_badge = new_badge
                post.update()
                print(f"Post {post_id} review badge updated to {new_badge}")
            else:
                raise ValueError("Invalid review badge. Please enter one of: Verified, Debunked, Caution")
        except ValueError as e:
            print(f"Error updating post badge: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print(f"Post {post_id} not found")

#Task
def list_tasks():
    try:
        tasks = Task.get_all()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("Sorry, no tasks found in our system")
    except ValueError as e:
        print(f'Error occured while retrieving tasks: {e}')

def create_task():
    try:
        status = int(input("Enter task status (1 for assigned, 2 for in progress, 3 for closed, 4 for unassigned): "))
        post_id = int(input("Enter post ID: "))
        reviewer_id = int(input("Enter reviewer ID: "))

        task = Task.create(status-1, post_id, reviewer_id)
        print(f"Task created: {task}")
    except Exception as e:
        print(f"Error creating task: {e}")

def update_task_reviewer():
    task_id = input("Enter the task's ID: ")
    task = Task.find_by_id(task_id)
    if task:
        new_reviewer_id = input("Enter the new reviewer's ID: ")
        try:
            new_reviewer_id = int(new_reviewer_id)
            task.reviewer_id = new_reviewer_id
            task.update()
            print(f"Task {task_id} reviewer updated to {new_reviewer_id}")
        except Exception as e:
            print(f"Error updating task reviewer: {e}")
    else:
        print(f"Task {task_id} not found")

def task_by_reviewer_id():
    reviewer_id = input("Enter the reviewer's ID: ")
    tasks = Task.find_by("reviewer_id", reviewer_id)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print(f"No tasks found for reviewer {reviewer_id}")

def task_by_post_id():
    post_id = input("Enter the post's id: ")
    tasks = Task.find_by("post_id", post_id)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print(f"No tasks found for post {post_id}")

# def task_by_post_id():
#     post_id = input("Enter the post's ID: ")
#     tasks = Task.find_by("post_id", post_id)
#     if tasks:
#         for task in tasks:
#             print(task)
#     else:
#         print(f"No tasks found for post {post_id}.")

# def sort_tasks(sort_by_created_at=True):
#     tasks = Task.get_all()
#     if tasks:
#         if sort_by_created_at:
#             sorted_tasks = sorted(tasks, key=lambda x: x.created_at, reverse=False)
#         else:
#             sorted_tasks = sorted(tasks, key=lambda x: x.status)
#         for task in sorted_tasks:
#             print(task)
#     else:
#         print("No tasks found")

# def task_by_status(STATUS_TYPES, tasks):
#     filtered_tasks = [task for task in tasks if task.STATUS_TYPES == STATUS_TYPES]
#     if filtered_tasks:
#         for task in filtered_tasks:
#             print(task)
#     else:
#         print(f'No tasks found with status: {STATUS_TYPES}')

def task_by_status():
    status = int(input("Enter task status (1 for assigned, 2 for in progress, 3 for closed, 4 for unassigned): "))
    tasks = Task.get_all()
    filtered_tasks = [task for task in tasks if task.status == status]
    if filtered_tasks:
        for task in filtered_tasks:
            print(task)
    else:
        print(f'No tasks found with status: {status}')

def sort_task_by_date(tasks):
    return sorted(tasks, key=lambda x: x.created_at)

def update_task_status(new_status):
    task_id = input("Please Enter a Task ID: ")
    task = Task.find_by_id(task_id)
    if task:
        task.STATUS_TYPES = new_status
        try:
            task.update()
            print(f"Task {task_id} status updated to {new_status}")
        except Exception as e:
            return e
    else:
        print(f"Task {task_id} not found")

    # def update_task_status():
    #     id_ = input("Enter the Task ID Number: ")
    #     if task := Task.find_by_id(id_):
    #         try:         
    #             status = input("Enter 2 for Status = In Process, 3 for Failed Verification, or 4 for Verified")
    #             task.status = status
    #             print(f'Status Changed to: {status}')
    #         except Exception as e:
    #             print("Error updating statu: ",e)
    #     else:
    #         print(f'Task{id_} not found')
