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
    update_post_badge,
    sort_post_by_interactions,
    sort_post_by_newest,
    find_post_by_id,
    list_tasks,
    create_task,
    update_task_reviewer,
    task_by_reviewer_id,
    task_by_post_id,
    task_by_status,
    update_task_status
)

#! Main Menu
def main():
    while True:
        menu()
        choice = input("TICKET TRIAGE > MAIN > ")
        if choice == "0":
            my_tasks()
        if choice == "1":
            manage_all_tasks()
        elif choice == "2":
            manage_posts()
        elif choice == "3":
            manage_reviewers()
        elif choice == "8":
            exit_program()
        elif choice == "9":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Sub Menus
def my_tasks():
    m = "tasks"
    while m == "tasks":
        my_task_menu()
        choice = input("TICKET TRIAGE > MY TASKS > ")
        if choice == "0":
            update_task_status("in_progress")
        elif choice == "1":
            update_post_badge()
        elif choice == "2":
            update_task_status(3)
        # elif choice == "3":
            # list_tasks()
        elif choice == "3":
            main()
        elif choice == "8":
            exit_program()
        elif choice == "9":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def manage_all_tasks():
    m = "manage tasks"
    while m == "manage tasks":
        task_mgmt_menu()
        choice = input ("TICKET TRIAGE > MANAGE TASKS > ")
        if choice == "0":
            list_tasks()
        elif choice == "1":
            create_task()
        elif choice == "2":
            task_by_reviewer_id()
        elif choice == "3":
            task_by_post_id()
        elif choice == "4":
            task_by_status()
        elif choice == "5":
            update_task_reviewer()
        elif choice == "6":
            break
        elif choice == "8":
            exit_program()
        elif choice == "9":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def manage_posts():
    while True:
        post_mgmt_menu()
        choice = input ("TICKET TRIAGE >  MANAGE POSTS > ")
        if choice == "0":
            list_posts()
        elif choice == "1":
            sort_post_by_interactions()
        elif choice == "2":
            sort_post_by_newest()
        elif choice == "3":
            find_post_by_id()
        elif choice == "4":
            break
        elif choice == "8":
            exit_program()
        elif choice == "9":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def manage_reviewers():
    while True:
        reviewer_mgmt_menu()
        choice = input ("TICKET TRIAGE > MANAGE REVIEWERS > ")
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
        elif choice == "8":
            exit_program()
        elif choice == "9":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Help Menu
def help():
    while True:
        help_menu()
        choice = input ("TICKET TRIAGE > HELP > ")
        if choice == "0":
            my_tasks()
        if choice == "1":
            manage_all_tasks()
        if choice == "2":
            manage_posts()
        if choice == "3":
            manage_reviewers()
        if choice == "4":
            main()
        if choice == "8":
            exit_program()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

#! Print Menu Options
def menu():
    print("[bold magenta]WELCOME REVIEWER:rainbow:[/]")
    print("[bold cyan]Main Menu[/]")
    print("[bold green]0[/]: My Tasks")
    print("[bold green]1[/]: Manage All Tasks")
    print("[bold green]2[/]: Manage Posts")
    print("[bold green]3[/]: Manage Reviewers")
    print("[bold green]8[/]: Exit")
    print("[bold green]9[/]: Help")

def my_task_menu():
    print("[bold cyan]My Tasks[/]")
    print("[bold green]0[/]: Begin Task")
    print("[bold green]1[/]: Update Post Badge")
    print("[bold green]2[/]: Complete Task")
    # print("[bold green]3[/]: Task List") #!
    print("[bold green]3[/]: Back to Main Menu")
    print("[bold green]8[/]: Exit")
    print("[bold green]9[/]: Help")

def task_mgmt_menu():
    print("[bold cyan]Manage Tasks[/]")
    print("[bold green]0[/]: View All")
    print("[bold green]1[/]: Create Tasks")
    print("[bold green]2[/]: Find Task by Reviewer ID")
    print("[bold green]3[/]: Find Task by Post ID")
    print("[bold green]4[/]: Find Task by Status")
    print("[bold green]5[/]: Update Task Reviewer")
    print("[bold green]6[/]: Back to Main Menu")
    print("[bold green]8[/]: Exit")
    print("[bold green]9[/]: Help")

def post_mgmt_menu():
    print("[bold cyan]Manage Posts[/]")
    print("[bold green]0[/]: View All")
    print("[bold green]1[/]: Most Viral Post")
    print("[bold green]2[/]: Sort by Most Recent")
    print("[bold green]3[/]: Find Post by ID")
    print("[bold green]4[/]: Back to Main Menu")
    print("[bold green]8[/]: Exit")
    print("[bold green]9[/]: Help")

def reviewer_mgmt_menu():
    print("[bold cyan]Manage Reviewers[/]")
    print("[bold green]0[/]: List Reviewers")
    print("[bold green]1[/]: Find Reviewer by ID")
    print("[bold green]2[/]: Find Reviewer by Name")
    print("[bold green]3[/]: Update Reviewer")
    print("[bold green]4[/]: Add Reviewer")
    print("[bold green]5[/]: Delete Reviewer")
    print("[bold green]6[/]: Back to Main Menu")
    print("[bold green]8[/]: Exit")
    print("[bold green]9[/]: Help")
    
def help_menu():
    print("[bold magenta]Welcome to the Help section!:butterfly:[/]")
    print("[bold cyan]Available Options:[/]")
    print("[bold green]0[/]: View, Begin, Update, and Complete [bold green]Your Tasks[/]")
    print("[bold green]1[/]: View [bold green]All Tasks[/], Sort, Add, Reassign, and Find by Reviewer/Post")
    print("[bold green]2[/]: View [bold green]All Posts[/], Find by Reviewer ID, and Sort")
    print("[bold green]3[/]: View [bold green]All Reviewers[/], Find by Name or ID, Update, Add, and Delete")
    print("[bold green]4[/]: Back to [bold green]Main Menu[/]")
    print("[bold green]8[/]: Exit")

if __name__ == "__main__":
    random.seed(0)
    main()
