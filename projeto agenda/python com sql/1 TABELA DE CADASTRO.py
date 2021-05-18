import sqlite3
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql="""
    create table cadastro
    (codigo inter, nome text, idade integer)
"""
cursor.execute(sql)
sql="""
    insert into cadastro
    (codigo, nome, idade)values(1284,'pedro de oliveira',32)
    """
cursor.execute(sql)
sql="""
    insert into cadastro
    (codigo, nome, idade)values(1309, 'maria lucia machado',37)
    """
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()
print("abra a pasta do programa e veja se o arquivo está la")
print("fim do programa")
