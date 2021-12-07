import unittest
from Logic.LogicAPI import LogicAPI
import json
import os
unittest.TestLoader.sortTestMethodsUsing = None


#this will pass in setUp
new_real_estate1 = json.dumps({ "role": "boss",
                        "key": "real_estate",
                        "data": {
                            "real_estate_id": "huhuhu",
                            "address": "pound town",
                            "destination": "Nuuk",
                            "maintenance_info": "blibli",
                            "tickets": "[]",
                            "reports": "[]"
                        }
                    })

#this will fail
new_real_estate2 = json.dumps({ "role": "boss",
                        "key": "real estate",
                        "data": {
                            "real_estate_id": "huhuhu",
                            "address": "hverfis skata 2",
                            "destination": "Reykjavík",
                            "maintenance_info": "fix this skate",
                            "tickets": "[]",
                            "reports": "[]"
                            }
                        })



class TestRealEstate(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera real estate, reyni 
            svo ad gera annað med sama real_estate_id, thad á að feila, breyti 
            svo upphaflega gæjanum þannig að næst þegar þetta keyrir þá er sá 
            gæji "ekki til"
        """
        self.LL = LogicAPI()
        res = json.loads(self.LL.post(new_real_estate1))
        self.id = res["data"]["id"]


    def test_post_real_estate(self):
        """Try to post new real estate that violates key constraint"""
        res = json.loads(self.LL.post(new_real_estate1))
        self.assertFalse(res["type"])

    def test_put_real_estate(self):
        """We change the real estate we made in setUp"""
        put_data_1 = json.dumps({"role": "boss",
                        "key": "real_estate",
                        "data": {
                            "id": str(self.id),
                            "real_estate_id": "onlln",
                            }
                        })
        res = json.loads(self.LL.put(put_data_1))
        self.assertTrue(res["type"])

    def test_put_real_estate_to_fail(self):
        """We try to change real estate details as regular employee"""
        put_data_2 = json.dumps({"role": "employee",
                        "key": "real_estate",
                        "data": {
                            "id": str(self.id),
                            "real_estate_id": "no id",
                            }
                        })
        res = json.loads(self.LL.put(put_data_2))
        self.assertFalse(res["type"])

    def test_get_real_estate(self):
        data = json.dumps({
            "key":"real_estate",
<<<<<<< HEAD
            "data":{"id": '5'}
=======
            "data":{"id": '1'}
>>>>>>> a7f45b7cb8be5fe2dba59008d6e12e35c26e1ae7
        })
        res = json.loads(self.LL.get(data))
        self.assertEqual(res['data']['address'], 'pound town')
        
    def test_filter_real_estate(self):
        data = json.dumps(
            {
                "key": "real_estate",
                "filter": True,
                "data": {
                    "filter": "destination",
                    "filter_value": "Nuuk"
                }
            }
        )
        res = json.loads(self.LL.get_all(data))
        self.assertEqual(res['data']['1']['address'], 'pound town')

    @classmethod
    def tearDownClass(self):
        put_data_delete = json.dumps({
                        "role": "boss",
                        "key": "real_estate",
                        "data": {
                            "id": str(self.id),
                            }
                        })
        res = json.loads(self.LL.delete(put_data_delete))


    

if __name__ == '__main__':
    unittest.main()
