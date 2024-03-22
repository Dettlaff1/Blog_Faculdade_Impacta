### Blog

Projeto desenvolvido para a matéria de Software Product: Analysis, Specification, Project & Implementation - na faculdade IMPACTA.

### Como executar

É necessário que o usuário tenha as ferramentas SQLite e Python instaladas no computador.

- Crie um ambiente virtual Python: `python -m venv env`
- Ative o ambiente virtual: `source env/bin/activate` em Linux ou `env\Scripts\Activate.ps1` em Windows PowerShell
- Instale os pacotes necessários: `pip install -r requirements.txt`
- Execute os seguintes comandos para inicializar o banco de dados: 
    - `flask db init`
    - `flask db migrate`
    - `flask db upgrade`
- Execute a aplicação com o comando: `flask run`

A aplicação estará disponívels em: `http://localhost:5000`

### Como utilizar

- A página inicial lista as últimas postagens feitas no blog
- Acesse `http://localhost:5000/admin` para acessar o painel de administrador do blog
- Autentique-se como usuário `admin` e senha `admin` para acessar o painel
- No painel de administrador você terá controles para criar, editar e deletar postagens
- Clique no nome do blog escrito na navbar para voltar para a tela inicial