from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext, audio

import json

__version__ = '0.3.0'
logger = logging.getLogger(__name__)

class Extension(ext.Extension):

    dist_name = 'Mopidy-Jingle'
    ext_name = 'jingle'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['media_dir'] = config.String()
        schema['every_x'] = config.Integer()
        return schema
    
    def setup(self, registry):
        from .backend import JingleBackend
        registry.add('backend', JingleBackend)



