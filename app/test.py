import unittest
from Logic.LogicAPI import LogicAPI
import json

class TestLogEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.LLAPI = LogicAPI()
        #set up employee to test
        self.employee_data = {"role": "Boss",
            "key": "employee",
            "data": {
                "role": "employee",
                "name": "Jón",
                "password": "yummy",
                "ssn": "1112922559",
                "address": "Kárastígur 5",
                "home_phone": "5812345",
                "mobile_phone": "8885555",
                "email": "jon19@ru.is",
                "location": "Reykjavík",
                "tickets": "[]",
                "reports": "[]",
                }
            }
        self.AuthEmp = self.LLAPI.post(json.dumps(self.employee_data))


    def test_authenticate_employee(self):
        data_dict = {
            "key": "employee", # Verður að vera svo LogicAPI sendi á réttan database
            "data": {
                "email": "ChangeMe", # Gögnin sem þú þarft að senda til að auðkenna
                "password": "ChangeMe", # -||-
            },
        }

        email = "jon19@ru.is"
        password = "yummy"

        data_dict['data']['email'] = email
        data_dict['data']['password'] = password

        # 1. formatta data_dict sem json

        data = json.dumps(data_dict)

        # 2. Kalla á LogicAPI.authenticate_employee og gefa honum json-data
        response = self.LLAPI.authenticate_employee(data) # <- þetta er json strengur
        self.assertTrue(response)

    def test_update_employee(self):
        employee_data = {"role": "Boss",
        "key": "employee",
        "data": {
            "id": '2',
            "role": "employee",
            "name": "Eyþór Mikael",
            "address": "Njálsgata 19",
            "email": "mcshit@ru.is",
            "location": "Reykjavík",
            }
        }
        response = self.LLAPI.put(json.dumps(employee_data))
        self.assertTrue(response)

    def test_register(self):
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
                "email": "jon19@ru.is",
                "location": "Reykjavík",
                "tickets": "[]",
                "reports": "[]",
                }
            }
        response = self.LLAPI.post(json.dumps(employee_data))
        self.assertFalse(response)


if __name__ == '__main__':
    unittest.main()
