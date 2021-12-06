Verklegt Námskeið 1 | T-113-VLN1 | Hópur 43
===========================================
![Image](https://i.imgur.com/f9GuSPR.png "Poster")

# About

# Models

The system implements the following models:

- Employee
- Destination
- Ticket
- Report
- RealEstate
- Destination

The model schemas can be found in "app/Models/Schemas.py"

# Data API
The data API implements a post, get, get_all and put methood for all models. 

The API takes JSON objects as parameters for all functions and returns JSON objects.

That is the Data API can post a new employee with the following syntax:

    new_employee = json.dumps({
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

Where the key defines which model the post methood is for.

# Logic Api
The logic API implements CRUD methoods for the system. As well as implementing a filter and search.

An example of a get_all() call where you want all employees in Reykjavík:

    get_all_in_reykjavik = {
                            "key":"employee",
                            "filter":"destination", 
                            "filter_value":"Reykjavík"}

Where the filter field specifies which field to filter and the filter_value what value to search for. 

# UI
