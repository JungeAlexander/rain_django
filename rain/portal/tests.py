from django.core.urlresolvers import reverse
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


def create_rna(identifier, description):
    """
    Creates a RNA with the given `identifier` and `description`.
    """
    return RNA.objects.create(identifier=identifier, description=description)


class RNAViewTests(TestCase):
    def test_index_view_with_no_rnas(self):
        """
        If no RNAs exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('portal:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No entities found.")
        self.assertQuerysetEqual(response.context['entity_list'], [])

    def test_index_view_with_an_rna_with_description(self):
        """
        RNA with a non-empty description should be displayed.
        """
        create_rna(identifier="myRNA", description='This is myRNA.')
        response = self.client.get(reverse('portal:index'))
        self.assertQuerysetEqual(
            response.context['entity_list'],
            ['<RNA: myRNA>']
        )

    def test_index_view_with_an_rna_without_description(self):
        """
        RNA with an empty description should not be displayed.
        """
        create_rna(identifier="myRNA", description='')
        response = self.client.get(reverse('portal:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No entities found.")
        self.assertQuerysetEqual(response.context['entity_list'], [])


class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_an_rna_without_description(self):
        """
        The detail view of an RNA without description should
        return a 404 not found.
        """
        rna = create_rna(identifier='XYZ', description='')
        url = reverse('portal:rna_detail', args=(rna.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_an_rna_with_description(self):
        """
        The detail view of an RNA without description should
        display the RNA identifier and description.
        """
        rna = create_rna(identifier="myRNA", description='This is myRNA.')
        url = reverse('portal:rna_detail', args=(rna.id,))
        response = self.client.get(url)
        self.assertContains(response, rna.identifier)
        self.assertContains(response, rna.description)
