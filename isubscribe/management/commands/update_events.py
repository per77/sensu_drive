from django.core.management.base import BaseCommand
from channels import Channel, channel_layers


class Command(BaseCommand):
    
    help = 'Schedule events scrape to be performed'
    
    def handle(self, *args, **kwargs):
        Channel('background-update-events').send({'comment': 'from management command'})
        self.stdout.write('scheduled background-update-events\n')
    