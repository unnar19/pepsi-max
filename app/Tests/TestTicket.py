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
                            "contractor_id": "0",
                            "destination": "Nuuk",
                            "start_date": "2020-12-03",
                            "close_date": "future",
                            "priority": "Emergency",
                            "ready": False,
                            "closed": False,
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
                            "contractor_id": "0",
                            "destination": "Reykjavík",
                            "start_date": "2020-12-03",
                            "close_date": "future",
                            "priority": "Now",
                            "ready": False,
                            "closed": False,
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
                            "priority": "As soon as possible",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])

    def test_put_ticket_to_fail(self):
        """We try to change ticket details as regular employee"""
        res = json.loads(self.LL.put(put_data_2))
        self.assertFalse(res["type"])

    def test_put_ready_in_ticket_as_employee(self):
        """We change the ready status of the ticket we made in setUp as an employee"""
        put_data_1 = json.dumps({"role": "employee",
                        "key": "ticket",
                        "data": {
                            "id": str(self.id),
                            "ready": True,
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])

    def test_get_ticket(self):
        data = json.dumps({
            "key":"ticket",
            "data":{"id": '2'}
        })
        res = json.loads(self.LL.get(data))
        self.assertEqual(res['data']['priority'], 'Emergency')

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
        self.assertEqual(res['data']['1']['destination'], 'Nuuk')

    def test_autofill(self):
        """We try to post a ticket while only filling in the required fields"""
        new_ticket4 = json.dumps({ "role": "boss",
                        "key": "ticket",
                        "data": {
                            "real_estate_id": "kl",
                            "description": "Pick up dog from hell",
                            "employee_id": "5",
                            "destination": "Nuuk",
                            "start_date": "2020-12-03",
                            }
                        })
        res = json.loads(self.LL.post(new_ticket4))
        self.assertTrue(res["type"])

    def test_required_fields(self):
        """We try to post a ticket while not filling in all the required fields"""
        new_ticket4 = json.dumps({ "role": "boss",
                        "key": "ticket",
                        "data": {
                            "real_estate_id": "kl",
                            "description": "Pick up dog from hell",
                            "employee_id": "5",
                            "start_date": "2020-12-03",
                            }
                        })
        res = json.loads(self.LL.post(new_ticket4))
        self.assertFalse(res["type"])

    def test_multiple_filtering(self):
        req = json.dumps({"key": "tickets", "data":{ "filters":["period","destination"],
                                             "filter_data":{ "start_date":"2020-01-01",
                                                                "end_date":"2021-01-01",
                                                                "destination":"Reykjavík"}}})
        res = json.loads(self.LL.get_tickets_filtered(req))
        self.assertTrue(res["type"])

    def test_more_than_two_filtering(self):
        req = json.dumps({"key": "tickets", "data":{ "filters":["period","destination","employee_id"],
                                             "filter_data":{ "start_date":"2020-01-01",
                                                                "end_date":"2021-01-01",
                                                                "destination":"Reykjavík",
                                                                "employee_id":"1"}}})
        res = json.loads(self.LL.get_tickets_filtered(req))
        print(res)
        self.assertTrue(res["type"])

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
