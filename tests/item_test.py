import unittest
from db.run_sql import run_sql
from models.item import Item
import repositories.item_repository as item_repo
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

class TestItem(unittest.TestCase):
    def setUp(self):
        self.wizard = Wizard("Norman", "Stargazer", 1000)
        self.item = Item("Hat", "Grey", "Standard; rounded point", self.wizard)
        
    # @unittest.skip("Delete this line to run the test")
    def test_item_has_colour(self):
        self.assertEqual("Grey", self.item.colour)

