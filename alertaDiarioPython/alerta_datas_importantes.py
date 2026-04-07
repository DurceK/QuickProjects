import time
from datetime import datetime, timedelta
from plyer import notification
import pywhatkit

# 🔹 ID DO GRUPO WHATSAPP
GRUPO_WHATSAPP = "120363366940492971@g.us"

eventos = [
    # 🎂 Aniversários
    ("Aniversário", "Sidney Martins Ferreira", "23/11/1964"),
    ("Aniversário", "Gilson Alves da Silva", "08/07/1970"),
    ("Aniversário", "Alexandre de Oliveira Silva", "16/11/1977"),
    ("Aniversário", "Rafaela Lourenço de Paula de Souza", "24/07/1992"),
    ("Aniversário", "Aurimar Pereira Dias", "11/10/1962"),
    ("Aniversário", "Josiel da Costa Silva", "17/07/1975"),
    ("Aniversário", "Rodrigo Sousa de Andrade", "26/03/1991"),
    ("Aniversário", "Wellington Martins", "17/11/1982"),
    ("Aniversário", "Renato Oliveira de Barros", "23/11/1989"),
    ("Aniversário", "Kaique Durce", "27/07/1998"),
    ("Aniversário", "Ailton Olivio da Silva Junior", "28/11/1993"),
    ("Aniversário", "TESTE Ailton Olivio da Silva Junior", "12/01/1993"),

    # 💍 Casamentos
    ("Casamento", "Sidney Martins Ferreira", "14/02/1993"),
    ("Casamento", "Gilson Alves da Silva", "22/05/1993"),
    ("Casamento", "Alexandre de Oliveira Silva", "20/01/2003"),
    ("Casamento", "Rafaela Lourenço de Paula de Souza", "29/07/2020"),
    ("Casamento", "Aurimar Pereira Dias", "05/05/2015"),
    ("Casamento", "Josiel da Costa Silva", "14/06/1996"),
    ("Casamento", "Rodrigo Sousa de Andrade", "27/10/2020"),
    ("Casamento", "Wellington Martins", "21/08/2009"),
    ("Casamento", "Renato Oliveira de Barros", "23/06/2015"),
    ("Casamento", "Kaique Durce", "05/04/2024"),
    ("Casamento", "Ailton Olivio da Silva Junior", "30/11/2018"),
]

alertados = set()
ultimo_dia = datetime.now().date()

print("🔔📲 Monitor de datas importantes iniciado...")

while True:
    agora = datetime.now()
    hoje = agora.date()
    amanha = hoje + timedelta(days=1)

    # 🔄 virou o dia
    if hoje != ultimo_dia:
        alertados.clear()
        ultimo_dia = hoje

    for tipo, nome, data_str in eventos:
        data_evento = datetime.strptime(data_str, "%d/%m/%Y")
        evento_ano = data_evento.replace(year=agora.year)

        # 📌 1 DIA ANTES
        if evento_ano.date() == amanha:
            chave = f"{tipo}-{nome}-amanha"

            if chave not in alertados:
                texto = f"📌 *Lembrete*\nAmanhã é {tipo.lower()} de *{nome}*."

                # 🖥 Notificação local
                notification.notify(
                    title=f"{tipo} Amanhã!",
                    message=texto,
                    timeout=0
                )

                # 📲 WhatsApp (grupo)
                pywhatkit.sendwhatmsg_to_group_instantly(
                    GRUPO_WHATSAPP,
                    texto,
                    wait_time=15,
                    tab_close=True
                )

                alertados.add(chave)

        # 🎉 NO DIA
        if evento_ano.date() == hoje:
            chave = f"{tipo}-{nome}-hoje"

            if chave not in alertados:
                if tipo == "Aniversário":
                    idade = agora.year - data_evento.year
                    texto = f"🎉 *Hoje é aniversário!*\n*{nome}* completa *{idade} anos* 🎂"
                else:
                    anos = agora.year - data_evento.year
                    texto = f"💍 *Hoje é aniversário de casamento!*\n*{nome}* – *{anos} anos*"

                # 🖥 Notificação local
                notification.notify(
                    title=f"{tipo} Hoje!",
                    message=texto,
                    timeout=0
                )

                # 📲 WhatsApp (grupo)
                pywhatkit.sendwhatmsg_to_group_instantly(
                    GRUPO_WHATSAPP,
                    texto,
                    wait_time=30,
                    tab_close=False
                )


                alertados.add(chave)

    time.sleep(60)
