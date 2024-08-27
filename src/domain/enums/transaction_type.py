from enum import Enum

class TransactionType(str, Enum):
    OPENING = "OPENING"
    CANCELLATION = "CANCELLATION"
