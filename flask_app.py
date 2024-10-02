from flask import Flask, request, jsonify, redirect, url_for, abort, make_response

app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Hello World!"

# Rota dinâmica com nome de usuário
@app.route('/user/<name>')
def user(name):
    if name.lower() == "leticia yukari":  # Verifica se o nome é "Leticia Yukari"
        return "Hello, Leticia Yukari!"  # Resposta personalizada
    return f"Hello, {name}!"  # Para outros nomes

# Rota para mostrar o contexto da requisição
@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')  # Obtém o user-agent da requisição
    return f"Your browser is: {user_agent}"

# Rota que retorna um código de status diferente
@app.route('/codigostatusdiferente')
def codigostatus_diferente():
    return "404 - Page not found", 404  # Mensagem de erro mais clara

# Rota que retorna um objeto de resposta JSON
@app.route('/objetoresposta')
def objeto_resposta():
    response = jsonify(message="This document carries a cookie!", status="success")  # Corrigido "sucesso" para "success"
    response.status_code = 200
    response.headers['Custom-Header'] = 'Valor do Cabeçalho'
    return response

# Rota para redirecionar a um site externo (exemplo: google.com)
@app.route('/redirecionamento')
def redirecionamento():
    return redirect("https://ptb.ifsp.edu.br/")  # Site desejado

# Rota para abortar a requisição com uma mensagem personalizada de Not Found
@app.route('/abortar')
def abortar():
    return make_response("404 - Not Found. Please check the URL.", 404)  # Mensagem breve

# Remova a linha abaixo antes de implantar na produção
# if __name__ == '__main__':
#     app.run(debug=True)  # Removido para produção

