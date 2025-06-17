from models.colmeia import Colmeia
from flask import jsonify, request

colmeias = []
contador_id = 1

def cadastrar_colmeia(data):
    global contador_id
    nova = Colmeia(
        id=contador_id,
        nome=data.get('nome'),
        localizacao=data.get('localizacao'),
        saude=data.get('saude')
    )
    colmeias.append(nova)
    contador_id += 1
    return jsonify({"message": "Colmeia cadastrada com sucesso!"}), 201

def listar_colmeias():
    return [vars(c) for c in colmeias], 200

def avaliar_colmeia(id, nova_saude):
    for c in colmeias:
        if c.id == id:
            c.saude = nova_saude
            return jsonify({"message": "Saúde da colmeia atualizada com sucesso!"}), 200
        
