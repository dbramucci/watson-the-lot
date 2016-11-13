from flask import Flask, request, url_for
from twilio.rest import TwilioRestClient
from urllib.request import urlopen
from math import radians, sqrt, cos
import data
from PIL import Image
from os import curdir
from functools import reduce
from imageMaker import *
import json
from secretsauce import PHONE_ID, account_sid, auth_token

client = TwilioRestClient(account_sid, auth_token)

EARTH_RADIUS = 6317009  # meters

parking_lot_location = 39.189991, -96.584112

within_range = False

app = Flask(__name__)

parking_lot = [i % 2 == 0 for i in
               range(10)]  # [False for _ in range(10)]  # The parking lot
parking_lot_image = None


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        check_spots()
        table = "<center><table><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></center>".format(
            *('<image src="{}">'.format(
                url_for('static', filename='red.png') if b else url_for(
                    'static', filename='green.png')) for b in parking_lot))
        parking_text = "hi"
        print(reduce(lambda a, b: a + b,
                     map(lambda x: 0 if x else 1, parking_lot)))
        parking_text = "There are {} spots free out of {} spots total".format(
            reduce(lambda a, b: a + b,
                   map(lambda x: 1 if x else 0, parking_lot)), 10)
        dictionary = {k: url_for('static', filename=v) for k, v in
                      data.srcs.items()}
        dictionary['parking_text'] = parking_text
        dictionary['table'] = table
        return data.no_subs_page.format(**dictionary)
    else:
        values = json.loads(request.data.decode("utf-8"))
        return str(values)


@app.route("/about")
def about():
    return "about page"


#
# @app.route("/update", methods=["GET", "POST"])
# def update():
#     if request.method == "POST":


@app.route("/image")
def image():
    # print(curdir)
    with open('C:/Users/Archer/Documents/GitHub/watson-the-lot/server/hi.txt',
              mode="w") as f:
        f.write("Hello World")
        print("hi")
    return url_for('static', filename='index_480.png')


def calc_dist(a, b):
    a = tuple(map(radians, a))
    b = tuple(map(radians, b))
    delta_latitude = a[0] - b[0]
    delta_longitude = a[1] - b[1]
    mean_latitude = (a[0] + b[0]) / 2
    return EARTH_RADIUS * sqrt(
        delta_latitude ** 2 + (cos(mean_latitude) * delta_longitude) ** 2)


def send_sms(text: str):
    message = client.messages.create(to="(913) 904-6044", from_="(913) 735-1407",
                                     body=text)


@app.route("/location", methods=["POST"])
def location():
    values = json.loads(request.data.decode("utf-8"))
    if values['id'] == PHONE_ID:
        # print(values)
        print(values['location'])
        print("Coordinates")
        print(float(values['location']['longitude']), ',',
              float(values['location']['latitude']))
        global within_range
        new_location = float(values['location']['longitude']), float(
            values['location']['latitude'])
        if not within_range and calc_dist(new_location, parking_lot_location):
            within_range = True
            if reduce(lambda x, y: x and y, parking_lot):
                send_sms("The lot is full")
            else:
                send_sms("There are {} spots left.".format(reduce(lambda a, b: a + b,
                     map(lambda x: 0 if x else 1, parking_lot))))
            within_range = True
        global location
        location = new_location
        # print(values['latitude'], values['longitude'])
    return ""


@app.route("/reset")
def reset():
    within_range = False
    return ""

@app.route("/update")
def update():
    global parking_lot_image
    parking_lot_image = lot(generate_list_of_parking_spots(0.5))
    return ''


x = None


@app.route("/check")
def check_parking_spots():
    check_spots()
    return ''


def check_spots():
    # pics = split_parking_lot(parking_lot_image)
    car_in_spot = [False for _ in range(10)]
    for i in range(10):
        if i < 10:
            x = urlopen(
                "http://iot-1-hr-practice.mybluemix.net/reco?imageurl={}/static/{}.png".format(
                    'http://159.203.129.227', i)).read()
            print("TEXT\n\n{}\n\n".format(x))
            classifications = json.loads(x.decode())['images'][0]['classifiers']
            for j in classifications:
                for k in j['classes']:
                    object_name = k['class']
                    if object_name == "car" or object_name == "vehicle" or object_name == "truck":
                        print(object_name)
                        car_in_spot[i] = True
                print(j['classes'])
        print(car_in_spot)
    global parking_lot
    parking_lot = car_in_spot


def main():
    app.run()


if __name__ == "__main__":
    app.run()
    # pic = lot(generate_list_of_parking_spots(0.5))
    # pic.save("pic.png")
    # split_parking_lot(pic)
