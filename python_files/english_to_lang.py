from translate import Translator
import random

def translate_paragraph(input_paragraph, target_language):
    try:
        # Create a translator object
        translator = Translator(to_lang=target_language)

        # Translate the input paragraph
        translated_text = translator.translate(input_paragraph)

        return translated_text

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    input_paragraph = """This is an example paragraph that we want to translate into another language."""
    target_languages = ["hi","bn","te","ta","pa","gu"]  # Change to the desired target language code (e.g., "es" for Spanish)
    target_language = random.choice(target_languages)
    translated_text = translate_paragraph(input_paragraph, target_language)

    print(f"Original Paragraph (English):\n{input_paragraph}")
    print(f"Translated Paragraph ({target_language}):")

    output_file_path = "translated_text.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(translated_text)
        
    print(translated_text)
