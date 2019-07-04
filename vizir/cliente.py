class Cliente:

    _cadastro_ddd = ["011","016","017","018"]

    def __init__(self,nome,cidade,plano):
        if cidade not in self._cadastro_ddd:
            raise Exception("Não é possível cadastrar a cidade {} para este cliente".format(cidade))
        self._nome = nome
        self._cidade = cidade
        self._plano = plano
        # print("Cliente criado->{} \nDDD->{}\nplano->{}".format(nome, cidade, plano.get_nome()))

    def get_status(self):
        #print(self._nome,self._cidade,self._plano)
        return {"nome":self._nome,
                "DDD":self._cidade,
                "Plano":self._plano}

    def solicitar_simulacao(self, plano, origem, destino, minutos_falados):
        return plano.simular_custo(origem, destino, minutos_falados)

    def alterar_plano(self, plano):
        print("Alterando plano de \"{}\" para \"{}\"... ".format(self._plano.get_nome(), plano.get_nome()))
        self._plano = plano
        print("Concluído!")

    def get_cadastro_ddd(self):
        return self._cadastro_ddd