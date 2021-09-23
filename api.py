from re import M
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import database

app = Flask(__name__) 
CORS(app)
api = Api(app)


def deserialize(file):
    f = open(file)
    data = json.load(f)
    return data

def find_account(uid):
    account = database.retreive_record(uid)
    return account

class User(Resource):
    def get(self):
        return deserialize('users.json')

class Account(Resource):
    def get(self):
        try:
            args = request.args
            uid = args['uid']
            result = find_account(uid)
            return jsonify(result)
        except Exception as e:
            error = deserialize('errors.json')
            return error[0] 

class All(Resource):
    def get(self):
        data = database.retreive_all()
        key = "name"
        my_dict = {}
        result = []
        for i in range(len(data)):
            my_dict.update({key: data[i][key]})
            result.append(my_dict)
            my_dict = {}

        return result

api.add_resource(User, '/users')
api.add_resource(Account, '/accounts')
api.add_resource(All, '/all')

if __name__ == '__main__':
    app.run(host="0.0.0.0")