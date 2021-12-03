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
import unittest
import json

if __name__ == "__main__":

    unittest.main(defaultTest="TestEmployee", exit=False)

