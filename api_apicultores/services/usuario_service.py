from models.usuario import Usuario

usuarios = []
proximo_id = 1

def cadastrar_usuario(data):
    global proximo_id
    novo = Usuario(proximo_id, data['nome'], data['email'])
    usuarios.append(novo)
    proximo_id += 1
    return novo

def listar_usuarios():
    return [vars(u) for u in usuarios]

def buscar_usuario_por_id(id):
    for u in usuarios:
        if u.id == id:
            return vars(u)
    return None

def atualizar_usuario(id, data):
    for u in usuarios:
        if u.id == id:
            u.nome = data.get('nome', u.nome)
            u.email = data.get('email', u.email)
            return u
    return None

def deletar_usuario(id):
    for u in usuarios:
        if u.id == id:
            usuarios.remove(u)
            return True
    return False
