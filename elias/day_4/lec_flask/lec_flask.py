from flask import Flask, request
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS
from datetime import datetime, timedelta
import logging
import sys

# Write in file
today = datetime.now()
today = today.strftime('%Y_%m_%d')
filename = '%s.log' % today

DISPLAY_LOG_IN_TERMNINAL = True

logger = logging.getLogger('MyLogger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s (%(funcName)s:%(lineno)d) [%(levelname)s]: %(message)s')

# Print in terminal
if DISPLAY_LOG_IN_TERMNINAL:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

file_handler = logging.FileHandler(filename)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()

@api.route('/rest')
class Rest(Resource):
    def sum(self, params):
        a = params['a']
        b = params['b']

        return {'result': 'fail', 'result': a+b}

    def minus(self, params):
        a = params['a']
        b = params['b']

        return {'result': 'fail', 'result': a-b}

    def multi(self, params):
        a = params['a']
        b = params['b']

        return {'result': 'fail', 'result': a*b}

    def devide(self, params):
        a = params['a']
        b = params['b']

        return {'result': 'fail', 'result': a/b if b != 0 else 0}

    def put(self):
        pass

    def get(self):
        pass

    def post(self):
        try:
            params = request.json.get('params')
            command = params['command']

            if command == 'sum':
                resp = self.sum(params)
            elif command == 'minus':
                resp = self.minus(params)
            elif command == 'multi':
                resp = self.multi(params)
            elif command == 'devide':
                resp = self.devide(params)

            # Not support command
            else:
                resp = {'result': 'fail', 'error': f'{command}는 지원하지 명령어입니다.'}

            return resp


        except Exception as e:
            message = f'--> Exception is {e} (Line: {sys.exc_info()[-1].tb_lineno})'
            logger.error(message)
            return {'result': 'fail', 'error': message}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
