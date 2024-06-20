import json
import os
from datetime import datetime

data_atual = datetime.now().strftime("%d/%m/%Y")

def Ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo,"r") as arquivo:
        dados = json.load(arquivo)
    return dados

def Limpar():
    os.system("cls")

def Menu_principal():
    print("| Bem vindo a Clínicia de Consultas Ágil |")
    print(f"Data atual:{data_atual}\n")
    print("1. Cadastrar um paciente")
    print("2. Marcar consulta")
    print("3. Cancelar consulta")
    print("4. Lista de Consultas")
    print("5. Sair\n")

def Cadastrar_paciente(nome,telefone):
    cadastro = Ler_arquivo_json("cadastros.json")
    cadastro.append({"nome":nome,"telefone":telefone})

    with open("cadastros.json","w") as arquivo:
        json.dump(cadastro, arquivo, indent=4)
    print("\nPaciente cadastrado com sucesso!")
    input("Digite qualquer tecla para voltar:\n")    
    Limpar()

def Lista_de_pacientes():
    cadastros = Ler_arquivo_json("cadastros.json")
    print("|  Pacientes  |")
    for indice, cadastro in enumerate(cadastros, start=1):
        print (f"{indice}. {cadastro["nome"]}")

def Escolha_cadastro():
    Limpar()
    print("Escolha o cadastro")
    Lista_de_pacientes()
    print("Digite 0 para voltar")
    resposta = int(input("\n"))
    if resposta == 0:
        main()
    Limpar()
    cadastro = Ler_arquivo_json("cadastros.json")
    print(f"{cadastro[resposta-1]["nome"]}")
    print(f"telefone:{cadastro[resposta-1]["telefone"]}")
    print("1. Marcar consulta")
    print("2. Voltar")
    return resposta

def Fazer_consultas(nome, dia, horario, especialidade):
    consulta = Ler_arquivo_json("consultas.json")
    consulta.append({"nome":nome, "dia":dia, "horario":horario, "especialidade": especialidade})

    with open("consultas.json", "w") as arquivo:
        json.dump(consulta, arquivo, indent=4)
    print("\nConsulta Realizada com sucesso!") 
    input("Digite qualquer tecla para voltar:\n")    
    Limpar()   

def Marcar_consulta():
    cadastro = Ler_arquivo_json("cadastros.json")
    resposta = Escolha_cadastro()
    escolha_paciente = int(input(""))
    Limpar()

    if escolha_paciente == 1:
        nome = cadastro[resposta-1]["nome"]
        print(f"Consulta no cadastro de {cadastro[resposta-1]["nome"]}\n")
        dia = input("Digite a data da consulta (dd/mm/aaaa):\n")
        if dia < data_atual:
            print("Está data não pode ser agendada")
            input("Digite qualquer tecla para marcar novamente:\n")
            Marcar_consulta()
        horario = input("Digite o horário da consulta (hh:mm):\n")
        especialidade = input("Digite a especialidade desejada da consulta:\n")
        if not Buscar_dias(dia,data_atual) and not Buscar_horario(horario,dia):
            Fazer_consultas(nome, dia, horario, especialidade)
    elif escolha_paciente == 2:
        Marcar_consulta()
    else:
        print("Opção inválida!")
        input("\nDigite qualquer tecla para voltar:\n")
        Marcar_consulta()

def Lista_de_consultas():
    consultas = Ler_arquivo_json("consultas.json")
    print("|  Consultas  |")
    for indice, consulta in enumerate(consultas, start=1):
        print (f"{indice}. {consulta["nome"]}")
   
def Escolha_consulta():
    Limpar()
    print("Escolha a consulta")
    Lista_de_consultas()
    print("Digite 0 para voltar")
    resposta = int(input("\n"))
    Limpar()
    if resposta == 0:
        main()
    else:
        consulta = Ler_arquivo_json("consultas.json")
        print(f"{consulta[resposta-1]["nome"]}")
        print(f"dia: {consulta[resposta-1]["dia"]}")
        print(f"horario: {consulta[resposta-1]["horario"]}")
        print(f"especialidade: {consulta[resposta-1]["especialidade"]}")
        print("1. Cancelar consulta")
        print("2. Voltar")
        return resposta

