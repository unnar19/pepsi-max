employee_schema = {
    "type": "object",
    "data": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "password": {"type": "string"},
        "ssn": {"type": "number"},
        "address": {"type": "string"},
        "home_phone": {"type": "number"},
        "mobile_phone": {"type": "number"},
        "email": {"type": "string"},
        "location": {"type": "string"},
    },
}

real_estate_schema = {
    "type": "object",
    "data": {
        "id": {"type": "number"},
        "address": {"type": "string"},
        "location": {"type": "string"},
        "maintenance_info": {"type": "string"},
    },
}

destination_schema = {
    "type": "object",
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
    "data": {
        "id": {"type": "number"},
        "real_estate_id": {"type": "list"},
        "work_description": {"type": "string"},
        "employees": {"type": "list"},
        "total_price": {"type": "float"},
        "contractor_id": {"type": "list"},
        "contractor_pay": {"type": "float"},
        "evaluation_of_contractor": {"type": "string"},
        "start_date": {"type": "string"},
        "time_period": {"type": "string"},
        "status": {"type": "string"},
        "was_recurring": {"type": "bool"},
    },
}

ticket_schema = {
    "type": "object",
    "data": {
        "id": {"type": "number"},
        "report_id": {"type": "number"},
        "real_estate_id": {"type": "list"},
        "work_description": {"type": "string"},
        "employees": {"type": "list"},
        "start_date": {"type": "string"},
        "importance": {"type": "string"},
        "status": {"type": "string"},
        "is_recurring": {"type": "bool"},
        "comments": {"type": "list"},
    },
}
