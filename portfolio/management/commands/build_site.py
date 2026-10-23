import shutil
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.test import Client
from django.urls import reverse

PAGES = {
    'portfolio:index': 'index.html',
}


class Command(BaseCommand):
    help = 'Renders the site to static files, for hosting without a server.'

    def add_arguments(self, parser):
        parser.add_argument('output', type=Path, help='Folder to write the site into. It is replaced if it exists.')

    def handle(self, *args, output, **options):
        if settings.DEBUG:
            raise CommandError('Debug mode is on. Set DJANGO_DEBUG to 0 to build the site.')

        call_command('collectstatic', interactive=False, verbosity=0, ignore_patterns=['admin'])

        shutil.rmtree(output, ignore_errors=True)
        output.mkdir(parents=True)
        client = Client(HTTP_HOST='philbenson.name')
        for name, filename in PAGES.items():
            self.save(client, reverse(name), 200, output / filename)
        self.save(client, '/404.html', 404, output / '404.html')
        shutil.copytree(settings.STATIC_ROOT, output / settings.STATIC_URL.strip('/'))

        self.stdout.write(self.style.SUCCESS(f'Built the site in {output}'))

    def save(self, client, url, status, path):
        response = client.get(url)
        if response.status_code != status:
            raise CommandError(f'{url} returned {response.status_code} instead of {status}.')
        path.write_bytes(response.content)
