from flask import Blueprint, jsonify, request
from services.usuario_service import *

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    usuario = cadastrar_usuario(data)
    return jsonify(vars(usuario)), 201

@usuario_bp.route('/', methods=['GET'])
def get_usuarios():
    return jsonify(listar_usuarios()), 200

@usuario_bp.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = buscar_usuario_por_id(id)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@usuario_bp.route('/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    usuario = atualizar_usuario(id, data)
    if usuario:
        return jsonify(vars(usuario)), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    if deletar_usuario(id):
        return jsonify({"mensagem": "Usuário deletado com sucesso!"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404
