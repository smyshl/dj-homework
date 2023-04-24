import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            item = Phone(id=int(phone['id']), name=phone['name'], image=phone['image'], price=float(phone['price']),
                         release_date=phone['release_date'])
            if phone['lte_exists'] == 'True':
                item.lte_exists = 1
            else:
                item.lte_exists = 0
            item.slug = slugify(item.name)
            item.save()
            # pass
