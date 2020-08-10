from flask import Flask, request, session
from flask_restful import Resource, Api
import pickle
import random
import Funky
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "HALLO"
api = Api(app)
app.permanent_session_lifetime = timedelta(minutes=5)


class Calculator(Resource):
    def get(self):
        if "user" in session:
            user = session['user']
            with open('{}\{}'.format('keys', user), 'rb') as fp:
                info = pickle.load(fp)

            result = Funky.calculate(info)
            if result.isnumeric():
                info += ' @ DONE @ '
                with open('{}\{}'.format('keys', user), 'wb') as fp:
                    pickle.dump(info, fp)
            else:
                with open('{}\{}'.format('keys', user), 'wb') as fp:
                    pickle.dump('', fp)
            return result
        else:
            return 'You Did Not POST Anything or Your Session Expired.'

    def post(self):
        if "user" in session:
            user = session["user"]
            with open('{}\{}'.format('keys', user), 'rb') as fp:
                info = pickle.load(fp)
            if '@ DONE @' in info:
                info = ''
            info += request.get_data(as_text=True) + '\n'
            if len(info) < 1000:
                with open('{}\{}'.format('keys', user), 'wb') as fp:
                    pickle.dump(info, fp)
            else:
                return 'Too large POST'
        else:
            session["user"] = random.random()
            user = session['user']
            info = request.get_data(as_text=True) + ' @ '
            if len(info) < 1000:
                with open('{}\{}'.format('keys', user), 'wb') as fp:
                    pickle.dump(info, fp)
            else:
                return 'Too large POST'
        return 'OK'


api.add_resource(Calculator, '/')

if __name__ == '__main__':
    app.run()
