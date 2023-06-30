from datetime import datetime

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {
                'name': 'Yota',
                'description': 'russian phone',
                'photo': '',
                'category': 'Phones',
                'price': '14',
                'release_date': datetime.now(),
                'last_change_date': datetime.now()
            },
            {
                'name': 'Asus M2',
                'description': 'Phones',
                'photo': '',
                'category': 'Phones',
                'price': '53',
                'release_date': datetime.now(),
                'last_change_date': datetime.now()
            },
            {
                'name': 'Xiaomi Mi2',
                'description': 'phones',
                'photo': '',
                'category': 'Phones',
                'price': '43',
                'release_date': datetime.now(),
                'last_change_date': datetime.now()
            }
        ]

        products_for_add = []
        for product in product_list:
            products_for_add.append(Product(**product))

        Product.objects.bulk_create(products_for_add)
