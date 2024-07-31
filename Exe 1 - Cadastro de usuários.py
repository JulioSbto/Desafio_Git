from flask import Flask, jsonify, request

app = Flask (__name__)

usuarios = [
    {
        'id': 1,
        'nome': 'Dante Sparda',
        'idade': 49
    },

    {
        'id': 2,
        'nome': 'Vergil Sparda',
        'idade': 49
    },

    {
        'id': 3,
        'nome': 'Mary Ann',
        'idade': 45
    },
]

@app.route ('/usuarios', methods=['GET'])
def consultar_usuarios():
    return jsonify(usuarios)


@app.route('/usuarios/<int:id>', methods=['GET'])
def consultar_usuario_por_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)

@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify (usuarios)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_por_id(id):
    usuario_atualizado = request.get_json()
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            usuarios[indice].update(usuario_atualizado)
            return jsonify(usuarios[indice])

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario_por_id(id):
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]
    return jsonify(usuarios)


app.run(port=8080, host='localhost',debug= True)