from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        for m in models.get_models():
            s = '%s model has %d object(s).\n' % (m.__name__, m.objects.count())
            self.stdout.write(s)
            self.stderr.write('error: %s' % s)
