import unittest
from Logic.LogicAPI import LogicAPI
import json
import os
unittest.TestLoader.sortTestMethodsUsing = None





#put to fail
put_data_2 = json.dumps({"role": "employee",
                        "key": "contractor",
                        "data": {
                            "id": '1',
                            "email": "this_wont_work@ru.is",
                            }
                        })

#this will pass in setUp
new_emp1 = json.dumps({ "role": "boss",
                        "key": "employee",
                        "data": {
                            "name": "",
                            "contact": "",
                            "phone": "",
                            "opening_hours": "",
                            "destination": "",
                            "tickets": "[]",
                            }
                        })
#this will fail
new_emp2 = json.dumps({ "role": "boss",
                        "key": "employee",
                        "data": {
                            "role": "employee",
                            "name": "Jón",
                            "password": "yummy",
                            "ssn": "1112922559",
                            "address": "Kárastígur 5",
                            "home_phone": "5812345",
                            "mobile_phone": "8885555",
                            "email": "blabla@ru.is",
                            "destination": "Reykjavík",
                            "tickets": "[]",
                            "reports": "[]",
                            }
                        })


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera emp, reyni svo ad gera 
            annann med sama email, thad á að feila, breyti svo upphaflega gæjanum 
            þannig að næst þegar þetta keyrir þá er sá gæji "ekki til"
        """
        self.LL = LogicAPI()
        res = json.loads(self.LL.post(new_emp1))
        self.id = res["data"]["id"]
    
    def test_put_employee(self):
        """We change the employee we made in setUp"""
        put_data_1 = json.dumps({"role": "boss",
                        "key": "employee",
                        "data": {
                            "id": str(self.id),
                            "name": "einar",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])


    def test_authenticate(self):
        data = json.dumps({
            "key":"employee",
            "data":{"email":"test_email1@ru.is",
                    "password": "TestPassword"}
        })
        res = json.loads(self.LL.authenticate_employee(data))
        self.assertEqual(res["data"]["name"], "TestEmployee")


    def test_put_employee_to_fail(self):
        """We try to change employee details as regular employee"""
        res = json.loads(self.LL.put(put_data_2))
        self.assertFalse(res["type"])

    def test_get_employee(self):
        data = json.dumps({
            "key":"employee",
            "data":{"id": '13'}
        })
        res = json.loads(self.LL.get(data))
        self.assertEqual(res['data']['name'], 'Charlie Adams')

    def test_filter_employee(self):
        data = json.dumps(
            {
                "key": "employee",
                "filter": True,
                "data": {
                    "filter": "destination",
                    "filter_value": "Cumtown"
                }
            }
        )
        res = json.loads(self.LL.get_all(data))
        self.assertEqual(res['data']['20']['name'], 'Gunnar Rassahlíð')

    @classmethod
    def tearDownClass(self):
        put_data_delete = json.dumps({
                        "role": "boss",
                        "key": "employee",
                        "data": {
                            "id": str(self.id),
                            }
                        })
        res = json.loads(self.LL.delete(put_data_delete))
    


if __name__ == '__main__':
    unittest.main()

