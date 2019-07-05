# DesafioVizir
Desafio realizado para a selação ShowMeTheCode2019 Para a empresa Vizir

O desafio foi realizado com utilização de linguagem Python, com módulos nativo de teste unittest e utilizando orientação de objetos, de maneira a respeitar os requisitos solicitados.

## Instalação

Realizar instalação de python versão 3.7.3 (mais recente) via download de Exe:
> https://www.python.org/downloads/

para os testes Web executar instalação de flask utilizando comando via terminal:
> pip install flask=0.12.2

## Interpretação de exercício

  Uma vez lidos os requisitos foram encontrados pontos abertos, que poderiam ser interpretados de formas incertas, para estes pontos, assumi o seguinte:
  * Para os pares de DDD Origem-x-Destino que não estavam com taxas definidas na tabela, foi assumido que as ligações não eram permitidas, portanto não deveria ser possível realizar simulação de valor a pagar.
  * Para as simulações entre DDDs iguais não foi informado que haveria uma taxa fixa ou um valor estipulado, então assumi que estas ligações estariam gratuitas ou inclusas no pacote de maneira que não neste exercício, as simulações destes valores vão resultar em R$0.00.
  * Embora não especificados, compreendi os exemplos de simulação de planos comFaleMais x semFaleMais disponibilizados, como testes unitários que deveriam ser executados, eles estão configurados como um dos testes executados na classe TestCases

## Execução

realizar o download dos arquivos do zip enviado e uma vez dentro da pasta vizir, executar o comando abaixo para verificar a execução de teste manual:

> python telzir_main.py

Serão impressos outputs de simulação de planos com plano FaleMais, tambem foi adicionada à Classe Cliente a opção de Mudar seu plano, utilizando um catalogo previamente estabelecido.

> O valor a pagar será de R$0.00
> O valor a pagar será de R$37.40
> O valor a pagar será de R$167.20
> Taxa de ligação não cadastrada no sistema. Impossível simular valores entre DDD de origem e destino
> Alterando plano de "comum" para "FaleMais30"...
> Concluído!

Para o teste das classes foi utilizado o módulo unittest, nativo com a versão 3 do Python. Para execução, dentro da pasta Vizir, executar o seguinte comando:

> python TestCases.py

São impressos outputs utilizados dentro das classes para execução manual, mas o resultado de asserts é retornado pelo framework/módulo unittest com dados dos testes realizados

> Alterando plano de "comum" para "FaleMais30"
> Concluído!
> O valor a pagar será de R$0.00\n
> O valor a pagar será de R$37.40
> O valor a pagar será de R$167.20
> Taxa de ligação não cadastrada no sistema. Impossível simular valores entre DDD de origem e destino
> O valor a pagar será de R$38.00
> O valor a pagar será de R$136.00
> O valor a pagar será de R$380.00
> Taxa de ligação não cadastrada no sistema. Impossível simular valores entre DDD de origem e destino
> .
----------------------------------------------------------------------
> Ran 7 tests in 0.016s
> OK

Para o teste do app será necessária a instalação do módulo Flask, ele não é nativo. Para Verificação do resultado obtido seguir passos abaixo:

Utilizar comando no CMD para iniciar o servidor:

> python app.py

Acessar pelo navegador o endereço retornado

> Restarting with stat
> Debugger is active!
> Debugger PIN: 924-465-269
> Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Observar a página exibida e fazer as interações desejadas

# Observações

Estou estudando Python para Web, e dessa forma planejo entender o funcionamento de aplicações web e sua configuração. Python é a linguagem que possuo maior afinidade. Gostaria de dizer que o projeto foi a primeira vez que realmente apliquei conhecimentos de programação para um WebApp, e que em pouco tempo consegui sair do zero e alcançar uma página satisfatória para meus objetivos

Devido à outros compromissos desenvolvi todos os códigos em 3 noites e a documentação no dia da entrega. 
Agradeço a oportunidade de me desenvolver com este desafio pela equipe da Vizir
