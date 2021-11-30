from Data.Log_employee import Log_employee
import json

employeeshit = Log_employee()
data = {"type":"dict",
        "data": {
            "id": 1,
            "name":"einar",
            "username": "einsi",
            "password": "12345",
            "ssn":15555555,
            "address": "einarville",
            "home_phone": 3333,
            "mobile_phone": 333333,
            "email": "Einar@kingsi.is",
            "location": "whoville"
    }}
testshit = json.dumps(data, indent = 4)
employeeshit.create_new_employee(testshit)