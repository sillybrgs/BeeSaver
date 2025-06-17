from flask import Blueprint, jsonify, request
from services.colmeia_service import (
    cadastrar_colmeia, listar_colmeias, avaliar_colmeia,
    buscar_colmeia_por_id, atualizar_colmeia, deletar_colmeia
)

colmeia_bp = Blueprint('colmeia', __name__)

@colmeia_bp.route('/', methods=['POST'])
def criar_colmeia():
    data = request.get_json()
    colmeia = cadastrar_colmeia(data)
    return jsonify(vars(colmeia)), 201

@colmeia_bp.route('/', methods=['GET'])
def get_colmeias():
    return jsonify(listar_colmeias()), 200

@colmeia_bp.route('/<int:id>', methods=['GET'])
def get_colmeia(id):
    colmeia = buscar_colmeia_por_id(id)
    if colmeia:
        return jsonify(colmeia), 200
    return jsonify({"error": "Colmeia não encontrada"}), 404

@colmeia_bp.route('/<int:id>/avaliar', methods=['PUT'])
def avaliar(id):
    data = request.get_json()
    nova = avaliar_colmeia(id, data.get('saude'))
    if nova:
        return jsonify(vars(nova)), 200
    return jsonify({"error": "Colmeia não encontrada"}), 404

@colmeia_bp.route('/<int:id>', methods=['PUT'])
def update_colmeia(id):
    data = request.get_json()
    colmeia = atualizar_colmeia(id, data)
    if colmeia:
        return jsonify(vars(colmeia)), 200
    return jsonify({"error": "Colmeia não encontrada"}), 404

@colmeia_bp.route('/<int:id>', methods=['DELETE'])
def delete_colmeia(id):
    if deletar_colmeia(id):
        return jsonify({"mensagem": "Colmeia deletada com sucesso!"}), 200
    return jsonify({"error": "Colmeia não encontrada"}), 404
