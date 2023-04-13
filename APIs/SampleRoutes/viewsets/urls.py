from APIs.SampleRoutes import sample_routes
from flask import request, jsonify



@sample_routes.route('/', methods=['GET', "POST"])
def func():
    if request.method == 'GET':
        pass
    if request.method == "POST":
        pass
    return jsonify({"data": "data"})