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

empty_emp = json.dumps({ "role": "boss",
                        "key": "employee",
                        "data": {
                            "role": "",
                            "name": "",
                            "password": "",
                            "ssn": "",
                            "address": "",
                            "home_phone": "",
                            "mobile_phone": "",
                            "email": "",
                            "destination": "",
                            "tickets": "",
                            "reports": "",
                            }
                        })

#LL.post(empty_emp)

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

req = json.dumps({"key": "tickets", "data":{ "filters":["period","employee_id"],
                                             "filter_data":{ "start_date":"10/10/2021",
                                                                "end_date":"11/10/2021",
                                                                "employee_id":"1"}}})

req = json.dumps({"key": "tickets", "data":{ "filters":["date","employee_id"],
                                             "filter_data":{ "start_date":"10/10/2021",
                                                                "employee_id":"1"}}})

res = LL.get_tickets_filtered(req)



req = json.dumps({"key": "reports", "filter":"ticket_id",
                                             "filter_data":1})

res = LL.get_all(req)

req = json.dumps({"role": "boss","key":"report", "data": {
                "ticket_id":"2",
                "real_estate_id":"blabla",
                "description":"tharf ad gera asap",
                "employee_id":1,
                "destination":"Reykjavík",
                "total_price":22,
                "start_date":"2021,10,30",
                "ready":False,
                "closed":False
                
}})

#date format: yyyy,mm,dd
res = LL.post(req)

print(json.loads(res))
"""

"""
# example of getting reports filtered by ticket_id = 1
req = json.dumps({"key": "report", "data": {"filter":"ticket_id",
                                             "filter_value":"1"}})

res = LL.get_all(req)
"""

# example of getting all tickets filtered by period = [2021-10-10, 2021-10-11] (YYYY-MM-DD) and employee_id = 1
# diffrence from get_all() with filter flag is the key is not "filter" but "filters" 
"""
req = json.dumps({"key": "tickets", "data":{ "filters":["period","employee_id"],
                                             "filter_data":{ "start_date":"2020-12-03",
                                                                "end_date":"2020-12-03",
                                                                "employee_id":"1"}}})


res = LL.get_tickets_filtered(req)

print(json.loads(res))
"""

"""
    "type": "object",
    "key": "report",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "ticket_id": {"type":"number"},
        "real_estate_id": {"type": "number"},
        "description": {"type": "string"},
        "employee_id": {"type": "number"},
        "destination": {"type": "string"},
        "total_price": {"type": "float"},
        "contractor_id": {"type": "list"},
        "contractor_pay": {"type": "float"},
        "start_date": {"type": "string"},
        "close_date": {"type": "string"},
        "ready": {"type": "bool"},
        "closed": {"type": "bool"},
        "comments": {"type": "list"},
    },
}
"""

print(json.dumps({"key":"ticket","data":{"id":1}}))

res = LL.get(json.dumps({"key":"ticket","data":{"id":1}}))
print(json.loads(res))
print('-'*60)
print(type(json.loads(res)['data']))