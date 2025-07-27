# Boas-vindas ao repositório do Tech News

Aqui você vai encontrar os detalhes de como foi estruturar o desenvolvimento do projeto a partir deste repositório.


# Entregáveis

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />

  Um projeto que tem como principal objetivo fazer consultas em notícias sobre tecnologia.

  As notícias são obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).

  <strong>🚵 Habilidades trabalhadas:</strong>
  <ul>
    <li>Utilizar o terminal interativo do Python</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos</li>
    <li>Aplicar técnicas de raspagem de dados</li>
    <li>Extrair dados de conteúdo HTML</li>
    <li>Armazenar os dados obtidos em um banco de dados</li>
  </ul>

</details>


# Orientações
<details>
  <summary><strong>⚠ Antes de começar a desenvolver</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:p4n1k0/Tech-News.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd Tech-News`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`  
  
</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├── tech_news
  │   ├── analyzer
  │   │   ├── 🔹ratings.py
  │   │   └── 🔹search_engine.py
  │   ├── 🔸database.py
  │   └── 🔹menu.py
  │   └── 🔹scraper.py
  ├── tests
  │   ├── 🔸assets/*
  │   ├── 🔸__init__.py
  │   ├── 🔸generate_fixture.py
  │   ├── 🔸news.py
  │   ├── 🔸test_menu.py
  │   ├── 🔸test_ratings.py
  │   ├── 🔸test_scraper.py
  │   ├── 🔸test_search_engine.py
  │   └── 🔸utils.py
  ├── 🔸dev-requirements.txt
  ├── 🔸docker-compose.yml
  ├── 🔸Dockerfile
  ├── 🔸pyproject.toml
  ├── 🔸README.md
  ├── 🔸requirements.txt
  ├── 🔸setup.cfg
  ├── 🔸setup.py
  └── 🔸trybe.yml
  ```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  ```bash
python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py
  ```

  Caso queria executar um teste especifico de um arquivo basta executar o comando:

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

  <strong>✍️ Teste Manual</strong>
  
  Abra um terminal Python importando as funções de interesse através do comando:

  <code>python3 -i tech_news/arquivo_de_interesse.py</code> 

</details>

<details>
  <summary><strong>🐳Docker</strong></summary>
  Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:

  ```bash
  docker-compose run --rm news pytest
  ```
Obs: Mairoia de testes foram desenvolvidos pelo time da trybe
</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary>
  As notícias a serem raspadas estarão disponíveis no _Blog da Trybe_: https://blog.betrybe.com.
  Essas notícias devem ser salvas no banco de dados utilizando as funções python que já vêm prontas no módulo `database.py`

  <strong>MongoDB</strong>

  Para a realização deste projeto, utilizaremos um banco de dados chamado `tech_news`.
  As notícias serão armazenadas em uma coleção chamada `news`.
  Já existem algumas funções prontas no arquivo `tech_news/database.py` que te auxiliarão no desenvolvimento.
  Não altere as funções deste arquivo; mudanças nele não serão executadas no avaliador automático.

  Rodar MongoDB via Docker:
  <code>docker-compose up -d mongodb</code> no terminal. 
  Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

  Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

  Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
  MacOS:  https://docs.mongodb.com/guides/server/install/
  
  Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
  Lembre-se de que o mongoDB utilizará por padrão a porta 27017. Se já houver outro serviço utilizando esta porta, considere desativá-lo.

</details>



<details>
  <summary><strong>🗣 Me dê feedbacks sobre o projeto!</strong></summary><br />

</details>

---

