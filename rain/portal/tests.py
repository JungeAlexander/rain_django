from django.test import TestCase

from .models import RNA


class RNAMethodTests(TestCase):

    def test_is_mirna_with_smirna(self):
        """
        is_mirna() should return False for identifier smiRNA
        """
        smirna = RNA(identifier='smiRNA')
        self.assertEqual(smirna.is_mirna(), False)


    def test_is_mirna_with_mirna(self):
        """
        is_mirna() should return False for identifier smiRNA
        """
        mirna = RNA(identifier='miRNA-')
        self.assertEqual(mirna.is_mirna(), True)
