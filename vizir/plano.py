class Plano():

    _matriz_precos = {
        "011": {
            "011": 0,
            "016": 1.9,
            "017": 1.7,
            "018": 0.9
        },
        "016": {
            "011": 2.9,
            "016": 0,
            "017": -1,
            "018": -1
        },
        "017": {
            "011": 2.7,
            "016": -1,
            "017": 0,
            "018": -1
        },
        "018": {
            "011": 1.9,
            "016": -1,
            "017": -1,
            "018": 0
        }
    }

    def __init__(self, nome, minutos_gratuitos = 0):
        self._nome = nome
        if nome == "comum": #se o nome for comum, não serão permitidos minutos gratuitos mesmo que sejam passados
            self._minutos_gratuitos = 0
        else:
            self._minutos_gratuitos = minutos_gratuitos


    def simular_custo(self, origem, destino, minutos_falados):
        taxa = self._matriz_precos[origem][destino]
        if self._matriz_precos[origem][destino] == -1:
            print("Taxa de ligação não cadastrada no sistema. Impossível simular valores entre DDD de origem e destino")
            return -1
        else:
            if self._nome == "comum":
                #utilizar Max pra me certificar que o calculo será zero ou maior
                valor = max((minutos_falados - self._minutos_gratuitos), 0) * taxa
            else:
                valor = max((minutos_falados - self._minutos_gratuitos), 0) * (taxa*1.1) #taxa acresimda de 10% por não estar no comum
            print("O valor a pagar será de R${0:.2f}".format(valor))
            return round(valor,2)

    def get_nome(self):
        return self._nome

    def get_minutos_gratuitos(self):
        return self._minutos_gratuitos
