"""
    Even though the package used is called unittest the tests 
    This file runns (see sub test files in app/tests) should
    not be regarded as unit tests, they are more of a integration
    tests as the requests sent here go all the way from logicAPI
    down to the Data layer. 

    If integration tests fail it can be hell to debug so write them carefully
"""

from json import encoder
from Tests import TestEmployee
from Tests import TestRealEstate
from Tests import TestTicket
import unittest
import json

if __name__ == "__main__":
    print("-"*27+" Employee Tests " +"-"*27)
    unittest.main(defaultTest="TestEmployee", exit=False)
    print("-"*26+" RealEstate Tests " +"-"*26)
    unittest.main(defaultTest="TestRealEstate", exit=False)
    print("-"*28+" Ticket Tests " +"-"*28)
    unittest.main(defaultTest="TestTicket", exit=False)

