from Logic.LogicAPI import LogicAPI
import json

def test_authenticate_employee(unnar_logic_api):
    data_dict = {
        "key": "employee", # Verður að vera svo LogicAPI sendi á réttan database
        "data": {
            "email": "ChangeMe", # Gögnin sem þú þarft að senda til að auðkenna
            "password": "ChangeMe", # -||-
        },
    }


    email = "Einar@kingsi.is"
    password = "12345"

    data_dict['data']['email'] = email
    data_dict['data']['password'] = password

    # 1. formatta data_dict sem json

    data = json.dumps(data_dict)

    # 2. Kalla á LogicAPI.authenticate_employee og gefa honum json-data
    response = unnar_logic_api.authenticate_employee(data) # <- þetta er json strengur

    if not response:
        print('Try again later')
        return False    
    response_dict = json.loads(response) # <- þetta er dictionary


    # Vista öll þessi gögn í UI!! Mikilvægt <3
    id = response_dict['data']['id']
    role = response_dict['data']['role']
    name = response_dict['data']['name']
    isloggedin = True

def test_register_employee(unnar_logic_api):
    employee_data = {"role": "Boss",
    "key": "employee",
    "data": {
        "role": "employee",
        "name": "Jón",
        "password": "yummy",
        "ssn": "1112922559",
        "address": "Kárastígur 5",
        "home_phone": "5812345",
        "mobile_phone": "8885555",
        "email": "jon@ru.is",
        "location": "Reykjavík",
        "tickets": "[]",
        "reports": "[]",
        }
    }

    return unnar_logic_api.post(json.dumps(employee_data))


if __name__ == '__main__':
    unnar_logic_api = LogicAPI()
    test_authenticate_employee(unnar_logic_api)
    print(test_register_employee(unnar_logic_api))