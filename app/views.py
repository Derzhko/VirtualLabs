from flask import render_template
from app import app

#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_servo+')
def background_process_servo_plus():
    print ("серво+")
    return ("nothing")

@app.route('/background_process_servo-')
def background_process_servo_minus():
    print ("серво-")
    return ("nothing")

@app.route('/background_process_generator')
def background_process_generator():
    print ("генератор")
    return ("nothing")
