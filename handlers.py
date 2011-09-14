import sys
import time
import logging
import pymongo
import json

from brubeck.models import User
from brubeck.auth import web_authenticated, UserHandlingMixin
from brubeck.request_handling import WebMessageHandler
from brubeck.templating import Jinja2Rendering

from models import ShortLink
from queries import (gen_next_shortid,
                     load_shortlink,
                     save_shortlink)

from shorten import BaseConverter
shortener = BaseConverter()

class BaseHandler(WebMessageHandler):
    """We don't have to override anything for this simple example!
    """
    

###
### Application Handlers
###

### Web Handlers

class ShortenLinkHandler(BaseHandler, Jinja2Rendering):
    def get(self):
        """Renders a template with a form for submitting a link
        """
        return self.render_template('links/shorten_link.html')

    def post(self):
        """Accepts inputs from get() and reports success or error for link
        shortening request.
        """
        url = self.get_argument('url', None) # default to None

        if not url.startswith('http'):
            url = 'http://%s' % (url)
        
        id_counter = gen_next_shortid(self.db_conn)
        short_id = shortener.from_decimal(id_counter)
        
        sl = ShortLink(created_at=self.current_time,
                       updated_at=self.current_time,
                       link=url,
                       short_id=short_id)
        
        save_shortlink(self.db_conn, sl)
        context = {'shortlink': 'http://localhost:6767/%s' % short_id}
        
        return self.render_template('links/success.html', **context)


class LinkExpansionHandler(BaseHandler, Jinja2Rendering):
    def get(self, short_id):
        """Renders a template with a form for submitting a link
        """
        short_info = load_shortlink(self.db_conn, short_id)
        if short_info:
            return self.redirect(short_info['link'])
        else:
            return self.render_template('errors.html', **{'error_code': 500})


### API Handler

class APILinkExpansionHandler(BaseHandler):
    def get(self):
        short_id = self.get_argument('short_id', None)
        status_code = 404 # default to not found
        
        short_info = load_shortlink(self.db_conn, short_id)

        if short_info:
            status_code = 200
            url = short_info['link']
        else:
            url = 'Pssshh... NADA!'
        
        data = {
            'url': url,
            'status_code': status_code
        }

        self.set_body(json.dumps(data))
        return self.render(status_code=200)
    
