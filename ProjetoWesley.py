import smtplib

print("Projeto de envio de emails iniciado")
caminho = "C:/Users/estev/Downloads/emails.txt"
emails = open(caminho)
envios = []
mensagem = "C:/Users/estev/Downloads/envio.txt"
enviarMensagem = open(mensagem)
enviarMensagem = enviarMensagem.read()
print( f" Texto a ser enviado: {enviarMensagem}")
linhas = emails.readlines()

for linha in linhas:
    envios.append(linha)
print(f"Emails dentro do arquivo para envio: {envios}")

for envio in envios:
    print(f"Estou enviando a mensagem para o email: {envio}")
    servico = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    #Passar o email e a senha
    servico.login("", "")
    servico.sendmail(
        "",
        f"{envio}",
        f"{enviarMensagem}"
    )
