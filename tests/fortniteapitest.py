import unittest
import FortniteAPI

class TestStringMethods(unittest.TestCase):

    def test_getLifeTimeStats(self):
        help = FortniteAPI.totalWins('Zerutule2')