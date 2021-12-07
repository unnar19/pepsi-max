employee_schema = {
    "type": "object",
    "key": "employee",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "role": {"type":"string"},
        "name": {"type": "string"},
        "password": {"type": "string"},
        "ssn": {"type": "number"},
        "address": {"type": "string"},
        "home_phone": {"type": "number"},
        "mobile_phone": {"type": "number"},
        "email": {"type": "string"},
        "destination": {"type": "string"},
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
        "real_estate_id": {"type": "string"},
        "address": {"type": "string"},
        "destination": {"type": "string"},
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
        "id": {"type": "number"},
        "airport": {"type": "string"},
        "country": {"type": "string"},
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
        "destination": {"type": "string"},
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

ticket_schema = {
    "type": "object",
    "key": "ticket",
    "role": {"type": "string"},
    "data": {
        "id": {"type": "number"},
        "report_id": {"type": "number"},
        "real_estate_id": {"type": "list"},
        "description": {"type": "string"},
        "employee_id": {"type": "number"},
        "destination": {"type": "tring"},
        "start_date": {"type": "string"},
        "close_date": {"type": "string"},
        "priority": {"type": "bool"},
        "open": {"type": "bool"},
        "is_recurring": {"type": "bool"},
    },
}
