import sqlite3
arq = open ("PesoAltura.txt","r")
L = arq.readlines()
arq.close()
print("\nLinha do arquivo")
sql="""update cadastro set peso = ?, altura = ?
        where codigo = ?"""
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
for s in L:
    d = s.rstrip()
    d = s.split(";")
    cursor.execute(sql,(d[1],d[2],d[0]))
    conector.commit()
    print(d,"  ...processando")
cursor.close()
conector.close()
print("\n\nBanco de dados atualizado com sucesso")
print("\n\nFIM DO PROGRAMA")
