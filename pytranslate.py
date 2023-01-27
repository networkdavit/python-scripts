from googletrans import Translator
import json

def translate_json(json_file, target_language):
    with open(json_file) as json_data:
        data = json.load(json_data)
    translated_data = {}
    translator = Translator()
    keys = list(data.keys())
    translations = translator.translate(keys, dest=target_language)
    for key, translation in zip(keys, translations):
        translated_data[key] = translation.text
    with open(f'{target_language}.json', 'w', encoding='utf-8') as outfile:
        json.dump(translated_data, outfile, ensure_ascii=False)

translate_json('keyspartone.json', 'ru')