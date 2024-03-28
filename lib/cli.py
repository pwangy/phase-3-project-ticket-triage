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
    list_tasks,
    create_task,
    update_task_reviewer,
    task_by_reviewer_id,
    task_by_post_id,
    sort_tasks,
    task_by_status,
    update_task_status
)

#! Main Menu
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            my_tasks()
        if choice == "1":
            manage_tasks()
        elif choice == "2":
            manage_posts()
        elif choice == "3":
            manage_reviewers()
        elif choice == "4":
            exit_program()
        elif choice == "5":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Sub Menus

def manage_tasks():
    m = "manage tasks"
    while m == "manage tasks":
        task_mgmt_menu()
        choice = input ("> ")
        if choice == "0":
            sort_tasks()
        elif choice == "1":
            task_by_reviewer_id()
        elif choice == "2":
            task_by_post_id()
        elif choice == "3":
            task_by_status()
        elif choice == "4":
            create_task()
        elif choice == "5":
            update_task_reviewer()
        elif choice == "6":
            break
        elif choice == "7":
            exit_program()
        elif choice == "8":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

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
            break
        elif choice == "6":
            exit_program()
        elif choice == "7":
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
            break
        elif choice == "7":
            exit_program()
        elif choice == "8":
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
            main()
        if choice == "4":
            exit_program()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Print Menu Options
def menu():
    print("[bold magenta]WELCOME REVIEWER:rainbow:[/bold magenta]")
    print("[bold cyan]Main Menu[/bold cyan]")
    print("[bold green]0[/bold green]: My Tasks")
    print("[bold green]1[/bold green]: Manage All Tasks")
    print("[bold green]2[/bold green]: Manage Posts")
    print("[bold green]3[/bold green]: Manage Reviewers")
    print("[bold green]4[/bold green]: Exit")
    print("[bold green]5[/bold green]: Help")

def my_task_menu():
    print("[bold cyan]My Tasks[/bold cyan]")
    print("0. Begin Task")
    print("1. Update Post Badge")
    print("2. Complete Task")
    print("3. Manage Reviewers")
    print("4. Back to Main Menu")
    print("5. Exit program")
    print("6. Help")

def task_mgmt_menu():
    print("[bold cyan]Manage Tasks[/bold cyan]")
    print("0. Sort Tasks")
    print("1. Find Task by Reviewer Id")
    print("2. Find Task by Post Id")
    print("3. Find Task by Status")
    print("4. Create Task")
    print("5. Update Task Reviewer")
    print("6. Back to Main Menu")
    print("7. Exit program")
    print("8. Help")

def post_mgmt_menu():
    print("[bold cyan]Manage Posts[/bold cyan]")
    print("0. Find Post by Task Id")
    print("1. Find Post with Most Interactions")
    print("2. Sort Post by Oldest to Newest")
    print("3. Find Post by Post Id")
    print("4. Find Post by Reviewer")
    print("5. Back to Main Menu")
    print("6. Exit program")
    print("7. Help")

def reviewer_mgmt_menu():
    print("[bold cyan]Manage Reviewers[/bold cyan]")
    print("[bold green]0[/bold green]: List Reviewers")
    print("[bold green]1[/bold green]: Find Reviewer by Id")
    print("[bold green]2[/bold green]: Find Reviewer by Name")
    print("[bold green]3[/bold green]: Update Reviewer")
    print("[bold green]4[/bold green]: Add Reviewer")
    print("[bold green]5[/bold green]: Delete Reviewer")
    print("[bold green]6[/bold green]: Back to Main Menu")
    print("[bold green]7[/bold green]: Exit Program")
    print("[bold green]8[/bold green]: Help")
    
def help_menu():
    print("[bold cyan]Welcome to the Help section![/bold cyan]")
    print("Here are the available options:")
    print("[bold green]0[/bold green]: View your tasks")
    print("[bold green]1[/bold green]: Manage posts")
    print("[bold green]2[/bold green]: Manage reviewers")
    print("[bold green]3[/bold green]: Back to Main Menu")
    print("[bold green]4[/bold green]: Exit program")

if __name__ == "__main__":
    random.seed(0)
    main()
