# lib/helpers.py
from rich import print
from rich.table import Table
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task
    # import ipdb; ipdb.set_trace()


def exit_program():
    print("Thanks for reviewing!")
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
        print("No reviewers found.")
    
def find_reviewer_by_id():
    id_ = input("Enter the reviewer's id: ")
    reviewer = Reviewer.find_by_id(id_)
    print(reviewer) if reviewer else print(f'Reviewer {id_} not found')

def find_reviewer_by_name():
    name = input("Enter the reviewer's name: ")
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

#! Post Helpers
def list_posts():
    posts = Post.get_all()
    if posts:
        for post in posts:
            print(post)
    else:
        print("No posts found.")

def find_post_by_id():
    id_ = input("Enter the post's id: ")
    post = Post.find_by_id(id_)
    print(post) if post else print(f'Post {id_} not found')

#! "Error updating post badge: 'ValueError' object has no attribute 'review_badge'"   
def update_post_badge():
    post_id = input("Enter the post's id: ")
    post = Post.find_by_id(post_id)
    if post:
        new_badge = input("Enter the new review badge: ")
        try:
            post.review_badge(new_badge)
            post.update()
            print(f"Post {post_id} review badge updated to {new_badge}.")
        except Exception as e:
            print(f"Error updating post badge: {e}")
    else:
        print(f"Post {post_id} not found.")

#! Task Helpers
#! STILL NEEDS TESTING ONCE SEED IS COMPLETE!
def list_tasks():
    tasks = Task.get_all()
    if tasks:
        for tasks in tasks:
            return tasks
    else:
        print("I am sorry, it looks like we have no tasks in our system")

def create_task():
    try:
        status = int(input("Enter task status (1 for assigned, 2 for in progress, 3 for closed): "))
        created_at = input("Enter creation date (YYYY-MM-DD): ")
        updated_at = input("Enter last update date (YYYY-MM-DD): ")
        post_id = int(input("Enter post id: "))
        reviewer_id = int(input("Enter reviewer id: "))
        
        task = Task.create(status, created_at, updated_at, post_id, reviewer_id)
        print(f"Task created: {task}")
    except Exception as e:
        print(f"Error creating task: {e}")

def update_task_reviewer():
    task_id = input("Enter the task's id: ")
    task = Task.find_by_id(task_id)
    if task:
        new_reviewer_id = input("Enter the new reviewer's id: ")
        try:
            task.reviewer_id = new_reviewer_id
            task.update()
            print(f"Task {task_id} reviewer updated to {new_reviewer_id}.")
        except Exception as e:
            print(f"Error updating task reviewer: {e}")
    else:
        print(f"Task {task_id} not found.")

def task_by_reviewer_id():
    reviewer_id = input("Enter the reviewer's id: ")
    tasks = Task.find_by("reviewer_id", reviewer_id)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print(f"No tasks found for reviewer {reviewer_id}.")

def task_by_post_id():
    post_id = input("Enter the post's id: ")
    tasks = Task.find_by("post_id", post_id)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print(f"No tasks found for post {post_id}.")

def sort_tasks():
    tasks = Task.get_all()
    if tasks:
        sorted_tasks = sorted(tasks, key=lambda x: x.created_at)
        for task in sorted_tasks:
            print(task)
    else:
        print("No tasks found.")

def task_by_status(TASK_STATUS, tasks):
    filtered_tasks = [task for task in tasks if task.TASK_STATUS == TASK_STATUS]
    if filtered_tasks:
        for task in filtered_tasks:
            print(task)
    else:
        print(f'No tasks found with status: {TASK_STATUS}')

def sort_task_by_date(tasks):
    return sorted(tasks, key=lambda x: x.created_at)

#! STILL NEEDS TESTING ONCE SEED IS COMPLETE!
def update_task_status(new_status):
    task_id = input("Please Enter a Task Id: ")
    task = Task.find_by_id(task_id)
    if task:
        task.TASK_STATUS = new_status
        try:
            task.update()
            print(f"Task {task_id} status updated to {new_status}.")
        except Exception as e:
            return e
    else:
        print(f"Task {task_id} not found.")

