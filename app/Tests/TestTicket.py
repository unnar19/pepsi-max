import unittest
from Logic.LogicAPI import LogicAPI
import json

new_ticket = json.dumps(
    {
        "role": "boss",
        "key": "ticket",
        "data": {
            "description": "Put dog in dishwasher",
            "destination": "Nuuk",
            "start_date": "7.12.2021",
            "priority": "A",
            "is_recurring": False
        }
    }
)
class TestTicket(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera emp, reyni svo ad gera 
            annann med sama email, thad á að feila, breyti svo upphaflega gæjanum 
            þannig að næst þegar þetta keyrir þá er sá gæji "ekki til"
        """
        self.LL = LogicAPI()
        res = json.loads(self.LL.post(new_ticket))


    def test_post_ticket(self):
        pass

    def test_put_ticket(self):
        pass

    def test_put_ticket_to_fail(self):
        pass

if __name__ == '__main__':
    unittest.main()
