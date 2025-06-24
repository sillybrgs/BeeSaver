from models.apicultor import Apicultor

apicultores = []
proximo_id = 1

def cadastrar_apicultor(data):
    global proximo_id
    novo = Apicultor(proximo_id, data['nome'], data['experiencia_anos'], data['regiao'])
    apicultores.append(novo)
    proximo_id += 1
    return novo

def listar_apicultores():
    return [vars(a) for a in apicultores]

def buscar_apicultor_por_id(id):
    for a in apicultores:
        if a.id == id:
            return vars(a)
    return None

def atualizar_apicultor(id, data):
    for a in apicultores:
        if a.id == id:
            a.nome = data.get('nome', a.nome)
            a.experiencia_anos = data.get('experiencia_anos', a.experiencia_anos)
            a.regiao = data.get('regiao', a.regiao)
            return a
    return None

def deletar_apicultor(id):
    for a in apicultores:
        if a.id == id:
            apicultores.remove(a)
            return True
    return False
