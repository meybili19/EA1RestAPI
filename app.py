from flask import Flask, jsonify, send_from_directory
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

# Configuración de Swagger
SWAGGER_URL = "/api-docs"
API_DOCS = "/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_DOCS, config={"app_name": "Hello world from REST API with Python"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Servir swagger.json
@app.route('/swagger.json')
def swagger_file():
    return send_from_directory('.', 'swagger.json')

# Endpoint principal
class HelloWorld(Resource):
    def get(self):
        return jsonify({"message": "Hello world from REST API with Python"})

# Registrar el recurso en la API
api.add_resource(HelloWorld, "/hello")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

