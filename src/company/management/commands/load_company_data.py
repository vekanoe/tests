from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.management import call_command

from company.models import Employee


class Command(BaseCommand):
    help = 'Загрузка тестовых данных'

    DUMP_FILE = 'company/fixtures/datas.json'

    def handle(self, *args, **kwargs):

        if not Employee.objects.exists():
            if Path(self.DUMP_FILE).exists():
                call_command('loaddata', self.DUMP_FILE)
                self.stdout.write(self.style.SUCCESS('Загрузка завершена'))
            else:
                self.stdout.write(self.style.ERROR(f'Файл {self.DUMP_FILE} не найден'))
        else:
            self.stdout.write(self.style.SUCCESS('Загрузка не выполнена, т.к. в базе присутствуют данные'))
