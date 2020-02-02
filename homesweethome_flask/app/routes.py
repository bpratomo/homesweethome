from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/property_list')
def property_list_from_event_ajax(payload):
    print(payload)