
from xdm.plugins import *

class DemoExternalPlugin(MediaType):
	version = "0.2"
	_config = {}
	identifier = 'de.lad1337.demopackage'
	config_meta = {'plugin_desc': 'just a deme plugin that is hosted on github for testing'}
