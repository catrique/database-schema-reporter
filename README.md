## Gerador de Inventário de Banco de Dados

Um script em Python para gerar um inventário consolidado de tabelas, colunas e tipos de dados de múltiplos bancos de dados SQL Server, exportando o resultado para um arquivo Excel.

-----

## 🚀 Como Usar

### Pré-requisitos

Certifique-se de que você tem o Python 3 instalado e as bibliotecas necessárias:

  - **`pyodbc`**: para conectar ao SQL Server.
  - **`openpyxl`**: para gerar o arquivo Excel.
  - **`ODBC Driver 17 for SQL Server`**: o driver necessário para a conexão.

Para instalar as bibliotecas Python, use o pip:

```bash
pip install pyodbc openpyxl
```

### Configuração

1.  Abra o arquivo `listar_tabelas.py`.
2.  Atualize as variáveis de conexão com suas credenciais: `server`, `username`, `password`.
3.  Modifique a lista `bancos_de_dados` para incluir os nomes dos bancos que você quer analisar.

<!-- end list -->

```python
server = 'seu_servidor'
username = 'seu_login'
password = 'sua_senha' 
bancos_de_dados = [
    'nome_do_seu_banco_1',
    'nome_do_seu_banco_2'
]
```

### Execução

Execute o script diretamente do seu terminal:

```bash
python listar_tabelas.py
```

O script irá gerar um arquivo `listagem_completa.xlsx` no mesmo diretório.

-----

## 🛠️ Detalhes Técnicos

  - **Tecnologia**: Python 3
  - **Bibliotecas**: `pyodbc`, `openpyxl`
  - **Funcionalidades**:
      - Conecta a múltiplos bancos de dados SQL Server.
      - Utiliza o `INFORMATION_SCHEMA` para consultar metadados.
      - Consolida as informações de todos os bancos em uma única planilha.
      - Inclui o nome do banco, schema, nome da tabela, nome da coluna e tipo de dado.

-----