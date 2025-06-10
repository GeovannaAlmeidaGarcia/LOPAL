
import csv
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import random

# Guardando a data e hora de agora
hoje = datetime.today().strftime('%Y-%m-%d')
agora = datetime.now().strftime("%H:%M:%S")

# Lista que vai armazenar os dados do CSV
dados = []

# Gerar nova linha com data, hora e status das esteiras
nova_linha = [hoje, agora, random.randint(0, 3), random.randint(0, 3), random.randint(0, 3)]
with open("Esp8266_Receiver.csv", "a", newline="") as projeto:
    escritor = csv.writer(projeto)
    escritor.writerow(nova_linha)

# Lê todas as linhas do CSV
with open("Esp8266_Receiver.csv", "r", encoding="utf-8") as projeto:
    leitor = csv.reader(projeto)
    for linha in leitor:
        dados.append(linha)

# Mensagens dos status de estoque
status_estoque = {
    "0": "⚪ Sem estoque",
    "1": "🟡 Estoque médio, planejar",
    "2": "🟢 Estoque cheio, sem necessidade de planejar",
    "3": "🔴 Estoque baixo, nível crítico"
}

# Configuração do servidor de e-mail
servidor_smtp = "smtp.gmail.com"
porta = 587
usuario = "geovanna.de.almeida.garcia@gmail.com"
senha = "qcat ljei lwtz thmd"

# Conexão e login no servidor SMTP
servidor = smtplib.SMTP(servidor_smtp, porta)
servidor.starttls()
servidor.login(usuario, senha)

# Montagem da mensagem
assunto = 'Aviso de estoque'
corpo = "Estoque do dia de hoje:\n\n"
for dado in dados:
    if len(dado) >= 5 and dado[0] == hoje:
        data = dado[0]
        hora = dado[1]
        corpo += f"Data: {data}, Hora: {hora}\n"
        for i in range(2, 5):
            esteira = dado[i]
            mensagem = status_estoque.get(esteira, "Erro")
            corpo += f"Esteira {i-1}: {mensagem}\n"
        corpo += "\n"

# Verificar o corpo gerado
print(f"Corpo do e-mail gerado:\n{corpo}")

# Criar e enviar e-mail
mensagem = MIMEText(corpo, "plain", "utf-8")
mensagem['Subject'] = assunto
mensagem['From'] = usuario
mensagem['To'] = 'geovanna.a.garcia@aluno.senai.br'

servidor.send_message(mensagem)
servidor.quit()

print("O E-mail foi enviado com sucesso!")
