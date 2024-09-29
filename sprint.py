import csv
import pandas as pd
import matplotlib.pyplot as plt
import random
from typing import List, Dict, Optional

# Dados fictícios de pilotos da Fórmula E
dados_formula_e = [
    {"Piloto": "Jean-Éric Vergne", "Equipe": "DS Techeetah", "Pontos": 60},
    {"Piloto": "António Félix da Costa", "Equipe": "DS Techeetah", "Pontos": 50},
    {"Piloto": "Sam Bird", "Equipe": "Jaguar Racing", "Pontos": 45},
    {"Piloto": "Lucas di Grassi", "Equipe": "Audi Sport ABT Schaeffler", "Pontos": 40},
    {"Piloto": "Stoffel Vandoorne", "Equipe": "Mercedes-EQ Formula E Team", "Pontos": 35}
]

# Nome do arquivo CSV a ser criado
nome_arquivo = "dados_formula_e.csv"

# Cabeçalho do CSV
cabecalho = ["Piloto", "Equipe", "Pontos"]

def escrever_csv(dados: List[Dict[str, str]], nome_arquivo: str, cabecalho: List[str]) -> None:
    """
    Escreve os dados fornecidos em um arquivo CSV.

    Args:
        dados (List[Dict[str, str]]): Lista de dicionários com os dados a serem salvos.
        nome_arquivo (str): Nome do arquivo CSV a ser criado.
        cabecalho (List[str]): Lista com os nomes das colunas do CSV.
    """
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
        escritor_csv.writeheader()  # Escreve o cabeçalho
        for dado in dados:
            escritor_csv.writerow(dado)  # Escreve cada linha de dados
    print(f'Arquivo CSV "{nome_arquivo}" criado com sucesso!')

def carregar_dados(caminho_arquivo: str) -> Optional[List[Dict[str, str]]]:
    """
    Carrega os dados de um arquivo CSV.

    Args:
        caminho_arquivo (str): Caminho do arquivo CSV a ser carregado.

    Returns:
        Optional[List[Dict[str, str]]]: Lista de dicionários contendo os dados carregados do CSV.
    """
    try:
        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            dados = list(leitor_csv)
            return dados
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo '{caminho_arquivo}': {str(e)}")
        return None

def gerar_info_carros() -> str:
    """
    Gera informações aleatórias sobre carros da Fórmula E.

    Returns:
        str: Informação aleatória sobre um carro da Fórmula E.
    """
    carros = [
        "DS Automobiles é uma marca francesa de carros de luxo premium, uma marca de propriedade da Stellantis. A marca independente DS foi criada em 2014, a partir da antiga submarca DS e linha inspirada em modelos de carros da Citroën fabricados desde 2009, embora tenha sido separada da Citroën na Ásia desde 2012. Atualmente, a DS Automobiles é uma das montadoras que faz parte da Gen3 da Fórmula E.", "Jaguar Cars, é a empresa inglesa de automóveis de luxo pertencente a Jaguar Land Rover, uma fabricante de automóveis multinacional com sede em Coventry, Inglaterra, subsidiária da empresa indiana Tata Motors desde 2008. Atualmente, a Jaguar Cars é uma das montadoras que faz parte da Gen3 da Fórmula E.", "Mahindra Racing é uma equipe de automobilismo indiana de propriedade da fabricante de automóveis indiana Mahindra & Mahindra. Atualmente, é uma das montadoras que faz parte da Gen3 da Fórmula E", "A Maserati é uma tradicional fabricante de automóveis italiana fundada em Bolonha. A marca foi fundada em 1 de dezembro de 1914 pelos irmãos Maserati com o objetivo de desenvolver carros, e especialmente motores, além de produzir velas de ignição. Atualmente, a Maserati é uma das montadoras que faz parte da Gen3 da Fórmula E", "A ERT Formula E Team é uma equipe chinesa de automobilismo que atualmente disputa a Fórmula E. A equipe foi formada a partir da NIO 333, que é uma das montadoras que marca presença na Gen3 da modalidade de carros elétricos", "A Nissan é uma fabricante japonesa de automóveis resultante de uma fusão entre Datsun e Prince. A Nissan está listada no Nikkei 225 e é a terceira maior fabricante japonesa de automóveis depois da Toyota e Honda em capitalização de mercado. Atualmente, a Nissan é uma das montadoras que faz parte da Gen3 da Fórmula E.", "Porsche é um fabricante alemão de automóveis especializado em carros esportivos, SUVs e sedãs de alto desempenho, com sede em Stuttgart, Baden-Württemberg, Alemanha. A empresa é de propriedade do Grupo Volkswagen, cujo controle acionário pertence à Porsche SE. Atualmente, é uma das montadoras que faz parte da Gen3 da Fórmula E."
    ]
    carro_aleatorio = random.choice(carros)
    return f"Informações sobre carros atuais da Fórmula E: {carro_aleatorio}"

