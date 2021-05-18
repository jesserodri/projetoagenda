import sqlite3
print("\ncria e carrea tabela cursos")
conector=sqlite3.connect("academia.db")
cursor=conector.cursor()
sql="""
    create table cursos
    (codcurso interger not NULL Primary key,
    nomecurso text, valores double)
    """

cursor.execute(sql)
print("\n .... table cursos criada")
#carrega com dados dos cursos
sql="""
insert into cursos(codcurso, nomecurso,
    valores)values(?,?,?)
"""

DadosCursos=[
(10,"cusculação",110.00),
(11,"treino aeróbico",110.00),
(12,"combo 1 : Musculação+aerobico",180.00),
(15,"natação",180.00),
(22,"pilates",165.00),
(25,"combo 2: Pilates + aerobico",240.00),
(30,"crossfit",180.00),
(41,"muay thai",140.00),
(42,"jiu jitsu",140.00),
(43,"Boxe",140.00)]

print("\n ....  dados a serem carregados")
for dados in DadosCursos:
    print("  ", dados)

cursor.executemany(sql,DadosCursos)
conector.commit()
cursor.close()
conector.close()

print("\nTabela cursos criada com sucesso")
print("\nFIM DO PROGRAMA")








    
