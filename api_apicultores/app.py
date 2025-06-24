from flask import Flask
from routes.colmeia_routes import colmeia_bp
from routes.usuario_routes import usuario_bp
from routes.apicultor_routes import apicultor_bp

app = Flask(__name__)

# Registrar os blueprints
app.register_blueprint(colmeia_bp, url_prefix='/colmeias')
app.register_blueprint(usuario_bp, url_prefix='/usuarios')
app.register_blueprint(apicultor_bp, url_prefix='/apicultores')

@app.route('/')
def index():
    return {'mensagem': 'API de Apicultores funcionando!'}

if __name__ == '__main__':
    app.run(debug=True)
