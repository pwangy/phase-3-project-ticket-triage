# Starting on the project - possible flow:
- [x] Pitch Prep (ERD/UML class/table diagram, timeline, core and stretch deliverables)
- [x] Start with the project template (provided in the following lesson). You are free to adapt the template structure, as long as you adhere to the project requirements.
- [ ] Class basic creation along with init, create_table(), drop_table(), create(), save().
- [ ] Work on seeding the db from inside your seed.py file using the class methods create() and the instance method save(). Feel free to seed the db with Faker, manually, or fetching/scraping data from the internet.
- [ ] Start equipping your classes with a few utility methods you know you will need (find_by(), find_or_create_by(), delete(), update(), etc)
- [ ] Start building the direct and through association methods (in case of a many-to-many) or only the direct association method (in case of a one-to-many). 
- [ ] Think about the user interaction. How will you prompt the user? What information will the user enter? How will you provide feedback to the user?
- [ ] Think about your data model. How will you organize and store the information received from the user?
- [ ] Start on the CLI class, what should be the flow for your for loop? What will be the main program options?
- [ ] Start forming CLI logic leveraging the other classes methods and VALIDATE EVERYTHING. Ensure that you are ACTUALLY USING the all the associations methods in your program.


## Advice to listen to closely
- [ ] You should always test your CLI by passing wrong values for ALL inputs and see what happens!
- [ ] The project revolves around many things but a MAJOR one are associations. Please make sure you actually build association methods AND USE THEM in the app. In a Doctor -> Appointment <- Patient example, given a doctor's name I allow the cli to list all the appointments AND all of the patients connected to the appointments.



## Links
[Pitch](https://docs.google.com/document/d/1Z9TDApNsv47NTMtcne-6JzDvuNjWAy22y7ab85noH0I/edit)

[Figma](https://www.figma.com/file/fhEHaljiHTu1Ggq4MauxM9/Ticket-Triage?type=whiteboard&node-id=1-143&t=B0Ju54tsqe1MpQus-0)

[Agreements](https://docs.google.com/document/d/1dPnwGhVtD0gjsfksEX_U1fX0R6dR-xWXKnOaCmjHyZU/edit#heading=h.e33dnqfb92rb)


[Project Requirements](https://learning.flatironschool.com/courses/7237/pages/phase-3-project-cli?module_item_id=655050)

[Grading Rubric](https://learning.flatironschool.com/courses/7237/assignments/271873?module_item_id=655054)



### from template

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```
---

## Credits


### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

