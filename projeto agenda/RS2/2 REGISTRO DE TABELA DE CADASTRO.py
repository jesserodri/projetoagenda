import sqlite3
conector = sqlite3.connect("agenda.db")
cursor= conector.cursor()
sql="select * from contratos"
cursor.execute(sql)
dados=cursor.fetchall()
cursor.close()
conector.close()

print("\nConsulta ao Banco de Dados agenda.db \n")
print("Dados da tabela dos contratos")
print("-"*35)
print("{} {} {} {} {} {}".format("codigo","nome","cel","telefone","email","data aniversario"))
for d in dados:
    print("{}{}{}{}{}{}".format(d[0],d[1],d[2],d[3],d[4],d[5]))

print("-"*35)
print("Encontrados {} registros".format(len(dados)))
print("\n\nFIM DO PROGRAMA")
