from flask import Flask

app = Flask(__name__)

@app.route("/curriculo")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo</title>
    </head>
    <body>
        <h1>Currículo</h1>
        <h2>Dados Pessoais</h2>
        <p><strong>Nome:</strong> Juan Marco</p>
        <p><strong>Email:</strong> juanmxavieer@gmail.com</p>
        <p><strong>Telefone:</strong> (31) 97171-3106</p>
        
        <h2>Formação</h2>
        <ul>
            <li>Ensino fundamental - Escola Dona Clara</li>
            <li>Cursando ensino medio - Colegio Cotemig</li>
        </ul>
        
        <h2>Experiência</h2>
        <ul>
            <li>Contabilidade na empresa do meu pai</li>
            <li>vendas na vidraçaria da minha mãe</li>
        </ul>
        
        <h2>Habilidades</h2>
        <ul>
            <li>Python</li>
            <li>Flask</li>
            <li>HTML e CSS</li>
            <li>JavaScript</li>
            <li>C#</li>
            <li>Figma</li>
            <li>MySql</li>
            <li>VirtualBox</li>
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)