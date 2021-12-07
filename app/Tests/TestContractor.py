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
                            "phone": "5555555",
                            }
                        })

#this will pass in setUp
new_cont1 = json.dumps({ "role": "boss",
                        "key": "contractor",
                        "data": {
                            "name": "contname",
                            "contact": "tom",
                            "phone": "9999999",
                            "opening_hours": "1-2",
                            "destination": "Nuuk",
                            "tickets": "[]",
                            }
                        })
#this will fail
new_cont2 = json.dumps({ "role": "boss",
                        "key": "contractor",
                        "data": {
                            "name": "contractor2",
                            "contact": "michelinmaðurinn",
                            "phone": "9898989",
                            "opening_hours": "15-20",
                            "destination": "Reykjavík",
                            "tickets": "[]",
                            }
                        })


class TestContractor(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera cont, reyni svo ad gera 
            annann med sama símanumer, thad á að feila, breyti svo upphaflega gæjanum 
            þannig að næst þegar þetta keyrir þá er sá gæji "ekki til"
        """
        self.LL = LogicAPI()
        res = json.loads(self.LL.post(new_cont1))
        self.id = res["data"]["id"]
    
    def test_put_contractor(self):
        """We change the contractor we made in setUp"""
        put_data_1 = json.dumps({"role": "boss",
                        "key": "contractor",
                        "data": {
                            "id": str(self.id),
                            "phone": "6767676",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])

    def test_put_contractor_to_fail(self):
        """We try to change contractor details as regular employee"""
        res = json.loads(self.LL.put(put_data_2))
        self.assertFalse(res["type"])

    def test_get_contractor(self):
        data = json.dumps({
            "key":"contractor",
            "data":{"id": '6'}
        })
        res = json.loads(self.LL.get(data))
        self.assertEqual(res['data']['name'], 'Bryan Adams')

    def test_filter_contractor(self):
        data = json.dumps(
            {
                "key": "contractor",
                "filter": True,
                "data": {
                    "filter": "destination",
                    "filter_value": "Cumtown"
                }
            }
        )
        res = json.loads(self.LL.get_all(data))
        self.assertEqual(res['data']['3']['name'], 'baron von flanagan')

    @classmethod
    def tearDownClass(self):
        put_data_delete = json.dumps({
                        "role": "boss",
                        "key": "contractor",
                        "data": {
                            "id": str(self.id),
                            }
                        })
        res = json.loads(self.LL.delete(put_data_delete))
    


if __name__ == '__main__':
    unittest.main()
