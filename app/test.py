from Data.LogEmployee import LogEmployee
import json


emp = LogEmployee()

data = {"type":"dict",
        "data": {
            "id": 1,
            "role": "boss",
            "name":"Eyþór",
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


emp.overwrite(json.dumps(data))
