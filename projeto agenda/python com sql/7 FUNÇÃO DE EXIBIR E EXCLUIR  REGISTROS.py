import sqlite3
def ExibeCursos():
    """Exibe os cursos existentes"""
    sql = "select * from cursos"
    cursor.execute(sql)
    dados = cursor.fetchall()
    print("/zConsulta ao banco de dados academia.db\n")

    print("\nDados da tabela cursos")
    print("-"*50)
    print("{:7}{:30}{:>11}".format("codigo","nome do curso", "val/mes"))
    print("-"*25)
    
    for d in dados:
        print("{:<7}{:30}{:>10.2f}".format(d[0],d[1],d[2]))
        print("-"*50)
        print("encontrados{} regristros\n".format(len(dados)))
        
def ExcluiCurso(Codigo):
    """varifica se o curso existe e o exclui"""
    sql="""select count(codcurso)from
cursos where codcurso = :param"""
    cursor.execute(sql,{'param':Codigo})
    x = cursor.fetchone()
    print(x[0])
    if x[0] == 0:
        return "curso{} não existe".format(Codigo)
    else:
        sql="delete from cursos where codcurso=:param"
        cursor.execute (sql,{'param': Codigo})
        conector.commit()
        return "curso {}Excluido".format(Codigo)

    #o programa começa a executar por aqui
conector = sqlite3.connect("academia.db")
cursor =  conector.cursor()
while True:
    ExibeCursos()
    print("para excluir um curso digite o codigo")
    print("para sair do programa digite  0 (zero)")
    Opc=int(input("sua escolha>>"))
    if Opc == 0:
        break
    else:
        Msg = ExcluiCurso(Opc)
        print(Msg)
        dummy=input("pressione enter para prosseguir")
        cursor.close()
        conector.close()
        print("\n\n FIM DO PROGRAMA")
