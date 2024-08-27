from enum import Enum


class PreferNotification(str, Enum):
    EMAIL = "email"
    PHONE = "phone"