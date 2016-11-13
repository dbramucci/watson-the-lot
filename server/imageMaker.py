from PIL import Image
from random import random
from flask import url_for


def generate_list_of_parking_spots(probability: float) -> list:
    return [random() > probability for _ in range(10)]


def lot(spots_taken: list) -> Image:
    carIm = Image.open('C:/Users/Archer/Documents/GitHub/watson-the-lot/server/static/red_car.png') #url_for('static', filename='red_car.png'))
    parking_lotIm = Image.open('C:/Users/Archer/Documents/GitHub/watson-the-lot/server/static/parking_lot.png')#url_for('static', filename='parking_lot.png'))
    carIm = carIm.resize((70, 140))
    parking_copy = parking_lotIm.copy()
    for i, b in enumerate(spots_taken):
        if b:
            parking_copy.paste(carIm, (75 + 100 * (i % 5), 50 + 160 * (i // 5)),
                               carIm)
    return parking_copy


def split_parking_lot(parking_lot_pic: Image) -> list:
    pics = []
    for i in range(10):
        x_1 = 55 + 100 * (i % 5)
        y_1 = 50 + 160 * (i // 5)
        x_2 = x_1 + 100
        y_2 = y_1 + 150
        pic_i = parking_lot_pic.crop((x_1, y_1, x_2, y_2))
        pics.append(pic_i)
    return pics
