from flask import Flask, render_template, request
import requests
import helpers
import json

from flask.cli import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["GET"])
def result():

    in_wales = None
    uprn = request.args.get("uprn")
    valid_uprn = helpers.validate_uprn(uprn)

    if valid_uprn:
        response = requests.post(
            "https://land-property-platform.herokuapp.com/is_it_in_wales",
            data=json.dumps({"uprn": uprn}),
        )
        data = response.json()
        in_wales = data.get("in_wales", None)

    if in_wales == None:
        raise Exception("Unhandled exception")

    return render_template(
        "result.html", uprn=uprn, valid_uprn=valid_uprn, in_wales=in_wales
    )
