from Data.LogEmployee import LogEmployee
import json


emp = LogEmployee()

data = {"type":"dict",
        "data": {
            "role": "boss",
            "name":"einar",
            "password": "12345",
            "ssn":15555555,
            "address": "einarville",
            "home_phone": 3333,
            "mobile_phone": 333333,
            "email": "einskikingsi@kingshit.com",
            "location": "whoville",
            "tickets": "[]",
            "reports": "[]",
    }}


emp.create_new_employee(json.dumps(data))
