import unittest
from db.run_sql import run_sql
from models.item import Item
import repositories.item_repository as item_repo
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo
from models.loss import Loss
import repositories.loss_repository as loss_repo

class TestLoss(unittest.TestCase):
    def setUp(self):
        wizard = Wizard("Norman", "Stargazer", 1000)
        item = Item("Hat", "Pink", "Glittery", wizard)
        self.loss = Loss(2020-2-2, "Lost at event at Gimli's Nightclub", wizard, item)

    # @unittest.skip("Delete this line to run the test")
    def test_loss_has_details(self):
        self.assertEqual(False, self.loss.recovered)

