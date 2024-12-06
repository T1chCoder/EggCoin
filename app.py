from flask import Flask, render_template as render

app = Flask(__name__)

import config, views, urls