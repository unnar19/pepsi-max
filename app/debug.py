#this will pass in setUp

import json

from Logic.LogicAPI import LogicAPI

emp_delete = json.dumps({
"role": "boss",
"key": "employee",
"data": {
    "id": 1,
    }
})

new_emp1 = json.dumps({ "role": "boss",
                        "key": "employee",
                        "data": {
                            "role": "employee",
                            "name": "TestEmployee",
                            "password": "TestPassword",
                            "ssn": "0123456789",
                            "address": "Hvergistræti 69",
                            "home_phone": "5812345",
                            "mobile_phone": "8885555",
                            "email": "peee@ru.is",
                            "destination": "Reykjavík",
                            "tickets": "[]",
                            "reports": "[]",
                            }
                        })

new_emp2 = json.dumps({ "role": "boss",
                        "key": "employee",
                        "data": {
                            "role": "employee",
                            "name": "TestEmployee",
                            "password": "TestPassword",
                            "ssn": "0123456789",
                            "address": "Hvergistræti 69",
                            "home_phone": "5812345",
                            "mobile_phone": "8885555",
                            "email": "nnnnn@ru.is",
                            "destination": "Reykjavík",
                            "tickets": "[]",
                            "reports": "[]",
                            }
                        })


LL = LogicAPI()




getAll = json.dumps({"key":"employee","filter":"destination", "filter_value":"Reykjavík"})

res = LL.post(new_emp1)

