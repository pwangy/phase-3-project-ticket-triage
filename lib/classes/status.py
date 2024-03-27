from enum import Enum 

class Status(Enum):
    assigned = 1
    in_progress = 2
    closed = 3
    unassigned = 4