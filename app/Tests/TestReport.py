import unittest
from Logic.LogicAPI import LogicAPI
import json
import os
unittest.TestLoader.sortTestMethodsUsing = None

#put to fail
put_data_2 = json.dumps({"role": "employee",
                        "key": "report",
                        "data": {
                            "id": '1',
                            "ready": "1",
                            }
                        })

#this will pass in setUp
new_report1 = json.dumps({ "role": "boss",
                        "key": "report",
                        "data": {
                            "ticket_id": "3",
                            "real_estate_id": "hjhjhj",
                            "description": "kaupa hvítann monster",
                            "employee_id": "1",
                            "destination": "Kulusuk",
                            "total_price": "1500 kr",
                            "contractor_id": "1",
                            "contractor_pay": "700 kr",
                            "date": "901.11.11",
                            "approved": False,
                            "comments": "[]",
                            }
                        })
#this will fail
new_report2 = json.dumps({ "role": "boss",
                        "key": "report",
                        "data": {
                            "ticket_id": "4",
                            "real_estate_id": "k",
                            "description": "hit the booty dew",
                            "employee_id": "1",
                            "destination": "Nuuk",
                            "total_price": "6kr",
                            "contractor_id": "2",
                            "contractor_pay": "6kr",
                            "date": "901.11.11",
                            "approved": False,
                            "comments": "[]",
                            }
                        })


class TestReport(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera report, reyni svo ad gera 
            annann med sama flugvöll, thad á að feila, breyti svo upphaflegu reportinu 
            þannig að næst þegar þetta keyrir þá er það report "ekki til"
        """
        self.LL = LogicAPI()
        res = json.loads(self.LL.post(new_report1))
        self.id = res["data"]["id"]
    
    def test_put_report(self):
        """We change the report we made in setUp"""
        put_data_1 = json.dumps({"role": "boss",
                        "key": "report",
                        "data": {
                            "id": str(self.id),
                            "total_price": "6767676",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])

    def test_put_report_to_fail(self):
        """We try to change report details as regular employee"""
        res = json.loads(self.LL.put(put_data_2))
        self.assertFalse(res["type"])

    def test_get_report(self):
        data = json.dumps({
            "key":"report",
            "data":{"id": '2'}
        })
        res = json.loads(self.LL.get(data))
        self.assertEqual(res['data']['real_estate_id'], 'brundfata')

    def test_filter_report(self):
        data = json.dumps(
            {
                "key": "report",
                "filter": True,
                "data": {
                    "filter": "destination",
                    "filter_value": "Nuuk"
                }
            }
        )
        res = json.loads(self.LL.get_all(data))
        self.assertEqual(res['data']['2']['real_estate_id'], 'brundfata')

    def test_post_report_as_employee(self):
        """Tests if employees can post reports, which they should"""
        new_report3 = json.dumps({ "role": "employee",
                        "key": "report",
                        "data": {
                            "ticket_id": "5",
                            "real_estate_id": "p",
                            "description": "hit the booty dew",
                            "employee_id": "1",
                            "destination": "Nuuk",
                            "total_price": "6kr",
                            "contractor_id": "2",
                            "contractor_pay": "6kr",
                            "date": "901.11.11",
                            "approved": False,
                            "comments": "[]",
                            }
                        })
        res = json.loads(self.LL.post(new_report3))
        self.assertTrue(res["type"])

    def test_autofill(self):
        """We try to post a report while only filling in the required fields"""
        new_report4 = json.dumps({ "role": "boss",
                        "key": "report",
                        "data": {
                            "real_estate_id": "kl",
                            "description": "do the stanky leg",
                            "employee_id": "3",
                            "destination": "Reykjavík",
                            "date": "901.11.12",
                            "approved": False,
                            }
                        })
        res = json.loads(self.LL.post(new_report4))
        self.assertTrue(res["type"])

    @classmethod
    def tearDownClass(self):
        put_data_delete = json.dumps({
                        "role": "boss",
                        "key": "report",
                        "data": {
                            "id": str(self.id),
                            }
                        })
        res = json.loads(self.LL.delete(put_data_delete))
    
if __name__ == '__main__':
    unittest.main()
