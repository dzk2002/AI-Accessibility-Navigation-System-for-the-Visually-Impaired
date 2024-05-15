from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, dest='en')
    return translated.text

# Test the translation method
text_to_translate = "你好，这是一个测试。"
translated_text = translate_text(text_to_translate)
print("Translated text:", translated_text)