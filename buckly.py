#!/usr/bin/env python


import logging

from brubeck.request_handling import Brubeck
from brubeck.templating import load_jinja2_env

from handlers import (ShortenLinkHandler,
                      LinkExpansionHandler,
                      APILinkExpansionHandler)

from queries import init_db_conn


###
### Configuration
###


# Instantiate database connection
db_conn = init_db_conn()


# Routing config
handler_tuples = [
    (r'^/api', APILinkExpansionHandler),
    (r'^/(?P<short_id>\w+)', LinkExpansionHandler),
    (r'^/$', ShortenLinkHandler),
]


# Application config
config = {
    'mongrel2_pair': ('tcp://127.0.0.1:9999', 'tcp://127.0.0.1:9998'),
    'handler_tuples': handler_tuples,
    'template_loader': load_jinja2_env('./templates'),
    'db_conn': db_conn,
    'log_level': logging.DEBUG,
}


# Instantiate app instance
app = Brubeck(**config)
app.run()
