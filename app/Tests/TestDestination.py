import unittest
from Logic.LogicAPI import LogicAPI
import json
import os
unittest.TestLoader.sortTestMethodsUsing = None

#put to fail
put_data_2 = json.dumps({"role": "employee",
                        "key": "destination",
                        "data": {
                            "id": '1',
                            "phone": "5555555",
                            }
                        })

#this will pass in setUp
new_dest1 = json.dumps({ "role": "boss",
                        "key": "destination",
                        "data": {
                            "airport": "Helsinki",
                            "country": "Finland",
                            "phone": "9999999",
                            "opening_hours": "1-2",
                            "manager_id": "6",
                            }
                        })
#this will fail
new_dest2 = json.dumps({ "role": "boss",
                        "key": "destination",
                        "data": {
                            "airport": "Helsinki",
                            "country": "Finland",
                            "phone": "8888888",
                            "opening_hours": "1-2",
                            "manager_id": "7",
                            }
                        })


class TestDestination(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera dest, reyni svo ad gera 
            annann med sama flugvöll, thad á að feila, breyti svo upphaflega gæjanum 
            þannig að næst þegar þetta keyrir þá er sá gæji "ekki til"
        """
        self.LL = LogicAPI()
        res = json.loads(self.LL.post(new_dest1))
        self.id = res["data"]["id"]
    
    def test_put_destination(self):
        """We change the destination we made in setUp"""
        put_data_1 = json.dumps({"role": "boss",
                        "key": "destination",
                        "data": {
                            "id": str(self.id),
                            "phone": "6767676",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])

    def test_put_destination_to_fail(self):
        """We try to change destination details as regular employee"""
        res = json.loads(self.LL.put(put_data_2))
        self.assertFalse(res["type"])

    def test_get_destination(self):
        data = json.dumps({
            "key":"destination",
            "data":{"id": '3'}
        })
        res = json.loads(self.LL.get(data))
        self.assertEqual(res['data']['airport'], 'Kulusuk')

    def test_filter_destination(self):
        data = json.dumps(
            {
                "key": "destination",
                "filter": True,
                "data": {
                    "filter": "country",
                    "filter_value": "Grænland"
                }
            }
        )
        res = json.loads(self.LL.get_all(data))
        self.assertEqual(res['data']['2']['airport'], 'Nuuk')

    @classmethod
    def tearDownClass(self):
        put_data_delete = json.dumps({
                        "role": "boss",
                        "key": "destination",
                        "data": {
                            "id": str(self.id),
                            }
                        })
        res = json.loads(self.LL.delete(put_data_delete))
    


if __name__ == '__main__':
    unittest.main()
