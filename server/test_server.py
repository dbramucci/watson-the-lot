from flask import Flask, request, url_for
from urllib.request import urlopen
from PIL import Image
from os import curdir
from imageMaker import *
import json
from secretsauce import PHONE_ID

app = Flask(__name__)

parking_lot = [False for _ in range(10)]  # The parking lot
parking_lot_image = None


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return "<b> hi </b> <a href=\"/about\"> about </a>"
    else:
        values = json.loads(request.data.decode("utf-8"))
        return "nothing"


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


@app.route("/location", methods=["POST"])
def location():
    values = json.loads(request.data.decode("utf-8"))
    if values['id'] == PHONE_ID:
        # print(values)
        print(values['location'])
        print("Coordinates")
        print(float(values['location']['longitude']), ',',
              float(values['location']['latitude']))
        # print(values['latitude'], values['longitude'])
    return ""

@app.route("/update")
def update():
    global parking_lot_image
    parking_lot_image = lot(generate_list_of_parking_spots(0.5))
    return ''

x = None

@app.route("/check")
def check_parking_spots():
    pics = split_parking_lot(parking_lot_image)
    car_in_spot = []
    for i, p in enumerate(pics):
        p.save("C:/Users/Archer/Documents/GitHub/watson-the-lot/server/static/{}.png".format(i))
        if i < 1:
            urlopen("http://iot-1-hr-practice.mybluemix.net/reco?imageurl={}/static/{}.png".format('http://d02e424d.ngrok.io', i))
    return ''




def main():
    app.run()


if __name__ == "__main__":
    app.run()
    # pic = lot(generate_list_of_parking_spots(0.5))
    # pic.save("pic.png")
    # split_parking_lot(pic)
