from django.test import TestCase

class TestGeneral(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def test_tautology(self):
        self.assertEquals(True, True)

