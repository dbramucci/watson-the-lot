from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "<b> hi </b> <a href=\"/about\"> about </a>"
    else:
        values = json.loads(request.data.decode("utf-8"))
        print(sum(values))
        sum_dict = {
      'd':{
        "temp" : sum(values),
        "humidity" : 42,
        "location" :
        {
          "longitude" : 43,
          "latitude" : 41
        },
      }}
        return json.dumps(sum_dict)


@app.route("/about")
def about():
    return "about page"


if __name__ == "__main__":
    app.run()
