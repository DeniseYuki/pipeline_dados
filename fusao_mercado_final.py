import json
import csv

from processamento_dados import Dados

#Etapa de leitura dos dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract 
dados_empresaA = Dados(path_json,'json')
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)

dados_empresaB = Dados(path_csv,'csv')
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)


#transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto':'Categoria do Produto',
                'Valor em Reais (R$)':'Preço do Produto (R$)',
                'Quantidade em Estoque':'Quantidade em Estoque',
                'Nome da Loja':'Filial' ,
                'Data da Venda':'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA,dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)
print(dados_fusao)

#Load

path_dados_combinados = 'data_processed/dados_combinados_Scripty2.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)


















#nome_colunas_csv = list(dados_csv[0].keys())
#nome_colunas_csv

#Transformação dos dados
#key_mapping = {'Nome do Item': 'Nome do Produto',
 #'Classificação do Produto':'Categoria do Produto',
 #'Valor em Reais (R$)':'Preço do Produto (R$)',
 #'Quantidade em Estoque':'Quantidade em Estoque',
 #'Nome da Loja':'Filial' ,
 #'Data da Venda':'Data da Venda'}


#dados_csv = rename_columns(dados_csv,key_mapping)
#nome_colunas_csv = get_columns(dados_csv)
#print("TRANSFORMAÇÃO DAS COLUNAS:",nome_colunas_csv)

# Combinando os dados

#dados_fusao = join(dados_json,dados_csv)
#nome_colunas_fusao = get_columns(dados_fusao)
#tamanho_dados_fusao = size_data(dados_fusao)
#print(f"Nome da coluna fusão: {nome_colunas_fusao}")
#print(f"Tamanho dos dados da fusão: {tamanho_dados_fusao}")

#Salvando dados

#dados_fusao_tabela = transformando_dados_tabela(dados_fusao,nome_colunas_fusao)

#path_dados_combinados = 'data_processed/dados_combinados_Scripty.csv'

#salvando_dados(dados_fusao_tabela,path_dados_combinados)
#print(path_dados_combinados)
