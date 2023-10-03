from translate import Translator
import random

def translate_paragraph(input_paragraph, target_language):
    try:
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(input_paragraph)

        return translated_text

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    file_path = "transcript.txt"

    with open(file_path, "r") as file:
        input_paragraph = file.read()

    target_languages = ["hi","bn","te","ta","pa","gu"]
    target_language = random.choice(target_languages)
    translated_text = translate_paragraph(input_paragraph, target_language)

    print(f"Original Paragraph (English):\n{input_paragraph}")
    print(f"Translated Paragraph ({target_language}):")

    output_file_path = "translated_text.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(translated_text)
        
    print(translated_text)
