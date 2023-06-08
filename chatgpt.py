import openai


class GPT:
    def __init__(self, token):
        openai.api_key = token
        self.start = "###Ты вежливый голосовой помощник по имени Мерда, всегда отвечай от имени Мерда. " \
                     "Мерда это женщина помощник, всегда готовый ответить и помочь с любым вопросом. " \
                     "На вопросы как тебя зовут, отвечай: Мерда. Всегда отвечай очень коротко, по " \
                     "делу и ясно.### Моя следующая просьба для тебя: "

    def gpt_response(self, message: str):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=self.start + message,
                max_tokens=200,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
                temperature=0.8
            )
            text = response["choices"][0]['text'].replace("Мерда:", "")
            return text.split("\n", 1)[1] if "\n" in text else text
        except openai.error.RateLimitError:
            return "Токен прекратил свою работу, прошу замените его, чтобы продолжить работу."
