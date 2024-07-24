Desafio 1

1º) O que é um VCS/SCM (Sistema de Controle de versões)?

 - VCS é um software que gerencia arquivos, tendo a função principal substituir os arquivos antigos de um programa por novos, o mesmo também é utilizado para fazer documentação e controle de histórico de desenvolvimento de códigos-fonte.

2º) Cite 5 vantagens de utilizar um VCS

1- O Controle de versão qual permite acompanhar as alterações feitas no código ao longo do tempo.

2- A função de Colab qual permite que vários desenvolvedores trabalhem simultaneamente, sem sobrescrever o trabalho uns dos outros.

3- O Backup seguro, o código fonte é armazenado em repositórios remotos, facilitando o procedimento de recuperação em caso de perda de arquivos.

4- O Rastreamento de bugs, o VCS permite vincular mudanças de código a tickets de bugs, facilitando a correção de erros, tornando possível identificar quais mudanças trouxeram o problema.

5- O Sistema de Automação e integração contínua, qual permite o VCS integrar-se com outras ferramentas de desenvolvimento, permitindo a automação de testes, builds e deploys, melhorando a eficiência e reduzindo a probabilidade de erros.

3º) Dê 3 exemplos de VCS

Git, Subversion, CVS.

Pós-créditos: Mercurial

Desafio 2

1º) Defina POO e cite seus pilares. (min 10, máx 20 linhas)

POO é um paradigma de programação que utiliza objetos como a principal unidade de código, cada objeto guarda dados e comportamentos relacionados. Sendo é projetada para ““melhorar”” a modularidade e facilitar a reutilização de códigos.
Os pilares da POO são: abstração, encapsulamento, herança e polimorfismo.
•	Abstração é o conceito de simplificar um sistema complexo, escondendo detalhes desnecessários, facilitando a exibição do conteúdo essencial.
•	Encapsulamento é o conceito de restringir o acesso direto a componentes de um objeto, protegendo os dados de modificações indevidas
•	Herança é o conceito de criar novas classes a partir de classes existentes, aproveitando estendendo funcionalidades.
•	Polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme, mesmo que seus comportamentos sejam diferentes.

2º) Exemplifique um cenário de abstração.

Vamos supor que fizemos uma locadora de veículos, no código fizemos uma classe “Veiculo” qual representa um veículo genérico, contendo atributos como marca, modelo e ano.
Com a abstração não é preciso se preocupar com os detalhes específicos de cada tipo de veículo na classe “Veiculo”, apenas com a ideia geral de um veículo.

3º) Exemplifique um cenário de encapsulamento.

Usando o exemplo da locadora, os atributos da classe “Veiculo” seriam privados, impedindo-os de serem modificados.

4º) Exemplifique um cenário de herança.

Ainda usando o exemplo da locadora, vamos supor que temos as classes “Carro” e “Moto” que herdam da classe “Veiculo”.
isso significa que Carro e moto teriam os mesmos atributos e métodos de “Veiculo”, mas podendo adicionar ou modificar funcionalidades específicas.
Por exemplo, “Moto” pode ter um atributo extra indicando as cilindradas.


5º) Exemplifique um cenário de polimorfismo.

Podemos ter uma lista de veículos que inclui os carros e as motos, mesmo que “Carro” e “Moto” sejam classes diferentes, podemos chamar o método para exibir as informações de cada veículo na lista sem se preocupar com o tipo de veículo.

6º) Cite 5 vantagens da POO.

Reutilização de código, modularidade, facilidade de manutenção, a abstração e o polimorfismo.

(Na realidade POO parece um paraíso quando apresentado dessa forma, mas quando você programa em Java você descobre que isso tudo é uma ilusão e não existe nenhuma vantagem, existe apenas dor e quem gosta é masoquista).

Desafio 3

1º) Com suas palavras, defina o que é o protocolo de comunicação HTTP e como ele funciona. (Mínimo 10 linhas)

O HTTP (HyperText Transfer Protocol) é um protocolo de comunicação utilizado para transferir dados na WEB. Funciona sobre o protocolo TCP/IP e define como as mensagens são formatadas e transmitidas entre “Clients” como navegadores e servidores Web. Quando um Client tenta acessar uma página, ele envia uma requisição HTTP ao servidor, especificando o recurso desejado como uma página HTML. O Servidor processa a solicitação e responde com um status e os dados solicitados. O HTTP é um protocolo sem estado, o que significa que cada requisição é independente e não mantém informações sobre solicitações anteriores. 
A versão mais comum é a HTTP/1.1, mas a 2 e 3 tem melhorias significativas em eficiência e segurança.

2º) Defina o que é REST e qual é a sua relação com o protocolo HTTP.

REST (Representational State Transfer) é um estilo de arquitetura para construir serviços WEB que utilizam o protocolo HTTP para comunicação.
Em sistemas RESTful, recursos são identificados por URLs e manipulados usando os métodos HTTP:
• GET para recuperar dados
• POST para criar novos recursos
• PUT para atualizar recursos.
• DELETE para remover recursos.
As respostas podem ser em formatos JSON ou XML, REST aproveita as funcionalidades padrão do HTTP para criar serviços simples, escaláveis e independentes entre o Client e o Servidor.

3º) Defina o que é Web API, e qual é a sua relação com REST.

Uma WEB API (Interface de Programação de Aplicações na WEB) é um conjunto de regras e protocolos que permite que a comunicação entre diferentes softwares via web. Ela expõe endpoints que podem ser acessados através de requisições HTTP para realizar operações como criar, ler, atualizar e deletar dados.
A relação com REST é que muitas WEB APIs são projetadas seguindo os princípios RESTful, utilizando métodos HTTP para manipular os recursos identificados por URLs.

4º) Liste todos os métodos de solicitações HTTP utilizados pelo padrão REST e suas respectivas finalidades.

• GET: Recupera informações de um recurso.
• POST: Cria um novo recurso.
• PUT: Atualiza um recurso existente.
• DELETE: Remove um recurso.
• PATCH: Aplica atualizações parciais a um recurso.
• HEAD: Recupera apenas os cabeçalhos de resposta.
• OPTIONS: Verifica os métodos suportados para um recurso.
• TRACE: Realiza uma mensagem de loop-back de teste para diagnóstico.

Desafio 4

1º) Defina com as suas palavras qual é a responsabilidade das camadas: Entity, Controller, Repository e Service

• Entity é uma das camadas do sistema de arquitetura de software que é responsável por gerenciar e representar os dados de um sistema.
• Controller é a camada responsável por ligar o Model e o View, fazendo com que os modelos possam ser repassados para as views e vice-versa.
• Repository permite separar a lógica de acesso a dados da lógica de negócio, proporcionando uma maior flexibilidade e facilidade de manutenção do código.
• Service ajuda a formar um encapsulamento claro e restrito de código ao implementar tarefas comerciais, cálculos e processos.