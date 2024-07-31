from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [

    {
        "id": 1,
        "Título": "O Menino que Taxava Livros",
        "Autor": "Marcus Taxa",
        "Preço R$": 82.00,
    },

    {
        "id": 2,
        "Título": "O Senhor dos Impostos - A Sociedade da Taxação",
        "Autor": "J.R.R Taxien",
        "Preço R$": 48.00,
    },

    {
        "id": 3,
        "Título": "Taxaman - O Imposto Mortal",
        "Autor": "Alan Taaxore",
        "Preço R$": 60.00,
    },

    {
        "id": 4,
        "Título": "A Divina Taxa - O Imposto de Dante",
        "Autor": "Dante Taxhieri",
        "Preço R$": 18.00,
    },

    {
        "id": 5,
        "Título": "Sun Taxu - A Arte do Imposto: Edição de Luxo",
        "Autor": "Sun Taxu",
        "Preço: R$": 67.50,
    },

    {
        "id": 6,
        "Título": "Caverna dos Impostos 5ª edição - Livro do Taxador",
        "Autor": "Gary Taxax",
        "Preço: R$": 67.50,
    },

    {
        "id": 7,
        "Título": "O Chamado do Imposto",
        "Autor": "H.P. Taxacraft ",
        "Preço: R$": 90.00,
    },
]

@app.route('/livros', methods=['GET'])
def consultar_livros():
    return jsonify(livros)

@app.route('/livros', methods=['GET'])
def consultar_livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro_por_id(id):
    livro_atualizado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_atualizado)
            return jsonify(livros[indice])

@app.route('/livros/<int:id>', methods=['DELETE'])
def remover_livro_por_id(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=8080, host='localhost',debug= True)