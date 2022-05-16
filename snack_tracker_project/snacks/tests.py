from django.test import TestCase
from django.urls import reverse

class SnacksTest(TestCase):
    def test_snacks_list_status_code(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_snacks_list_template(self):
        response = self.client.get(reverse('snacks_list'))
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    # def test_snacks_details_status_code(self):
    #     url = reverse('snack_details', args=[1])
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)
    
    # def test_snacks_details_template(self):
    #     response = self.client.get(reverse('snack_details', args=[1]))
    #     self.assertTemplateUsed(response, 'snack_detail.html')