def Cancelar_consulta():
    consulta = Ler_arquivo_json("consultas.json")
    escolha = Escolha_consulta()
    escolha_cancelamento = int(input(""))
    Limpar()

    if escolha_cancelamento == 1:
      consulta.pop(escolha-1)
      with open("consultas.json", "w") as arquivo:
            json.dump(consulta, arquivo, indent=4)
      print("Consulta removida com sucesso!")
      input("\nDigite qualquer tecla para voltar:\n")
      Limpar()
    elif escolha_cancelamento == 2:
        Cancelar_consulta()
    elif escolha_cancelamento == 0:
        return
    else:
        print("Opção inválida!")
        input("\nDigite qualquer tecla para voltar:\n")
        Cancelar_consulta()

def Buscar_numero(telefone):
    cadastros = Ler_arquivo_json("cadastros.json")
    for cadastro in cadastros:
        if cadastro["telefone"] == telefone:
            print("Este numero numero de telefone já está cadastrado!")
            input("\nDigite qualquer tecla para voltar:\n")
            Limpar()    
            return True
    return False

def Buscar_dias(dia, data_atual):
    consultas = Ler_arquivo_json("consultas.json")
    for consulta in consultas:
        if consulta["dia"] == dia:
            print("Este dia já está agendado!")
            input("\nDigite qualquer tecla para voltar:\n")
            Limpar()    
            return True
        elif consulta["dia"] < data_atual:
            print("Esta data não pode ser marcada!")
            input("\nDigite qualquer tecla para voltar:\n")
            Limpar()
            return True
    return False  

def Buscar_horario(horario,dia):
    consultas = Ler_arquivo_json("consultas.json")
    for consulta in consultas:
        if consulta["horario"] == horario and consulta["dia"] == dia:
            print("Este horario já está ocupado!")  
            input("\nDigite qualquer tecla para voltar:\n")
            Limpar()    
            return True
    return False

def Escolha_lista_de_consulta():
    Limpar()
    print("Escolha a consulta")
    Lista_de_consultas()
    print("Digite 0 para voltar")
    resposta = int(input("\n"))
    Limpar()
    if resposta == 0:
        main()
    else:
        consulta = Ler_arquivo_json("consultas.json")
        print(f"{consulta[resposta-1]["nome"]}")
        print(f"dia: {consulta[resposta-1]["dia"]}")
        print(f"horario: {consulta[resposta-1]["horario"]}")
        print(f"especialidade: {consulta[resposta-1]["especialidade"]}")
        print("1. Listas de consulta")
        print("2. Voltar ao menu principal")
        return resposta

def Lista_consulta_marcadas():
    Limpar()
    Escolha_lista_de_consulta()
    escolha_cancelamento = int(input(""))
    Limpar()
    if escolha_cancelamento == 1:
        Lista_consulta_marcadas()
    elif escolha_cancelamento == 2:
        main()

def main():
    Limpar()
    while True:
        Menu_principal()
        resposta_inicial = int(input("Escolha uma opção:\n"))
        if resposta_inicial == 1:
                Limpar()
                nome = input("Digite o nome do paciente:\n").upper()
                telefone = input("Digite o telefone do paciente:\n")
                if not Buscar_numero(telefone):
                    Cadastrar_paciente(nome,telefone)
        elif resposta_inicial == 2:
            Lista_de_pacientes()
            Marcar_consulta()
        elif resposta_inicial == 3:
            Cancelar_consulta()
        elif resposta_inicial == 4:
            
            Lista_consulta_marcadas()
        elif resposta_inicial == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            input("\nDigite qualquer tecla para voltar ao menu principal:\n")
            main()
    
if __name__ == "__main__":
    main()