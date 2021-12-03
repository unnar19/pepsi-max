import unittest
from Logic.LogicAPI import LogicAPI
import json


new_real_estate = json.dumps({ "role": "boss",
                        "key": "real_estate",
                        "data": {
                            "real_estate_id": "blalba",
                            "address": "pound town",
                            "destination": "Nuuk",
                            "maintenance_info": "blibli",
                            "tickets": "[]",
                            "reports": "[]"
                        }
                    })

class TestRealEstate(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera emp, reyni svo ad gera 
            annann med sama email, thad á að feila, breyti svo upphaflega gæjanum 
            þannig að næst þegar þetta keyrir þá er sá gæji "ekki til"
        """
        self.LL = LogicAPI()


    def test_post_real_estate(self):
        res = self.LL.post(new_real_estate)
        self.assertTrue(res)

    def test_put_real_estate(self):
        pass

    def test_put_real_estate_fail(self):
        pass

if __name__ == '__main__':
    unittest.main()
