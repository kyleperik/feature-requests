from flask import Flask, request, session, g, redirect, url_for, \
                abort, render_template, flash, json, send_from_directory

from feature_requests.data.models import db

from feature_requests.controllers.home import home
from feature_requests.controllers.feature_request import feature_request

from flask import Flask

import os

# Add .jinja as an autoescaped file type
class AutoEscapeFlask(Flask):
    def select_jinja_autoescape(self, filename):
        return (Flask.select_jinja_autoescape(self, filename)
                or filename.endswith('.jinja'))
    
# create app!
app = AutoEscapeFlask(__name__)
app.config.from_envvar('FEAT_REQS_SETTINGS')

app.register_blueprint(home)
app.register_blueprint(feature_request, url_prefix='/feature_request')

# Pass through any config settings/global stuff for all templates
@app.context_processor
def inject_global():
    return dict(debug = app.debug)

# Initialize Database
db.init_app(app)

