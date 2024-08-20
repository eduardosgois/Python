import pandas as pd

# Caminho para o arquivo CSV original
input_csv_path = 'caminho/para/seu/arquivo.csv'

# Defina o número de linhas por cada arquivo dividido
linhas_por_arquivo = 1000

# Leia o arquivo CSV
df = pd.read_csv(input_csv_path)

# Calcule o número total de arquivos necessários
num_arquivos = (len(df) // linhas_por_arquivo) + 1

for i in range(num_arquivos):
    # Determine o intervalo de linhas para este arquivo
    inicio = i * linhas_por_arquivo
    fim = inicio + linhas_por_arquivo
    
    # Extraia a parte do DataFrame para este arquivo
    df_part = df.iloc[inicio:fim]
    
    # Defina o caminho para o arquivo dividido
    output_csv_path = f'caminho/para/saida/arquivo_parte_{i+1}.csv'
    
    # Escreva o DataFrame parcial em um novo arquivo CSV
    df_part.to_csv(output_csv_path, index=False)
    
    print(f'Arquivo {output_csv_path} criado com sucesso.')
