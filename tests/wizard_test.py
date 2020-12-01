import unittest
from db.run_sql import run_sql
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

class TestWizard(unittest.TestCase):
    def setUp(self):
        self.wizard = Wizard("Norman", "Stargazer", 1000)

    # @unittest.skip("Delete this line to run the test")
    def test_wizard_has_name(self):
        self.assertEqual("Norman", self.wizard.first_name)

