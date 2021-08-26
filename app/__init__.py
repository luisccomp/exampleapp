from flask import Flask

from app.extensions import register_extensions
from app.settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)

register_extensions(app)

from app.models.entities import *
