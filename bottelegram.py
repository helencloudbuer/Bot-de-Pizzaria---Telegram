import os
import telebot

chave_api = os.environ["TELEGRAM_BOT_TOKEN"]

bot = telebot.TeleBot(chave_api)


@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo para entrega, o tempo de espera é no máximo 20 minutos.")


@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo para entrega, o tempo de espera é no máximo 20 minutos.")


@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo para entrega, o tempo de espera é no máximo 20 minutos.")


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você deseja? (clique apenas em uma das opções abaixo)
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.reply_to(mensagem, "Agradecemos pela reclamação ! ;)")


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.reply_to(mensagem, "Agradecemos pelo elogio <3")
    print(mensagem)


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    escolha uma opção para continuar ;) :
    /opcao1 Fazer pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um elogio <3
    Obs: responder qualquer coisa não vai funcionar, por isso, clique apenas em uma das opções amostradas
    """
    bot.reply_to(mensagem, texto)


bot.polling()