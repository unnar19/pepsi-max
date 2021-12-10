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

An example of a get() call where you want the employee with the id 4:

    get_employee = {
                    "key":"employee",
                    "data":{"id":"4"}}

An example of a post() call where you want to register a new employee:

    post_employee = {
            "role":"boss"
            "key":"employee"
            "data": {
                "id":"5"
                "role":"Custodian"
                "name":"Walter Flanigan"
                "password":"imnormal"
                "ssn":"0405683478"
                "address":"Hverfis Skata 2"
                "home_phone":"8888888"
                "mobile_phone":"9999999"
                "email":"waltflanandson@nan.is"
                "destination":"Reykjavík"
                "tickets":"[]"
                "reports":"[]"}}

"role" is the job title of an employee, "key" is the category that the user wishes to post and data is the attributes of the employee. A user can only use the post() call if they have the role of "boss" or if they key is "report", all users can post a report.

An example of a put() call where you want to change an attribute of an employee:

    put_employee = {
            "role":"boss"
            "key":"employee"
            "data": {
                "id": "5",
                "home_phone": "5555555",}}

Only one attribute can be changed in one call. A user can only use the put() call if they have the role of "boss" or if the key is "ticket" and the latter key in data is "ready". The first key must always be "id".

An example of a delete() call where you want to delete an employee:

    delete_employee = {
                "role":"boss"
                "key":"employee"
                "data":{"id":"5"}}

Only a user with the role "boss" can call on delete().

Here are templates for all of the calls:

    get_all = {
                "key":"<key>",
                "data": {
                    "filter":"<filter_key>", 
                    "filter_value":"<filter_value>"}}

    get = {
            "key":"<key>",
            "data":{"id":"<id>"}}

    post = {
            "role":"<role>"
            "key":"<key>"
            "data": {
                "post_key":"<post_value>"
                ...
                "post_key":"<post_value>"}}

    put = {
            "role":"<role>"
            "key":"<key>"
            "data": {
                "id": "<id>",
                "put_key": "<put_value>",}}

    delete = {
                "role":"boss"
                "key":"<key>"
                "data":{"id":"<id>"}}


# UI
