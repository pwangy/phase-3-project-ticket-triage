
from classes.__init__ import CURSOR, CONN
from classes.post import Post
from classes.status import Status
from classes.reviewer import Reviewer

print(Task.all)

def Task_Tests():
t1 = Task(1, "12-14-15", "1-2-55", 1, 3)
print(t1)

T = Task.create(
        self.status = 2,
        self.created_at = "2-5-55", 
        self.updated_at = "3-6-23",
        self.post_id = 1,
        self.reviewer_id = 9)
print("T")

Task.__repr__(T):(
        f"{self.id}"
        + f"Status {self.status},"
        + f"Created {self.created_at},"
        + f"Last Updated {self.updated_at},"
        + f"Post: {self.post_id},"
        + f"Assigned Reviewer: {self.reviewer_id}>"
        ) 

if T.status == 1 | 2 | 3 print (T.status):
    else: 
    raise ValueError("Status must be 1, 2, or 3")



T.status = 2
T.Updated_at = "03/27/24"
Task.update(T):
    print f"{T.__repr__}"

Task.Delete(T)
"not_deleted" if T else "gonzo"