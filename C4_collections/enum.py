from enum import Enum

class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


s=Status.APPROVED
print(s)
print(s.name,s.value)
print(Status.APPROVED=="approved")
print(s.APPROVEDD)
