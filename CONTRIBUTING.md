
**src/chatbot.py**
```python
class ChatBot:
    def __init__(self):
        self.responses = {
            "olá": "Olá! Como posso ajudar você hoje?",
            "horários de atendimento": "Nosso suporte funciona de segunda a sexta, das 9h às 18h.",
            "contato": "Você pode nos enviar um e-mail para suporte@empresa.com."
        }

    def respond(self, message: str) -> str:
        message = message.lower()
        for key, response in self.responses.items():
            if key in message:
                return response
        return "Desculpe, não entendi sua pergunta. Pode reformular?"
