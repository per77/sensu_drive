import django
django.setup()
from isubscribe.tasks import *
#sensu_client_list()
#sensu_check_list()
#sensu_entity_list()
#alert_rules()

message = {'entity': 'us-monitor01.locsec.net:ori-test', 'status': 0, 'output': 'test output'}
alert_handler(message)

