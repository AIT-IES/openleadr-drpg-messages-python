import openleadr
from jinja2 import Environment, PackageLoader

TEMPLATES_DRPG = Environment(loader=PackageLoader('openleadr_drpg_messages', 'templates'))
TEMPLATES_DRPG.filters['datetimeformat'] = openleadr.utils.datetimeformat
TEMPLATES_DRPG.filters['timedeltaformat'] = openleadr.utils.timedeltaformat
TEMPLATES_DRPG.filters['booleanformat'] = openleadr.utils.booleanformat
TEMPLATES_DRPG.trim_blocks = True
TEMPLATES_DRPG.lstrip_blocks = True

MEASUREMENT_NAMESPACES_DRPG = {
    'currency': 'ns3',
    'currencyPerWK': 'ns3',
    'currencyPerKWh': 'ns3',
    'currencyPerThm': 'ns3',
    'current': 'ns3',
    'energyApparent': 'ns6',
    'energyReactive': 'ns6',
    'energyReal': 'ns6',
    'frequency': 'ns3',
    'powerApparent': 'ns6',
    'powerReactive': 'ns6',
    'powerReal': 'ns6',
    'pulseCount': 'ns3',
    'temperature': 'ns3',
    'Therm': 'ns3',
    'voltage': 'ns6',
    'customUnit': 'ns3'
    }

def enable():
    '''
    Apply changes to use package openleadr with the message templates defined in this package.
    '''
    openleadr.messaging.TEMPLATES = TEMPLATES_DRPG
    openleadr.enums._MEASUREMENT_NAMESPACES = MEASUREMENT_NAMESPACES_DRPG
