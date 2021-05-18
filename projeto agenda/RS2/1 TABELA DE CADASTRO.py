import sqlite3
conector = sqlite3.connect("e.db")
cursor = conector.cursor()
sql="""
    create table contratos
    (codigo inter,
    nome  text,
    cel text,
    Telefone text,
    email text,
    'data aniversario', text)
"""
cursor.execute(sql)
sql="""
   insert into contratos
    (codigo, nome, cel, telefone, email, 'data aniversario')values(2,'maria do sarara',998455652,27155225,'mariazinhaesquisita@gmail.com','20-09-2000')
    """
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()
