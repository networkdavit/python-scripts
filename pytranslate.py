from googletrans import Translator
import json
def translate_json(json_file, target_language):
    with open(json_file) as json_data:
        data = json.load(json_data)
        print(data)
    translated_data = {}
    translator = Translator()
    for key in data:
        print(key)
        translation = translator.translate(key, dest=target_language)
        print(translation.text)
        translated_data[key] = translation.text
    with open(f'{target_language}.json', 'w', encoding='utf-8') as outfile:
        json.dump(translated_data, outfile, ensure_ascii=False)
translate_json('file.json', 'ru')
