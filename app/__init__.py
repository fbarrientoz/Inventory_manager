#!/usr/bin/env python3
# -*- coding: utf8 -*-
""""""
# """  """

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "MYSUPERSECRETSTRING"

from app import routes