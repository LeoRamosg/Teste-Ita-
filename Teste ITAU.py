from flask import Flask, jsonify, request 

app = Flask(__name__)

Pessoas = [
    {
        'id': 1,
        'Nome completo': 'Leonardo Ramos Gonçalves',
        'Data de nacimento': '14/04/1999',
        'Endereco': 'Rua das Laranjas, 204, Fazenda Marajoara',
        'CPF': '490.579.508-22',
        'Estado civil': 'Solteiro'
    },
    {
        'id': 2,
        'Nome completo': 'Beatriz Policastro de Oliveira',
        'Data de nacimento': '14/11/2003',
        'Endereco': 'Rua Benedito de Paula Cordeiro, 120, Jardim California',
        'CPF': '485.925.238-18',
        'Estado civil': 'Solteiro'
    },
]

# Consultar (todos)
@app.route('/Pessoas',methods=['GET'])
def obter_pessoas():
    return jsonify(Pessoas)

# Consultar (id)
@app.route('/Pessoas/<int:id>',methods=['GET'])
def obter_pessoas_por_id(id):
    for Pessoa in Pessoas:
       if Pessoa.get('id') == id:
           return jsonify(Pessoa)
# Editar 
@app.route('/Pessoas/<int:id>', methods=['PUT'])
def editar_Pessoas_por_id(id):
        Pessoa_alterada = request.get_json()
        for indice,Pessoa in enumerate(Pessoas):
             print(Pessoa)
             if Pessoa.get('id') == id:
                Pessoas[indice].update(Pessoa_alterada)
                return jsonify(Pessoas[indice])
# Criar
@app.route('/Pessoas', methods=['POST'])
def incluir_nova_Pessoa():
    nova_Pessoa = request.get_json()
    Pessoas.append(nova_Pessoa)

    return jsonify(Pessoas)

# Excluir
@app.route('/Pessoas/<int:id>', methods=['DELETE'])
def excluir_pessoa(id):
     for indice, Pessoa in enumerate(Pessoas):
         if Pessoa.get('id') == id:
             del Pessoas[indice]

     return jsonify(Pessoas)
app.run(port=5000,host='localhost',debug=True)
