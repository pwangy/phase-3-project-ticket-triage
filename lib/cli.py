# lib/cli.py
import ipdb
import random
from rich import print

from helpers import (
    exit_program,
    list_reviewers,
    find_reviewer_by_id,
    find_reviewer_by_name,
    create_reviewer,
    update_reviewers,
    delete_reviewer,
    list_posts,
    find_post_by_id,
    list_tasks_by_user,
    list_tasks,
    update_task_status
)

#! Main Menu
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            my_tasks()
        elif choice == "1":
            manage_posts()
        elif choice == "2":
            manage_reviewers()
        elif choice == "3":
            exit_program()
        elif choice == "4":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Sub Menus
def my_tasks():
    m = "tasks"
    while m == "tasks":
        my_task_menu()
        choice = input("> ")
        if choice == "0":
            update_task_status("in_progress")
        elif choice == "1":
            update_post_badge()
        elif choice == "2":
            update_task_status("completed")
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            main()
        elif choice == "5":
            exit_program()
        elif choice == "6":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def manage_tasks(my_tasks):
    m = "manage tasks"
    while m == "manage tasks":
        task_mgmt_menu(my_tasks)
        choice = input ("> ")
        if choice == "0":
            sort_tasks()
        elif choice == "1":
            find_task_by_reviewer_id()
        elif choice == "2":
            find_task_by_post_id()
        elif choice == "3":
            find_task_by_status()
        elif choice == "4":
            create_task()
        elif choice == "5":
            update_task_reviewer()
        elif choice == "6":
            exit_program()
        elif choice == "7":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def manage_posts():
    while True:
        post_mgmt_menu()
        choice = input ("> ")
        if choice == "0":
            sort_by_task_id()
        elif choice == "1":
            sort_post_by_interactions()
        elif choice == "2":
            sort_post_by_oldest()
        elif choice == "3":
            find_post_by_id()
        elif choice == "4":
            find_post_by_reviewer()
        elif choice == "5":
            exit_program()
        elif choice == "6":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def manage_reviewers():
    while True:
        reviewer_mgmt_menu()
        choice = input ("> ")
        if choice == "0":
            list_reviewers()
        elif choice == "1":
            find_reviewer_by_id()
        elif choice == "2":
            find_reviewer_by_name()
        elif choice == "3":
            update_reviewers()
        elif choice == "4":
            create_reviewer()
        elif choice == "5":
            delete_reviewer()
        elif choice == "6":
            exit_program()
        elif choice == "7":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Help Menu
def help():
    while True:
        help_menu()
        choice = input ("> ")
        if choice == "0":
            my_tasks()
        if choice == "1":
            manage_posts()
        if choice == "2":
            manage_reviewers()
        if choice == "3":
            exit_program
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Print Menu Options
def menu():
    print("[bold cyan]WELCOME REVIEWER:rainbow:[/bold cyan]")
    print("[bold cyan]Main Menu[/bold cyan]")
    print("[bold green]0[/bold green]: Manage Tasks")
    print("[bold green]1[/bold green]: Manage Posts")
    print("[bold green]2[/bold green]: Manage Reviewers")
    print("[bold green]3[/bold green]: Exit")
    print("[bold green]4[/bold green]: Help")

def my_task_menu():
    print("Please select an option:")
    print("0. Begin Task")
    print("1. Update Post Badge")
    print("2. Complete Task")
    print("3. Manage Reviewers")
    print("4. Back to Main Menu")
    print("5. Exit program")
    print("6. Help")

def task_mgmt_menu():
    print("Please select an option:")
    print("0. Sort Tasks")
    print("1. Find Task by Reviewer Id")
    print("2. Find Task by Post Id")
    print("3. Find Task by Status")
    print("4. Create Task")
    print("5. Update Task Reviewer")
    print("6. Exit program")
    print("7. Help")


def post_mgmt_menu():
    print("Please select an option:")
    print("0. Find Post by Task Id")
    print("1. Find Post with Most Interactions")
    print("2. Sort Post by Oldest to Newest")
    print("3. Find Post by Post Id")
    print("4. Find Post by Reviewer")
    print("5. Exit program")
    print("6. Help")

def reviewer_mgmt_menu():
    print("Please select an option:")
    print("0. List Reviewers")
    print("1. Find Reviewer by Id")
    print("2. Find Reviewer by Name")
    print("3. Update Reviewer")
    print("4. Add Reviewer")
    print("5. Delete Reviewer")
    print("6. Exit Program")
    print("7. Help")
    
def help_menu():
    print("[bold cyan]Welcome to the Help section![/bold cyan]")
    print("Here are the available options:")
    print("0: View your tasks")
    print("1: Manage posts")
    print("2: Manage reviewers")
    print("3: Exit the program")
    print("4: Display this help message")

if __name__ == "__main__":
    random.seed(0)
    main()
