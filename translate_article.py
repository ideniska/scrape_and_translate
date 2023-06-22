import os
from os import getenv
from dotenv import load_dotenv
import requests
import openai

load_dotenv()
openai.api_key = getenv("OPENAI_KEY")


def translate_and_save(title, file_path):
    print("Tratranslate_and_save started")
    with open(file_path, "r") as file:
        article_content = file.read()

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate this into Russian:\n\n{article_content}\n\n1.",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    output_directory = "translated"
    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, f"{title}.txt")
    translated_article = response["choices"][0]["text"]
    print(f"{translated_article=}")

    with open(output_path, "w") as file:
        file.write(translated_article)

    print("Translated!")
