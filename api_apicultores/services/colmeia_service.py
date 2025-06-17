from models.colmeia import Colmeia

colmeias = []
proximo_id = 1

def cadastrar_colmeia(data):
    global proximo_id
    nova = Colmeia(proximo_id, data['nome'], data['localizacao'], data.get('saude', 'Boa'))
    colmeias.append(nova)
    proximo_id += 1
    return nova

def listar_colmeias():
    return [vars(c) for c in colmeias]

def buscar_colmeia_por_id(id):
    for c in colmeias:
        if c.id == id:
            return vars(c)
    return None

def avaliar_colmeia(id, nova_saude):
    for c in colmeias:
        if c.id == id:
            c.saude = nova_saude
            return c
    return None

def atualizar_colmeia(id, data):
    for c in colmeias:
        if c.id == id:
            c.nome = data.get('nome', c.nome)
            c.localizacao = data.get('localizacao', c.localizacao)
            c.saude = data.get('saude', c.saude)
            return c
    return None

def deletar_colmeia(id):
    for c in colmeias:
        if c.id == id:
            colmeias.remove(c)
            return True
    return False
