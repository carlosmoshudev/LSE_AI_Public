# src/translator.py

import openai
import time
import json
import logging

MAX_RETRIES = 5
CHUNK_SIZE = 1024
CHAT_GPT_MODEL = 'gpt-3.5-turbo'
CHAT_GPT_SYSTEM = ' '

class Translator:
    def __init__(self, config_path):
        with open(config_path) as config_file:
            self.config = json.load(config_file)
        openai.api_key = self.config['Auth']['OPENAI']

    def translate(self, input_text):
        current_retry = 0
        while current_retry < MAX_RETRIES:
            try:
                response = openai.ChatCompletion.create(
                    model=CHAT_GPT_MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": CHAT_GPT_SYSTEM
                        },
                        {
                            "role": "user",
                            "content": input_text
                        }
                    ]
                )
                print(response)
                return response.choices[0].message.content
            except Exception as e:
                logging.exception("Error while trying to translate text.")
                current_retry += 1
                time.sleep(1)

        raise RuntimeError("Maximum number of retries exceeded.")
