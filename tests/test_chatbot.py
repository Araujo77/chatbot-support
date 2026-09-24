from src.chatbot import ChatBot

def test_greeting():
    bot = ChatBot()
    assert "Olá" in bot.respond("olá")

def test_hours():
    bot = ChatBot()
    assert "segunda a sexta" in bot.respond("Quais são os horários de atendimento?")
