from dataclasses import dataclass
from typing import List, Literal


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    address: str
    birthday: str
    gender: Literal['Male', 'Female', 'Other']
    hobby: Literal['Sports', 'Reading', 'Music']
    subject: Literal['Maths', 'Accounting', 'Arts', 'Social Studies', 'English', 'Chemistry', 'Physics',
    'Computer Science', 'Economics', 'History', 'Civics', 'Commerce', 'Biology', 'Hindi']
    picture: str
    state: Literal['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city: Literal['Karnal', 'Panipat', 'Delhi', 'Gurgaon', 'Noida', 'Agra', 'Merrut', 'Lucknow', 'Jaipur', 'Jaiselmer']


