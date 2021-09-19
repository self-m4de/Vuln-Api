from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import database

app = Flask(__name__) 
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

api.add_resource(User, '/users')
api.add_resource(Account, '/accounts')

if __name__ == '__main__':
    app.run(host="0.0.0.0")