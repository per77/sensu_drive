from django.core.management.base import BaseCommand
from channels import Channel, channel_layers


class Command(BaseCommand):
    
    help = 'Schedule entities scrape to be performed'
    
    def handle(self, *args, **kwargs):
        Channel('background-update-entities').send({'comment': 'from management command'})
        self.stdout.write('scheduled background-update-entities\n')
    