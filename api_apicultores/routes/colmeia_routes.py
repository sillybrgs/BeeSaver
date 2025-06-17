from flask import Blueprint, jsonify, request
from services.colmeia_service import cadastrar_colmeia, listar_colmeias, avaliar_colmeia
from models.colmeia import Colmeia

colmeia_bp = Blueprint('colmeia', __name__)

@colmeia_bp.route('/', methods=['POST'])
def criar_colmeia():
    data = request.get_json()
    colmeia = cadastrar_colmeia(data)
    return jsonify(colmeia)
@colmeia_bp.route('/', methods=['GET'])
def get_colmeias():
    colmeias = listar_colmeias()
    return jsonify(colmeias)
@colmeia_bp.route('/<int:id>/avaliar', methods=['PUT'])
def avaliar(id):
    data = request.get.json()
    nova = avaliar_colmeia(id, data.get('saude'))
    if nova is None:
        return jsonify({"error": "Colmeia não encontrada"}), 404
    return jsonify(nova)
@colmeia_bp.route('/<int:id>', methods=['GET'])
def get_colmeia(id):
    colmeias = listar_colmeias()
    for colmeia in colmeias:
        if colmeia.id == id:
            return jsonify(vars(colmeia)), 200
    return jsonify({"error": "Colmeia não encontrada"}), 404
@colmeia_bp.route('/<int:id>', methods=['DELETE'])
def delete_colmeia(id):
    colmeias = listar_colmeias()
    for colmeia in colmeias:
        if colmeia.id == id:
            colmeias.remove(colmeia)
            return jsonify({"message": "Colmeia deletada com sucesso!"}), 200
    return jsonify({"error": "Colmeia não encontrada"}), 404
@colmeia_bp.route('/<int:id>', methods=['PUT'])
def update_colmeia(id):
    data = request.get_json()
    colmeias = listar_colmeias()
    for colmeia in colmeias:
        if colmeia.id == id:
            colmeia.nome = data.get('nome', colmeia.nome)
            colmeia.localizacao = data.get('localizacao', colmeia.localizacao)
            colmeia.saude = data.get('saude', colmeia.saude)
            return jsonify(vars(colmeia)), 200
    return jsonify({"error": "Colmeia não encontrada"}), 404
