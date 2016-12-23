from django.core.management.base import BaseCommand
from channels import Channel, channel_layers


class Command(BaseCommand):
    
    help = 'Schedule clients scrape to be performed'
    
    def handle(self, *args, **kwargs):
        Channel('background-update-checks').send({'comment': 'from management command'})
        self.stdout.write('scheduled background-update-checks\n')
    