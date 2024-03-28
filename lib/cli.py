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
            exit_program()
        elif choice == "1":
            list_tasks_by_user()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_posts()
        elif choice == "4":
            list_reviewers()
        elif choice == "5":
            help()
        else:
            print("That option doesn't exist, please choose an option from the menu.")

def my_tasks():
    while True:
        sub_menu1()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            update_task_status()
        elif choice == "2":
            pass

def manage_tasks():
    while True:
        sub_menu2()
        pass

def manage_posts():
    while True:
        sub_menu3()
        pass

def manage_reviewers():
    while True:
        sub_menu4()
        pass

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
    print("Please select an option:")
    print("0. Exit program")
    print("1. My Tasks")
    print("2. Manage All Tasks")
    print("3. Manage All Posts")
    print("4. Manage Reviewers")
    print("5. Help")


def sub_menu1():
    print("Please select an option:")
    print("0. Exit program")
    print("1. Update Task Status")
    print("2. Manage All Tasks")
    print("3. Manage All Posts")
    print("4. Manage Reviewers")
    print("5. Help")

def sub_menu2():
    print("Please select an option:")
    print("0. Exit program")
    pass

def sub_menu3():
    print("Please select an option:")
    print("0. Exit program")
    pass

def sub_menu4():
    print("Please select an option:")
    print("0. Exit program")
    pass


if __name__ == "__main__":
    random.seed(0)
    main()
    my_tasks()
    # manage_tasks()
    # manage_posts()
    # manage_reviewers()
