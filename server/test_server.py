from flask import Flask, request, url_for
from urllib.request import urlopen
import data
from PIL import Image
from os import curdir
from functools import reduce
from imageMaker import *
import json
from secretsauce import PHONE_ID

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
        print(reduce(lambda a, b: a+b, map(lambda x: 0 if x else 1, parking_lot)))
        parking_text = "There are {} spots free out of {} spots total".format(
            reduce(lambda a, b: a+b, map(lambda x: 1 if x else 0, parking_lot)), 10)
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