def gerar_info_passeios() -> str:
    """
    Gera informações aleatórias sobre passeios virtuais na Fórmula E.

    Returns:
        str: Informação aleatória sobre um passeio virtual na Fórmula E.
    """
    passeios = [
        "Passeio virtual pelo circuito de Berlim", "Visita virtual aos boxes da equipe Mercedes-EQ",
        "Tour virtual pelo simulador de corrida da Audi Sport ABT Schaeffler", "Exploração virtual do centro de pesquisa da DS Techeetah"
    ]
    passeio_aleatorio = random.choice(passeios)
    return passeio_aleatorio

def saudacao(nome: str) -> str:
    """
    Exibe uma saudação personalizada com informações aleatórias sobre carros e passeios virtuais.

    Args:
        nome (str): Nome do usuário.

    Returns:
        str: Saudação personalizada contendo informações sobre carros e passeios virtuais.
    """
    mensagem = f"Olá, {nome}! Bem-vindo ao programa interativo da Fórmula E. Aqui você encontrará informações sobre carros e montadoras da modalidade, e também poderá desfrutar de {gerar_info_passeios()}.\n\n"
    mensagem += "Para mais informações sobre os carros da Fórmula E, visite: https://www.fiaformulae.com/en/technology\n"
    mensagem += "Para experimentar passeios virtuais, visite: https://www.fiaformulae.com/en/virtual-tours\n"
    return mensagem

def exibir_estatisticas(dados: Optional[List[Dict[str, str]]]) -> None:
    """
    Exibe estatísticas básicas dos dados de pilotos utilizando pandas.

    Args:
        dados (Optional[List[Dict[str, str]]]): Lista de dicionários com os dados dos pilotos.
    """
    if dados is not None:
        df = pd.DataFrame(dados)
        print("Estatísticas do DataFrame:")
        print(df.describe())
    else:
        print("Não é possível exibir estatísticas pois os dados estão vazios ou não foram carregados corretamente.")

def exibir_classificacoes(dados: Optional[List[Dict[str, str]]]) -> None:
    """
    Exibe a classificação dos pilotos com base nos pontos.

    Args:
        dados (Optional[List[Dict[str, str]]]): Lista de dicionários com os dados dos pilotos.
    """
    if dados is not None:
        pontos_por_piloto = {}
        for dado in dados:
            piloto = dado['Piloto']
            pontos = int(dado['Pontos'])
            if piloto in pontos_por_piloto:
                pontos_por_piloto[piloto] += pontos
            else:
                pontos_por_piloto[piloto] = pontos

        pontos_por_piloto = {k: v for k, v in sorted(pontos_por_piloto.items(), key=lambda item: item[1], reverse=True)}

        print("Classificação dos pilotos por pontos:")
        posicao = 1
        for piloto, pontos in pontos_por_piloto.items():
            print(f"{posicao}. {piloto}: {pontos} pontos")
            posicao += 1
    else:
        print("Não é possível exibir classificações pois os dados estão vazios ou não foram carregados corretamente.")

def visualizar_dados(dados: Optional[List[Dict[str, str]]]) -> None:
    """
    Visualiza os dados em um gráfico de barras, representando a pontuação por equipe.

    Args:
        dados (Optional[List[Dict[str, str]]]): Lista de dicionários com os dados dos pilotos.
    """
    if dados is not None:
        pontos_por_equipe = {}
        for dado in dados:
            equipe = dado['Equipe']
            pontos = int(dado['Pontos'])
            if equipe in pontos_por_equipe:
                pontos_por_equipe[equipe] += pontos
            else:
                pontos_por_equipe[equipe] = pontos

        pontos_por_equipe = {k: v for k, v in sorted(pontos_por_equipe.items(), key=lambda item: item[1], reverse=True)}

        plt.bar(pontos_por_equipe.keys(), pontos_por_equipe.values())
        plt.title('Pontuação por Equipe na Fórmula E')
        plt.xlabel('Equipe')
        plt.ylabel('Pontos')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Não é possível visualizar dados pois os dados estão vazios ou não foram carregados corretamente.")

def menu_interativo() -> None:
    """
    Exibe o menu interativo para o usuário interagir com o programa da Fórmula E.
    """
    nome_usuario = input("Digite seu nome: ")
    print(saudacao(nome_usuario))

    caminho_arquivo = input("Digite o caminho do arquivo CSV com os dados dos pilotos da Fórmula E (ou pressione Enter para usar o padrão): ")
    if not caminho_arquivo:
        caminho_arquivo = nome_arquivo
        escrever_csv(dados_formula_e, nome_arquivo, cabecalho)

    dados = carregar_dados(caminho_arquivo)

    while True:
        print("\nEscolha uma opção:")
        print("1. Exibir estatísticas dos dados")
        print("2. Exibir classificações dos pilotos")
        print("3. Visualizar pontuações por equipe")
        print("4. Gerar informações aleatórias sobre carros da Fórmula E")
        print("5. Gerar informações sobre passeios virtuais")
        print("0. Sair")

        escolha = input("Opção: ")

        if escolha == "1":
            exibir_estatisticas(dados)
        elif escolha == "2":
            exibir_classificacoes(dados)
        elif escolha == "3":
            visualizar_dados(dados)
        elif escolha == "4":
            print(gerar_info_carros())
        elif escolha == "5":
            print(gerar_info_passeios())
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executar o menu interativo
menu_interativo()
