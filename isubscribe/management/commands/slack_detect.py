from django.core.management.base import BaseCommand
from channels import Channel, channel_layers


class Command(BaseCommand):
    
    help = 'Schedule slack users detection'
    
    def handle(self, *args, **kwargs):
        Channel('background-slack-detect').send({'comment': 'from management command'})
        self.stdout.write('scheduled background-slack-detect\n')
    