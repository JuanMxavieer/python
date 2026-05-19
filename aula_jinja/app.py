from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def questao1():
    return render_template("questao1.html", name = "Juan")

@app.route("/q2")
def q2():
    dados = { "nome": "Juan", "idade" : 18}
    return render_template("q2.html", aluno = dados)

@app.route("/q3")
def q3():
    usuario = {"nome": "Ana", "email": "ana@email.com"}
    return render_template("q3.html", aluno = usuario)


if __name__ == "__main__":
    app.run(debug=True)