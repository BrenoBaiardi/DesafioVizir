import unittest
from plano import Plano
from cliente import Cliente

class TestCliente(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.catalogo = {
            "Comum": Plano("comum"),
            "FaleMais30": Plano("FaleMais30", 30),
            "FaleMais60": Plano("FaleMais60", 60),
            "FaleMais120": Plano("FaleMais120", 120),
        }


    def setUp(self):
        self.c_1 = Cliente("Exemplo", "011", self.catalogo["Comum"])

    def test_init_cliente_valido(self):

        self.assertEqual(self.c_1.get_status()["nome"], "Exemplo")
        self.assertEqual(self.c_1.get_status()["DDD"], "011")
        self.assertEqual(self.c_1.get_status()["Plano"].get_nome(), "comum")

    def test_init_cliente_invalido(self):

        try:
            Cliente("Exemplo", "012", self.catalogo["Comum"])
            created = True
        except:
            created = False
        self.assertFalse(created)

    def test_alterar_plano_cliente(self):
        self.c_1.alterar_plano(self.catalogo["FaleMais30"])



class TestPlano(unittest.TestCase):

    def setUp(self):
        self.catalogo = {
            "1": Plano("comum"),
            "2": Plano("FaleMais30", 30),
            "3": Plano("FaleMais60", 60),
            "4": Plano("FaleMais120", 120),
        }

    def test_init_plano_comum(self):
        self.assertEqual(self.catalogo["1"].get_nome(), "comum","Erro na criação do nome")
        self.assertEqual(self.catalogo["1"].get_minutos_gratuitos(), 0, "Não deveria haver benefício de gratuidade")

    def test_init_plano_FaleMais(self):
        self.assertEqual(self.catalogo["2"].get_nome(), "FaleMais30","Erro na criação do nome")
        self.assertEqual(self.catalogo["2"].get_minutos_gratuitos(), 30, "Bônus deveria ser de exatamente 30 minutos")
        self.assertEqual(self.catalogo["3"].get_nome(), "FaleMais60", "Erro na criação do nome")
        self.assertEqual(self.catalogo["3"].get_minutos_gratuitos(), 60, "Bônus deveria ser de exatamente 60 minutos")
        self.assertEqual(self.catalogo["4"].get_nome(), "FaleMais120", "Erro na criação do nome")
        self.assertEqual(self.catalogo["4"].get_minutos_gratuitos(), 120, "Bônus deveria ser de exatamente 120 minutos")

    def test_simular_custo_comum(self):
        self.assertEqual(self.catalogo["1"].simular_custo("011", "016", 20), 38.0,
                         "O valor a Pagar deveria ser R$38 em plano Comum")
        self.assertEqual(self.catalogo["1"].simular_custo("011", "017", 80), 136.0,
                         "O valor a Pagar deveria ser R$38 em plano Comum")
        self.assertEqual(self.catalogo["1"].simular_custo("018", "011", 200), 380.0,
                         "O valor a Pagar deveria ser R$38 em plano Comum")
        self.assertEqual(self.catalogo["1"].simular_custo("018", "017", 100), -1,
                         "Não deveria ser possível calcular, pois não ha taxa na tabela")

    def test_simular_custo_Falemais(self):
        self.assertEqual(self.catalogo["2"].simular_custo("011", "016", 20), 0.0,
                         "O valor a Pagar deveria ser R$0 em plano Falemais30")
        self.assertEqual(self.catalogo["3"].simular_custo("011", "017", 80), 37.40,
                         "O valor a Pagar deveria ser R$37.40 em plano Falemais60")
        self.assertEqual(self.catalogo["4"].simular_custo("018", "011", 200), 167.20,
                         "O valor a Pagar deveria ser R$167.20 em plano Falemais120")
        self.assertEqual(self.catalogo["1"].simular_custo("018", "017", 100), -1,
                         "Não deveria ser possível calcular, pois não ha taxa na tabela")



if __name__ == "__main__":
    unittest.main()
