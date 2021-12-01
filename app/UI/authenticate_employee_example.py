from Logic.LogicAPI import LogicAPI
import json

data_dict = {
    "key": "employee", # Verður að vera svo LogicAPI sendi á réttan database
    "data": {
        "email": "ChangeMe", # Gögnin sem þú þarft að senda til að auðkenna
        "password": "ChangeMe", # -||-
    },
}


email = str()
password = int()

data_dict['data']['email'] = email
data_dict['data']['password'] = password

# 1. formatta data_dict sem json

data = json.dumps(data_dict)

# 2. Kalla á LogicAPI.authenticate_employee og gefa honum json-data

response = LogicAPI.authenticate_employee(data) # <- þetta er json strengur

response_dict = json.loads(response) # <- þetta er dictionary


# Vista öll þessi gögn í UI!! Mikilvægt <3
id = response_dict['data']['id']
role = response_dict['data']['role']
name = response_dict['data']['name']
isloggedin = True