from django.test import TestCase
from main.models import Gear
from django.urls import reverse


def sample_gear(**params):
    """Create and return a sample gear"""
    defaults = {
        'name': 'test',
        'size': '1.2 m',
        'avail_quantity': 5,
        'unit_price':6,
    }
    defaults.update(params)
    return Gear.objects.create(**defaults)


class GearTest(TestCase):
     """ Test module for Gear model """

     def setUp(self):
        """ Client setup for request and response"""
        print("hello")


     def test_get_all_gear(self):
          """ List all gear test. """

          gear = sample_gear()
          self.assertEqual(response.status_code, status.HTTP_200_OK)

        # def test_get_valid_single_dailyusage(self):
        #     """ Retrieve single valid dailyusage. """
        #     dailyusage = sample_dailyusage()
        #     itemused = sample_itemused()
        #     dailyusage.used_item.add(itemused)
        #     dailyusage.save()
        #     response = self.client.get(reverse('inventory_RUD_dailyusage', kwargs={'id': dailyusage.pk}))
        #     serializer = DailyUsageSerializer(dailyusage)
        #     self.assertEqual(response.data, serializer.data)
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        #
        # def test_get_invalid_single_dailyusage(self):
        #     """ Retrieve single invalid dailyusage. """
        #     response = self.client.get(reverse('inventory_RUD_dailyusage', kwargs={'id': 30}))
        #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        #
        # def test_create_valid_dailyusage(self):
        #     """ Create single valid dailyusage. """
        #     item = sample_item()
        #     valid_payload = {
        #         "used_item": [{
        #             "item": 2,
        #             "used_quantity": 4,
        #             "action": "add"
        #         }],
        #         "comment": "test"
        #     }
        #     response = self.client.post(reverse('inventory_create_daily_usage'),
        #                                 data=json.dumps(valid_payload),
        #                                 content_type='application/json')
        #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #
        # def test_create_invalid_dailyusage(self):
        #     """ Create single invalid dailyusage. """
        #     item = sample_item()
        #     invalid_payload = {
        #         "used_item": [{
        #             "item": "",
        #             "used_quantity": "",
        #             "action": ""
        #         }],
        #         "comment": ""
        #     }
        #     response = self.client.post(reverse('inventory_create_daily_usage'),
        #                                 data=json.dumps(invalid_payload),
        #                                 content_type='application/json')
        #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        #
        # def test_valid_delete_dailyusage(self):
        #     """ Delete single valid dailyusage. """
        #     dailyusage = sample_dailyusage()
        #     itemused = sample_itemused()
        #     dailyusage.used_item.add(itemused)
        #     dailyusage.save()
        #     response = self.client.delete(reverse('inventory_RUD_dailyusage', kwargs={'id': dailyusage.pk}))
        #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #
        # # def test_invalid_delete_dailyusage(self):
        # #     """ Delete single invalid dailyusage. """
        # #     response = self.client.delete(reverse('inventory_RUD_dailyusage', kwargs={'id':30}))
        # #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        #
        # def test_valid_update_dailyusage(self):
        #     """ Update single valid dailyusage. """
        #     dailyusage = sample_dailyusage()
        #     itemused = sample_itemused()
        #     dailyusage.used_item.add(itemused)
        #     dailyusage.save()
        #     # items = Item.objects.all().values()
        #     # print(items)
        #     valid_payload = {
        #         "used_item": [{
        #             "item": 8,
        #             "used_quantity": 1,
        #             "action": "add"
        #         }],
        #         "comment": "changed"
        #     }
        #     response = self.client.put(
        #         reverse('inventory_RUD_dailyusage', kwargs={'id': dailyusage.pk}),
        #         data=json.dumps(valid_payload),
        #         content_type='application/json'
        #     )
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        #
        # def test_valid_partial_update_dailyusage(self):
        #     """ Update single valid dailyusage. """
        #     dailyusage = sample_dailyusage()
        #     itemused = sample_itemused()
        #     dailyusage.used_item.add(itemused)
        #     dailyusage.save()
        #     valid_payload = {
        #         "used_item": [],
        #         "comment": "changes"
        #     }
        #     response = self.client.patch(
        #         reverse('inventory_RUD_dailyusage', kwargs={'id': dailyusage.pk}),
        #         data=json.dumps(valid_payload),
        #         content_type='application/json'
        #     )
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        #
        # def test_invalid_update_dailyusage(self):
        #     """ Update single valid item. """
        #     dailyusage = sample_dailyusage()
        #     itemused = sample_itemused()
        #     dailyusage.used_item.add(itemused)
        #     dailyusage.save()
        #     invalid_payload = {
        #         "used_item": [],
        #         "comment": ""
        #     }
        #     response = self.client.put(
        #         reverse('inventory_RUD_dailyusage', kwargs={'id': dailyusage.pk}),
        #         data=json.dumps(invalid_payload),
        #         content_type='application/json')
        #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)