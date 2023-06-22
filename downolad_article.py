import requests
from bs4 import BeautifulSoup
import os


def download_medium_article(url):
    directory = "articles"  # Updated directory path

    # Send a GET request to the Medium article URL
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the article title
    title = soup.find("h1").text.strip()

    # Find all paragraphs and headings within the article
    paragraphs = soup.find("article").find_all(["p", "h2", "h3"])

    # Remove specific paragraphs by excluding them while constructing the content string
    excluded_paragraphs = [1, 2, 3, 4, 5]  # Indices of the paragraphs to remove
    content = ""
    for i, element in enumerate(paragraphs):
        if i not in excluded_paragraphs:
            if element.name == "p":
                content += element.text.strip() + "\n\n"
            else:  # Handle headings
                content += f"\n{element.text.strip()}\n\n"

    # Remove the unwanted phrase and everything after it
    target_phrase = "Medium: Follow us here!"
    if target_phrase in content:
        content = content.split(target_phrase)[0]

    # Print the modified article
    # print(f"Title: {title}")
    # print("-------------------------------------------------")
    # print(content)
    # print("-------------------------------------------------")

    # Save the modified article to a text file
    filepath = f"{directory}/{title}.txt"  # Updated filename path
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    return [title, filepath]
