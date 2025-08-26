import pyodbc
from openpyxl import Workbook
import os

server = 'seu_servidor'  # Ex: 'localhost\SQLEXPRESS', ou o IP
database = 'nome_do_seu_banco'   
username = 'seu_login'          
password = 'sua_senha'            

bancos_de_dados = [
    'lista_de_bancos'
]

print("Preparando o arquivo Excel...")
wb = Workbook()
ws = wb.active
ws.title = "Lista de Colunas"

ws.append(["Banco de Dados", "Schema", "Nome da Tabela", "Nome da Coluna", "Tipo de Dado"])

all_rows = []

for db in bancos_de_dados:
    print(f"\n Conectando e coletando dados do banco: {db}...")
    
    try:
        connection_string = (
            f'Driver={{ODBC Driver 17 for SQL Server}};'
            f'Server={server};'
            f'Database={db};'
            f'Uid={username};'
            f'Pwd={password};'
        )

        with pyodbc.connect(connection_string) as cnxn:
            cursor = cnxn.cursor()

            sql_query = """
            SELECT
                DB_NAME() AS DatabaseName,
                t.TABLE_SCHEMA AS SchemaName,
                t.TABLE_NAME AS TableName,
                c.COLUMN_NAME AS ColumnName,
                c.DATA_TYPE AS DataType
            FROM INFORMATION_SCHEMA.TABLES t
            JOIN INFORMATION_SCHEMA.COLUMNS c
                ON t.TABLE_NAME = c.TABLE_NAME
                AND t.TABLE_SCHEMA = c.TABLE_SCHEMA
            ORDER BY t.TABLE_SCHEMA, t.TABLE_NAME, c.ORDINAL_POSITION;
            """
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            print(f"   ✅ Dados coletados: {len(rows)} colunas encontradas.")

            for row in rows:
                all_rows.append([row.DatabaseName, row.SchemaName, row.TableName, row.ColumnName, row.DataType])

    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f" Erro ao processar o banco {db}: {sqlstate}")
        continue

print("\n Gerando planilha Excel...")
for row_data in all_rows:
    ws.append(row_data)

ws.column_dimensions['A'].width = 25  
ws.column_dimensions['B'].width = 15  
ws.column_dimensions['C'].width = 30  
ws.column_dimensions['D'].width = 30  
ws.column_dimensions['E'].width = 15  

file_path = "listagem_completa.xlsx"
try:
    wb.save(file_path)
    print(f"\n Planilha salva com sucesso em: {os.path.abspath(file_path)}")
except Exception as e:
    print(f"\n Erro ao salvar planilha: {e}")