from flask import Blueprint, jsonify, request
from services.apicultor_service import *

apicultor_bp = Blueprint('apicultor', __name__)

@apicultor_bp.route('/', methods=['POST'])
def criar_apicultor():
    data = request.get_json()
    apicultor = cadastrar_apicultor(data)
    return jsonify(vars(apicultor)), 201

@apicultor_bp.route('/', methods=['GET'])
def get_apicultores():
    return jsonify(listar_apicultores()), 200

@apicultor_bp.route('/<int:id>', methods=['GET'])
def get_apicultor(id):
    apicultor = buscar_apicultor_por_id(id)
    if apicultor:
        return jsonify(apicultor), 200
    return jsonify({"error": "Apicultor não encontrado"}), 404

@apicultor_bp.route('/<int:id>', methods=['PUT'])
def update_apicultor(id):
    data = request.get_json()
    apicultor = atualizar_apicultor(id, data)
    if apicultor:
        return jsonify(vars(apicultor)), 200
    return jsonify({"error": "Apicultor não encontrado"}), 404

@apicultor_bp.route('/<int:id>', methods=['DELETE'])
def delete_apicultor(id):
    if deletar_apicultor(id):
        return jsonify({"mensagem": "Apicultor deletado com sucesso!"}), 200
    return jsonify({"error": "Apicultor não encontrado"}), 404
