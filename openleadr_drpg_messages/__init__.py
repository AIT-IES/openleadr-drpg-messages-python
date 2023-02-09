import openleadr
from jinja2 import Environment, PackageLoader

def enable():
    TEMPLATES = Environment(loader=PackageLoader('openleadr_drpg_messages', 'templates'))
    TEMPLATES.filters['datetimeformat'] = openleadr.utils.datetimeformat
    TEMPLATES.filters['timedeltaformat'] = openleadr.utils.timedeltaformat
    TEMPLATES.filters['booleanformat'] = openleadr.utils.booleanformat
    TEMPLATES.trim_blocks = True
    TEMPLATES.lstrip_blocks = True
    openleadr.messaging.TEMPLATES = TEMPLATES

    openleadr.enums._MEASUREMENT_NAMESPACES = {
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
