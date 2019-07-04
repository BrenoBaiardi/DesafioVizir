from flask import Flask, render_template, request, redirect, url_for
from cliente import Cliente
from plano import Plano

app = Flask(__name__)

catalogo_planos = {
        "Comum": Plano("comum"),
        "FaleMais30": Plano("FaleMais30", 30),
        "FaleMais60": Plano("FaleMais60", 60),
        "FaleMais120": Plano("FaleMais120", 120),
        }

c = Cliente("Zé", "011", catalogo_planos["Comum"])
catalogo_ddd = c.get_cadastro_ddd()
promocoes = {i for i in catalogo_planos if i !="Comum"}

@app.route('/')
def index():
    return render_template("simulacao.html", titulo='Telzir', catalogo_ddd=catalogo_ddd, catalogo_planos=promocoes, resultado_promo="", resultado_comum="")


@app.route("/criar",methods=['POST'])
def criar():
    # handle and return class instead of string
    plano = catalogo_planos[request.form["plano"]]
    comum = catalogo_planos["Comum"]
    origem = request.form["origem"]
    destino = request.form["destino"]
    minutos_falados = float(request.form["minutos_falados"])
    resultado_promo = c.solicitar_simulacao(plano,origem,destino,minutos_falados)
    resultado_comum = c.solicitar_simulacao(comum, origem, destino, minutos_falados)
    if resultado_promo == -1:
        resultado_comum = ""
        resultado_promo = "Taxa de ligação não cadastrada no sistema. Impossível simular valores entre DDD de origem e destino"
    return render_template('simulacao.html', titulo='Telzir', catalogo_ddd=catalogo_ddd,
                           catalogo_planos=promocoes, resultado_promo=resultado_promo,resultado_comum=resultado_comum)

app.run(debug=True)