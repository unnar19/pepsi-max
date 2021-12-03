import unittest
from Logic.LogicAPI import LogicAPI
import json


class TestDestination(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        """ þar sem það er ekki delete methood þá verð ég að vera smá sniðugur
            með hvernig eg set upp testin, byrja a ad gera emp, reyni svo ad gera 
            annann med sama email, thad á að feila, breyti svo upphaflega gæjanum 
            þannig að næst þegar þetta keyrir þá er sá gæji "ekki til"
        """
        self.LL = LogicAPI()


    def test_post_destination(self):
        pass

    def test_put_destination(self):
        pass

    def test_put_destination_fail(self):
        pass

if __name__ == '__main__':
    unittest.main()
