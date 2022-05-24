from hero import *
import unittest

class TestHero(unittest.Testcase):

    def test_init(self):
        #check iig hero.name is a string and if hero.starting_helath is integer
        self.assert