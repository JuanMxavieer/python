from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/decorator') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Explicação sobre Decorators</title>
</head>
<body>
    <h1>Em Python, um decorator é uma função que “envolve” outra função para adicionar um comportamento extra sem precisar alterar o código original dela.</h1>
    <p>A ideia principal é:</p>
    <ul>
        <li>pegar uma função</li>
        <li>modificar ou expandir o comportamento dela</li>
        <li>devolver uma nova função</li>
    </ul>
    <p>O símbolo usado é <code>@</code>.</p>
    <hr>
    <h2>Exemplo simples</h2>
    <pre>
def meu_decorator(funcao):
    def wrapper():
        print("Antes da função")
        
        funcao()
        
        print("Depois da função")
    
    return wrapper


@meu_decorator
def ola():
    print("Olá!")


ola()
    </pre>
    <p><strong>Saída:</strong></p>
    <pre>
Antes da função
Olá!
Depois da função
    </pre>
    <hr>
    <h2>O que aconteceu?</h2>
    <p>Quando você escreve:</p>
    <pre>
@meu_decorator
def ola():
    </pre>
    <p>O Python faz isso internamente:</p>
    <pre>
ola = meu_decorator(ola)
    </pre>
    <p>Ou seja:</p>
    <ul>
        <li><code>ola</code> é enviada para o decorator</li>
        <li>o decorator cria uma nova função</li>
        <li>essa nova função substitui a original</li>
    </ul>
    <hr>
    <h2>Para que decorators servem?</h2>
    <p>Eles são muito usados para:</p>
    <ul>
        <li>autenticação</li>
        <li>logs</li>
        <li>validação</li>
        <li>controle de acesso</li>
        <li>cache</li>
        <li>medir tempo de execução</li>
        <li>rotas web</li>
        <li>tratamento automático</li>
    </ul>
    <hr>
    <h2>Como o Flask usa decorators?</h2>
    <p>No Flask, decorators são usados principalmente para registrar rotas.</p>
    <p><strong>Exemplo:</strong></p>
    <pre>
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Página inicial"
    </pre>
    <hr>
    <h2>O que o <code>@app.route("/")</code> faz?</h2>
    <p>Esse decorator diz ao Flask:</p>
    <blockquote>“Quando alguém acessar /, execute a função home().”</blockquote>
    <p>Internamente é parecido com:</p>
    <pre>
home = app.route("/")(home)
    </pre>
    <p>O Flask pega a função e salva ela como responsável por aquela URL.</p>
    <hr>
    <h2>Fluxo real</h2>
    <p>Quando o navegador acessa:</p>
    <pre>http://localhost:5000/</pre>
    <p>O Flask:</p>
    <ol>
        <li>procura qual função está ligada à rota /</li>
        <li>encontra <code>home</code></li>
        <li>executa a função</li>
        <li>envia o retorno ao navegador</li>
    </ol>
    <hr>
    <h2>Outro exemplo com rota</h2>
    <pre>
@app.route("/sobre")
def sobre():
    return "Página sobre"
    </pre>
    <p>Agora:</p>
    <ul>
        <li><code>/</code> → executa <code>home()</code></li>
        <li><code>/sobre</code> → executa <code>sobre()</code></li>
    </ul>
    <hr>
    <h2>Decorator com métodos HTTP</h2>
    <p>Você também pode configurar métodos:</p>
    <pre>
@app.route("/login", methods=["GET", "POST"])
def login():
    return "Tela de login"
    </pre>
    <p>Aqui o decorator registra:</p>
    <ul>
        <li>URL</li>
        <li>métodos permitidos</li>
        <li>função responsável</li>
    </ul>
    <hr>
    <h2>Exemplo de decorator próprio no Flask</h2>
    <p>Muito usado para autenticação:</p>
    <pre>
from functools import wraps

def login_obrigatorio(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        logado = True

        if not logado:
            return "Acesso negado"

        return funcao(*args, **kwargs)

    return wrapper

@app.route("/painel")
@login_obrigatorio
def painel():
    return "Painel do usuário"
    </pre>
    <p><strong>Fluxo:</strong></p>
    <ol>
        <li>usuário acessa <code>/painel</code></li>
        <li>decorator verifica login</li>
        <li>se estiver logado: executa <code>painel()</code></li>
        <li>senão: bloqueia acesso</li>
    </ol>
    <hr>
    <h2>Resumindo</h2>
    <p>Decorator em Python:</p>
    <ul>
        <li>é uma função que modifica outra função</li>
        <li>usa <code>@</code></li>
        <li>adiciona comportamentos extras</li>
        <li>evita repetir código</li>
    </ul>
    <p>No Flask:</p>
    <ul>
        <li><code>@app.route()</code> conecta URLs às funções</li>
        <li>outros decorators fazem autenticação, permissões, cache etc.</li>
    </ul>
</body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
