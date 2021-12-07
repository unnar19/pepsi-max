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



"""
put = json.dumps({"role": "boss","key":"employee","id":1, "data":{"id": "1", "email": "nnnn@ru.is"}})

res = LL.put(put)

print(json.loads(res))


create_ticket = json.dumps({"role": "boss","key":"ticket", "data":{"real_estate_id":"blabla",
                                                                    "description": "blabla",
                                                                    "employee_id": "1",
                                                                    "destination": "Kulusuk",
                                                                    "start_date" : "10/10/2021",
                                                                    "priority":"very",
                                                                    "open":"yes"
                                                                     }})

res = LL.post(create_ticket)
"""

req = json.dumps({"key": "tickets", "data":{ "filters":["period","employee_id"],
                                             "filter_data":{ "start_date":"10/10/2021",
                                                                "end_date":"11/10/2021",
                                                                "employee_id":"1"}}})

req = json.dumps({"key": "tickets", "data":{ "filters":["date","employee_id"],
                                             "filter_data":{ "start_date":"10/10/2021",
                                                                "employee_id":"1"}}})

res = LL.get_tickets_filtered(req)


print(res)