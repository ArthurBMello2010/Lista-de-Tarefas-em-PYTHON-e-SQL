import pyodbc

conexaoDB =  (
    "Driver={MySQL ODBC 9.7 ANSI Driver};"
    "Server=localhost;"
    "port=3306;"
    "UID=SEU ID;"
    "PWD=SUA SENHA;"
    "Database=lista_de_tarefas;"
)

conexao = pyodbc.connect(conexaoDB)
cursor = conexao.cursor()

print('Lista de Tarefas em Python e SQL')

def adtrf():
    trf = str(input('Digite a tarefa que deseja adicionar: ')).strip()
    if not trf or len(trf) < 3:
        print('Erro! Valor invalido!')
    else:
        ad = """
        INSERT INTO lista (tarefa, situacao) 
        value (?, "Nao concluida")
        """
        cursor.execute(ad, trf)
        cursor.commit()
        print('Tarefa adicionada com sucesso!')

def rmtrf():
    remtrf = str(input('Digite a tarefa que deseja remover: ')).strip().upper()
    if not rmtrf or len(remtrf) < 3:
        print('Erro! Valor invalido!')
    else:
        rm = """
        delete from lista
        where tarefa = ?
        """
        cursor.execute(rm, remtrf)
        cursor.commit()
        print('Tarefa removida com sucesso!')

def vertrfs():
    cursor.execute("select * from lista")
    lista = cursor.fetchall()

    if lista:
        for index, tarefa, situacao in lista:
            print(f'''
             ID: {index}
             Tarefa: {tarefa}
             Situacao: {situacao}''')
    else:
        print('Erro! Nenhuma tarefa encontrada!')

def marcartrf():
    nmtrf = str(input('Digite a tarefa que deseja marcar como concluida: ')).strip().lower()
    if not nmtrf or len(nmtrf) < 3:
        print('Erro! Valor Invalido!')
    else:
        marcar = """
        update lista
        set situacao = "Concluida"
        where tarefa = ?
        """
        cursor.execute(marcar, nmtrf)
        cursor.commit()
        print('Tarefa marcada com sucesso!')

while True:
    print('''Menu:
    1) Adicionar Tarefa
    2) Remover Tarefa
    3) Ver Tarefas
    4) Marcar Tarefa Concluida
    5) Sair''')
    acao = int(input('Digite a opcao desejada (1-5): '))
    if acao == 1:
        adtrf()
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if cont == 'N':
            break
    elif acao == 2:
        rmtrf()
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if cont == 'N':
            break
    elif acao == 3:
        vertrfs()
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if cont == 'N':
            break
    elif acao == 4:
        marcartrf()
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if cont == 'N':
            break
    elif acao == 5:
        break