from flask import Flask, request

app = Flask(__name__)

# Página principal (Home)
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Avaliação contínua: Aula 030</title>
        </head>
        <body>
            <h1>Avaliação contínua: Aula 030</h1>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/identificacao">Identificação</a></li>
                <li><a href="/contexto">Contexto da Requisição</a></li>
            </ul>
        </body>
    </html>
    """

# Página "Identificação"
@app.route('/identificacao')
def identificacao():
    return """
    <html>
        <head>
            <title>Identificação</title>
        </head>
        <body>
            <h1>Avaliação contínua: Aula 030</h1>
            <p>Aluno: Leticia Yukari</p>
            <p>Prontuário: PT302596X</p>
            <p>Instituição: IFSP</p>
            <a href="/">Voltar</a>
        </body>
    </html>
    """

# Página "Contexto da Requisição"
@app.route('/contexto')
def contexto():
    user_agent = request.headers.get('User-Agent')  # Pegando o navegador do cliente
    ip_remoto = request.remote_addr  # Pegando o IP do cliente
    host_aplicacao = request.host  # Pegando o host da aplicação

    return """
    <html>
        <head>
            <title>Contexto da Requisição</title>
        </head>
        <body>
            <h1>Avaliação contínua: Aula 030</h1>
            <p>Seu navegador é: {user_agent}</p>
            <p>O IP do computador remoto é: {ip_remoto}</p>
            <p>O host da aplicação é: {host_aplicacao}</p>
            <a href="/">Voltar</a>
        </body>
    </html>
    """.format(user_agent=user_agent, ip_remoto=ip_remoto, host_aplicacao=host_aplicacao)

if __name__ == '__main__':
    app.run()
