import json
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Load the input JSON file
with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translate the strings that have :num
for item in data:
    if ':num' in item['string']:
        words = item['string'].split()
        for i, word in enumerate(words):
            if word == ':num':
                translated_word = translator.translate(words[i + 1], dest="ru").text
                item['string'] = item['string'].replace(words[i + 1], translated_word)

# Write the translated data to a new JSON file
with open('output_final.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
