import unittest
from Logic.LogicAPI import LogicAPI
import json
import os
unittest.TestLoader.sortTestMethodsUsing = None


#put to fail
put_data_2 = json.dumps({"role": "employee",
                        "key": "ticket",
                        "data": {
                            "id": '1',
                            "phone": "5555555",
                            }
                        })

#this will pass in setUp
new_ticket1 = json.dumps({"role": "boss",
                        "key": "ticket",
                        "data": {
                            "report_id": "0",
                            "real_estate_id": "brundfata",
                            "description": "Put dog in dishwasher",
                            "employee_id": "2",
                            "destination": "Nuuk",
                            "start_date": "7.12.2021",
                            "close_date": "future",
                            "priority": "A",
                            "open": True,
                            "is_recurring": False,
                            }
                        })
#this will fail
new_ticket2 = json.dumps({ "role": "boss",
                        "key": "ticket",
                        "data": {
                            "report_id": "0",
                            "real_estate_id": "k",
                            "description": "Pick up dog from dishwasher",
                            "employee_id": "3",
                            "destination": "Reykjavík",
                            "start_date": "7.12.2021",
                            "close_date": "future",
                            "priority": "B",
                            "open": True,
                            "is_recurring": False,
                            }
                        })


class TestTicket(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera dest, reyni svo ad gera 
            annann med sama flugvöll, thad á að feila, breyti svo upphaflega gæjanum 
            þannig að næst þegar þetta keyrir þá er sá gæji "ekki til"
        """
        self.LL = LogicAPI()
        res = json.loads(self.LL.post(new_ticket1))
        self.id = res["data"]["id"]
    
    def test_put_ticket(self):
        """We change the ticket we made in setUp"""
        put_data_1 = json.dumps({"role": "boss",
                        "key": "ticket",
                        "data": {
                            "id": str(self.id),
                            "priority": "C",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])

    def test_put_ticket_to_fail(self):
        """We try to change ticket details as regular employee"""
        res = json.loads(self.LL.put(put_data_2))
        self.assertFalse(res["type"])

    def test_get_ticket(self):
        data = json.dumps({
            "key":"ticket",
            "data":{"id": '3'}
        })
        res = json.loads(self.LL.get(data))
        self.assertEqual(res['data']['priority'], 'A')

    def test_filter_ticket(self):
        data = json.dumps(
            {
                "key": "ticket",
                "filter": True,
                "data": {
                    "filter": "real_estate_id",
                    "filter_value": "k"
                }
            }
        )
        res = json.loads(self.LL.get_all(data))
        self.assertEqual(res['data']['2']['destination'], 'Reykjavík')

    @classmethod
    def tearDownClass(self):
        put_data_delete = json.dumps({
                        "role": "boss",
                        "key": "ticket",
                        "data": {
                            "id": str(self.id),
                            }
                        })
        res = json.loads(self.LL.delete(put_data_delete))
    


if __name__ == '__main__':
    unittest.main()
