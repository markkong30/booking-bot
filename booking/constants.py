import os
from dotenv import load_dotenv
from enum import Enum

load_dotenv()

login_email = os.environ["TOYOKO_EMAIL"]
login_password = os.environ["TOYOKO_PASSWORD"]
mobile_number = os.environ["MOBILE_NUMBER"]
booking_time = os.environ["BOOKING_TIME"]


class Smoking_type(Enum):
    NON_SMOKING = "0"
    SMOKING = "1"


class No_of_people(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"


class Room_type(Enum):
    SINGLE = "10"
    DOUBLE = "20"
    TWIN = "30"


class Room_type_text(Enum):
    SINGLE = "禁煙　シングル"
    DOUBLE = "禁煙　ダブル"
    TWIN = "禁煙　ツイン"


class Gender(Enum):
    MALE = "1"
    FEMALE = "2"
