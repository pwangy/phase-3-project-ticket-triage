# Ticket Triage
Ever wondered just *how difficult it actually is* for social media platforms to trigger a fact checking task once a post become viral? We did! 

And then we decided to build an app about it. 

Imagined as an internal tool, this program works by creating a task once user-created content reaches viral status. 

What defines virality? There's no single answer, so we chose 3.5 million interactions as our virality threshold.

If a post has 3.5m or more interactions, a task is created and our end-user (a Reviewer) can work on that task. Once reviewed, a Post will then receive a publically visable badge displaying that the Post's content has been "Verified", "Debunked", or (if factfullness couldn't be conclusively decided) a warning to "Proceed With Caution".

This is not an end-to-end program, but rather it is a proof of concept. 

It assumes a database of user created content (Posts) which also includes a total count of interactions and that once a truthfullness badge has been assigned that another program detect the upate and display the corresponding graphical badge to the public.



### TL;DR
---
Ticket Triage is a fact checking queue, triggered by a post becoming viral. An internal tool for platform owners to mitigate disinformation.



## Getting Up and Running
Fork and clone this repo, then run ```pipenv install``` and ```pipenv shell``` in your terminal.

other steps...



## MVP &nbsp;|&nbsp; Deliverables
### ORM Requirements
- [x] The application must include a database created and modified with Python ORM methods that you write.
- [x] at least 2 tables with a one-to-many relationship (I would love to see a many-to-many though 🤓) manual ORM to implement: create, delete, get all, and find by id at minimum
- [x] The data model must include at least 2 model classes.
- [x] The data model must include at least 1 one-to-many relationship.
- [x] For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- [x] Pipfile contains all needed dependencies and no unneeded dependencies.
- [x] Imports are used in files only where necessary.
- [x] Project folders, files, and modules should be organized and follow appropriate naming conventions.
- [ ] well-organized code (separate classes for separate responsibilities) respect OO principles (SST, SOC, SOLID)
- [ ] The project should include a README.md that describes the application.

### CLI Requirements
- [x] The CLI must display menus with which a user may interact.
- [ ] The CLI should use loops as needed to keep the user in the application until they choose to exit.
- [ ] The CLI should validate user input and object creations/deletions, providing informative errors to the user.
- [x] Make sure your CLI has the option to quit/exit the program at any point and it doesn’t break on its own otherwise

### Classes/ Modules
- [x] Posts - can have a Task
- [x] Tasks - each task will have a Post and a Reviewer
- [x] Reviewer - will have a list of Tasks (which points to the Post)

### ORM Association Methods
- [x] Once a post reaches viral status, a Task is created and has an associated Reviewer

### CLI: User(Reviewer) can:
- [ ] create an object
- [ ] delete an object 
- [ ] display all objects 
- [ ] view related objects 
- [ ] find an object by attribute
- [ ] reviewer should be able to log in and check their list of tasks
- [ ] update task status
- [ ] update review_badge in Post
- [ ] manage reviewers
- [ ] see all posts
- [ ] see all tasks

### Stretch / Roadmap
- [ ] After the post is reviewed and is found to be false, then figure out what action should be taken
- [ ] Possible warning to the account who posted
- [ ] Each reviewer can assign priority to tasks on their task list 
- [ ] Priority levels: low, medium, high, blocker (all hands on deck)



## Authors
- [Gabriella Richmond](https://github.com/gabriellarichmo)
- [Peggy Wang](https://github.com/pwangy)
- [Chris Kjolhede](https://github.com/CKjolhede)


## Tech
Ticket Triage is a Python CLI Application
- Python
- SQL
- CLI
- Rich
- Faker
