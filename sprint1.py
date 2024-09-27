import csv
import pandas as pd
import matplotlib.pyplot as plt
import random

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

# Função para escrever os dados no arquivo CSV
def escrever_csv(dados, nome_arquivo, cabecalho):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
        escritor_csv.writeheader()  # Escreve o cabeçalho
        for dado in dados:
            escritor_csv.writerow(dado)  # Escreve cada linha de dados
    print(f'Arquivo CSV "{nome_arquivo}" criado com sucesso!')

# Chamando a função para escrever o arquivo CSV
escrever_csv(dados_formula_e, nome_arquivo, cabecalho)

# Função para carregar dados de um arquivo CSV usando o módulo csv
def carregar_dados(caminho_arquivo):
    try:
        with open(caminho_arquivo, mode='r', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            dados = list(leitor_csv)
            return dados
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo '{caminho_arquivo}': {str(e)}")
        return None

# Função para gerar informações aleatórias sobre carros da Fórmula E
def gerar_info_carros():
    carros = [
        "Audi e-tron FE07", "BMW iFE.21", "DS E-Tense FE21", "Jaguar I-Type 5", "Mahindra M7Electro",
        "Mercedes-Benz EQ Silver Arrow 02", "NIO 333 001", "Nissan IM03", "Porsche 99X Electric", "Venturi 6"
    ]
    carro_aleatorio = random.choice(carros)
    return f"Informações sobre o carro atual da Fórmula E: {carro_aleatorio}"

# Função para gerar informações aleatórias sobre passeios virtuais na Fórmula E
def gerar_info_passeios():
    passeios = [
        "Passeio virtual pelo circuito de Berlim", "Visita virtual aos boxes da equipe Mercedes-EQ",
        "Tour virtual pelo simulador de corrida da Audi Sport ABT Schaeffler", "Exploração virtual do centro de pesquisa da DS Techeetah"
    ]
    passeio_aleatorio = random.choice(passeios)
    return f"Descubra mais: {passeio_aleatorio}"

# Função para exibir saudação personalizada com informações aleatórias sobre carros e passeios virtuais
def saudacao(nome):
    mensagem = f"Olá, {nome}! Bem-vindo ao site interativo da Fórmula E. Aqui você encontrará {gerar_info_carros()}, e também poderá desfrutar de {gerar_info_passeios()}.\n\n"
    mensagem += "Para mais informações sobre os carros da Fórmula E, visite: https://www.fiaformulae.com/en/technology\n"
    mensagem += "Para experimentar passeios virtuais, visite: https://www.fiaformulae.com/en/virtual-tours\n"
    return mensagem

# Função para exibir estatísticas básicas dos dados (usando pandas)
def exibir_estatisticas(dados):
    if dados is not None:
        df = pd.DataFrame(dados)
        print("Estatísticas do DataFrame:")
        print(df.describe())
    else:
        print("Não é possível exibir estatísticas pois os dados estão vazios ou não foram carregados corretamente.")

# Função para exibir classificações dos pilotos por pontos
def exibir_classificacoes(dados):
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

# Função para visualizar dados em um gráfico de barras (usando pandas e matplotlib)
def visualizar_dados(dados):
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

# Função principal (main) para execução do programa
def executar_programa():
    nome_usuario = input("Digite seu nome: ")
    print(saudacao(nome_usuario))

    caminho_arquivo = input("Digite o caminho do arquivo CSV com os dados dos pilotos da Fórmula E: ")
    
    # Tentar carregar e processar os dados
    dados = carregar_dados(caminho_arquivo)
    if dados is not None:
        exibir_estatisticas(dados)
        exibir_classificacoes(dados)
        visualizar_dados(dados)

# Chamar a função principal para execução do programa
executar_programa()
