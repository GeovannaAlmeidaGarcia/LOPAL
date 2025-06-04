
import smtplib

# Configurações do servidor de email
servidor_smtp = 'smtp.gmail.com'
porta = 587
usuario = 'geovanna.de.almeida.garcia@gmail.com'
senha = 'kfxk nprd jstt thyq'

# Conectando ao servidor
servidor = smtplib.SMTP(servidor_smtp, porta)
servidor.starttls()  # Inicia a criptografia TLS
servidor.login(usuario, senha)

from email.mime.text import MIMEText

# Criando a mensagem
assunto = 'Email de estoque'
corpo = 'f"Seu estoque"'
mensagem = MIMEText(corpo)
mensagem['Subject'] = assunto
mensagem['From'] = usuario
mensagem['To'] = 'geovanna.a.garcia@aluno.senai.br'

# Enviando o email
servidor.send_message(mensagem)

# Fechando a conexão com o servidor
servidor.quit()


# whatzap