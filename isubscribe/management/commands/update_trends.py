from django.core.management.base import BaseCommand
from channels import Channel, channel_layers


class Command(BaseCommand):
    
    help = 'Schedule trends buildup to be performed'
    
    def handle(self, *args, **kwargs):
        Channel('background-update-trends').send({'comment': 'from management command'})
        self.stdout.write('scheduled background-update-trends\n')
    