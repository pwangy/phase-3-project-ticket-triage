# lib/cli.py
import ipdb
import random

from helpers import (
    welcome,
    exit_program,
    help,
    list_reviewers,
    find_reviewer_by_id,
    create_reviewer,
    update_reviewers,
    delete_reviewer,
    list_posts,
    find_post_by_id,
    list_tasks_by_user,
    list_tasks,
    update_task_status
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            list_tasks_by_user()
        elif choice == "1":
            list_tasks()
        elif choice == "2":
            list_posts()
        elif choice == "3":
            list_reviewers()
        elif choice == "4":
            exit_program()
        elif choice == "5":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def my_tasks():
    m = "tasks"
    while m == "tasks":
        sub_menu1()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            update_task_status()
        elif choice == "2":
            pass
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def manage_tasks(my_tasks):
    m = "manage tasks"
    while m == "manage tasks":
        sub_menu2(my_tasks)
        choice = input ("> ")
        if choice == "0":
            sort_tasks()
        elif choice == "1":
            find_task_by_reviewer()
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
        sub_menu3()
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
        sub_menu4()
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

# def mainmenu ():
#     d = ''
#     msg = ''    # Added in Update #1
#     while d == '':
#         print ('\nWELCOME REVIEWER!')
#         print ('1. Settings')
#         print ('q. Quit')
#         option = input ('Select an option: ')
#         if option.lower () == 'q':
#             sys.exit ()
#         elif option == '1':
#             msg = 'Option 1'    # Added in Update #1
#             d = submenu ()
#         else:
#             print ('Invalid selection!')
#     return msg, d 


def menu():
    print("Welcome Reviewer!")
    print("Please select an option:")
    print("0. My Tasks")
    print("1. Manage All Tasks")
    print("2. Manage All Posts")
    print("3. Manage Reviewers")
    print("4. Exit program")
    print("5. Help")


def sub_menu1():
    print("Please select an option:")
    print("0. Update Task Status")
    print("1. Manage All Tasks")
    print("2. Manage All Posts")
    print("3. Manage Reviewers")
    print("4. Exit program")
    print("5. Help")

def sub_menu2():
    print("Please select an option:")
    print("0. Sort Tasks")
    print("1. Find Task by Reviewer")
    print("2. Find Task by Post Id")
    print("3. Find Task by Status")
    print("4. Create Task")
    print("5. Update Task Reviewer")
    print("6. Exit program")
    print("7. Help")


def sub_menu3():
    print("Please select an option:")
    print("0. Find Post by Task Id")
    print("1. Find Post with Most Interactions")
    print("2. Sort Post by Oldest to Newest")
    print("3. Find Post by Post Id")
    print("4. Find Post by Reviewer")
    print("5. Exit program")
    print("6. Help")

def sub_menu4():
    print("Please select an option:")
    print("0. List Reviewers")
    print("1. Find Reviewer by Id")
    print("2. Find Reviewer by Name")
    print("3. Update Reviewer")
    print("4. Add Reviewer")
    print("5. Delete Reviewer")
    print("6. Exit Program")
    print("7. Help")
    


if __name__ == "__main__":
    random.seed(0)
    main()
    my_tasks()
    manage_tasks()
    manage_posts()
    manage_reviewers()
