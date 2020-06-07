# -*- coding: utf-8 -*-
import os
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }}
})

current_path = os.path.dirname(os.path.realpath(__file__))
