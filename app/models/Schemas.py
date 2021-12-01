employee_schema = {
    "type": "object",
    "key": "employee",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "role": {"type":"string"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "password": {"type": "string"},
        "ssn": {"type": "number"},
        "address": {"type": "string"},
        "home_phone": {"type": "number"},
        "mobile_phone": {"type": "number"},
        "email": {"type": "string"},
        "location": {"type": "string"},
        "tickets": {"type":"array"},
        "reports": {"type":"array"},
    },
}

real_estate_schema = {
    "type": "object",
    "key": "real_estate",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "address": {"type": "string"},
        "location": {"type": "string"},
        "maintenance_info": {"type": "string"},
        "tickets": {"type":"array"},
        "reports": {"type":"array"},
    },
}

destination_schema = {
    "type": "object",
    "key": "destination",
    "role": {"type": "string"},
    "data": {
        "airport": {"type": "string"},
        "location": {"type": "string"},
        "phone": {"type": "int"},
        "opening_hours": {"type": "string"},
        "manager": {"type": "string"},
    },
}

contractor_schema = {
    "type": "object",
    "key": "contractor",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "contact": {"type": "string"},
        "phone": {"type": "int"},
        "opening_hours": {"type": "string"},
        "location": {"type": "string"},
        "tickets" : {"type": "list"},
    },
}

report_schema = {
    "type": "object",
    "key": "report",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "ticket_id": {"type":"number"},
        "real_estate_id": {"type": "number"},
        "work_description": {"type": "string"},
        "employees": {"type": "list"},
        "total_price": {"type": "float"},
        "contractor_id": {"type": "list"},
        "contractor_pay": {"type": "float"},
        "evaluation_of_contractor": {"type": "string"},
        "time_period": {"type": "string"},
        "status": {"type": "string"},
    },
}

ticket_schema = {
    "type": "object",
    "key": "ticket",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "report_id": {"type": "number"},
        "real_estate_id": {"type": "list"},
        "work_description": {"type": "string"},
        "employees": {"type": "list"},
        "start_date": {"type": "string"},
        "close_date": {"type": "string"},
        "priority": {"type": "string"},
        "status": {"type": "string"},
        "is_recurring": {"type": "bool"},
        "comments": {"type": "list"},
    },
}
