from flask import Flask
from routes.colmeia_routes import colmeia_bp

app = Flask(__name__)
app.register_blueprint(colmeia_bp, url_prefix='/colmeias')

@app.route('/')
def index():
    return {'mensagem': 'API de Apicultores funcionando!'}

if __name__ == '__main__':
    app.run(debug=True)

#Borges esteve aqui