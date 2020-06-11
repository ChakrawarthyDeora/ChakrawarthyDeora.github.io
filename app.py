from flask import Flask,render_template,request
from pyowm.owm import OWM

app= Flask(__name__)


owm=OWM('be68f88b8fbed89f9f51fbe6ada45db8')


@app.route("/")
def info():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def info_post():
    degree=u"\u00B0"
    location=request.form.get('location')
    mgr=owm.weather_manager()
    observation=mgr.weather_at_place(location)
    weather=observation.weather
    temp_dict_celsius=weather.temperature('celsius')['temp']
    return f"The Temperature in {location} is {temp_dict_celsius} {degree} celsius or {(temp_dict_celsius * 9/5)+32} {degree} fahrenheit"
