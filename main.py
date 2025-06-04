import csv

dados = []

with open("Esp8266_Receiver.csv", "r") as projeto:
    reader = csv.DictReader(projeto)
    for now in reader:
        dados.append(now)
        print(now)

# Dicionário para converter os níveis em texto + emoji
status_estoque = {
   "0": "⚪ Sem estoque",
   "1": "🟡 Estoque médio, planejar",
   "2": "🟢 Estoque cheio, sem necessidade de planejar",
   "3": "🔴 Estoque baixo, nível crítico"
}

# Geração da página HTML
html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Monitoramento de Estoque</title>
</head>
<body>
<h1>Monitoramento de Estoque</h1>
<table border="1">
    <tr>
    <th>Data</th>
    <th>Hora</th>
    <th>Esteira 1</th>
    <th>Esteira 2</th>
    <th>Esteira 3</th>
</tr>
"""
for dado in dados:
    html += (f"<tr><td>{dado['Date']}</td><td>{dado['Time']}</td>")
    for i in range(1, 4):
        valor = dado[f"esteira{i}"]
        mensagem = status_estoque.get(valor, valor)
        html += f"<td>{mensagem}</td>"
    html += "</tr>"

html += """
    </table>
</body>
</html>
"""

# Salvar o arquivo html
with open("automacao.html", "w", encoding="utf-8") as auto:
    auto.write(html)
    print("HTML gerado com sucesso!")










