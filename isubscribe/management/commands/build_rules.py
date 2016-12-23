from django.core.management.base import BaseCommand
from channels import Channel, channel_layers


class Command(BaseCommand):
    
    help = 'Schedule alert rules building'
    
    def handle(self, *args, **kwargs):
        Channel('background-build-rules').send({'comment': 'from management command'})
        self.stdout.write('scheduled background-update-entities\n')
    