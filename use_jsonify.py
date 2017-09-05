# coding:utf-8
import json
from flask import jsonify,Flask
from flask import Response


app=Flask(__name__)

@app.route("/json/",methods=["GET"])
def get_json():
    person={
        "name":"二蛋",
        "age":10,
        "wife":None,
        "has_child":True,
        "has_car":False
    }
    return jsonify(person=person)

@app.route("/json2/",methods=["GET"])
def get_json2():
    person={
        "name":"二蛋",
        "age":10,
        "wife":None,
        "has_child":True,
        "has_car":False
    }
    format=json.dumps(person,ensure_ascii=False)
    return Response(
        response=format,
        mimetype="application/json",
        status=200
    )

app.run(host='0.0.0.0')
