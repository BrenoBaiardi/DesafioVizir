

from cliente import Cliente
from plano import Plano


if __name__ == "__main__":

    catalogo = {
        "Comum": Plano("comum"),
        "FaleMais30": Plano("FaleMais30", 30),
        "FaleMais60": Plano("FaleMais60", 60),
        "FaleMais120": Plano("FaleMais120", 120),
        }

    c = Cliente("Zé", "011", catalogo["Comum"])

    c.solicitar_simulacao(catalogo["FaleMais30"], "011", "016", 20)
    c.solicitar_simulacao(catalogo["FaleMais60"], "011", "017", 80)
    c.solicitar_simulacao(catalogo["FaleMais120"], "018", "011", 200)
    c.solicitar_simulacao(catalogo["FaleMais30"], "018", "017", 200)
    c.alterar_plano(catalogo["FaleMais30"])