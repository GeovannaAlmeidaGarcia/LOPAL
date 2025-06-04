
import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('Esp8266_Receiver.csv')

# Exportar para Excel
df.to_excel('projeto.xlsx', index=False)
