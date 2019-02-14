from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GenerateSolution(Resource):
    def solver(self):
        return {'hello': 'world'}

api.add_resource(GenerateSolution, '/<string:problem_string>')

if __name__ == '__main__':
    app.run(debug=True) 