import unittest
from Logic.LogicAPI import LogicAPI
import json
import os




#put to fail
put_data_2 = json.dumps({"role": "employee",
                        "key": "employee",
                        "data": {
                            "id": '1',
                            "email": "this_wont_work@ru.is",
                            }
                        })

#this will pass in setUp
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
                            "email": "test_email1@ru.is",
                            "destination": "Reykjavík",
                            "tickets": "[]",
                            "reports": "[]",
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
                            "email": "test_email1@ru.is",
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


    def test_post_employee(self):
        """Try to post new employee that violates key constraint"""
        res = self.LL.post(new_emp2)
        self.assertFalse(res)

    def test_put_employee(self):
        """We change the employee we made in setUp"""
        put_data_1 = json.dumps({"role": "boss",
                        "key": "employee",
                        "data": {
                            "id": str(self.id),
                            "email": "post_test@ru.is",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])


    def test_put_employee_to_fail(self):
        """We try to change employee details as regular employee"""
        res = self.LL.put(put_data_2)
        self.assertFalse(res)


    def test_delete_emp(self):
        put_data_delete = json.dumps({"role": "boss",
                        "key": "employee",
                        "data": {
                            "id": str(self.id),
                            }
                        })
        res = self.LL.put(put_data_delete)
        print("Type of response in put: "+str(type(res)))



if __name__ == '__main__':
    unittest.main()
