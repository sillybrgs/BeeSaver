from flask import Flask, jsonify, request
from routes.colmeia_routes import colmeia_bp

app = Flask(__name__)
app.register_blueprint(colmeia_bp, url_prefix='/colmeias')

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

#Borges esteve aqui