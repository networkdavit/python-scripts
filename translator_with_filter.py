import json
from googletrans import Translator
import sys
import time


#part 1
def translator(input, output, dest_lang):
    # Read the input JSON file
    with open(input, "r") as f:
        data = json.load(f)

    translator = Translator()
    # Translate the "string" values that do not contain "_" or ":"
    strings_to_translate = [item["string"] for item in data if "_" not in item["string"] and ":" not in item["string"] and "DB" not in item["string"]]
    strings_to_translate = "\n".join(strings_to_translate)
    translated_strings = translator.translate(text=strings_to_translate, dest=dest_lang).text
    translated_strings = translated_strings.split("\n")

    # Split the translated string back into individual strings
    j = 0
    for i, item in enumerate(data):
        if "_" in item["string"] or ":" in item["string"] or "DB" in item["string"]:
            continue
        item["string"] = translated_strings[j]
        j += 1

    # Write the translated data to the output JSON file
    with open(output, "a",  encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, indent=2, ensure_ascii=False) + "," + '\n')


input_file = sys.argv[1]
input_files = []

output_file = sys.argv[2]
output_files = []

lang = sys.argv[3]

with open(f"{output_file}.json", "w+",  encoding='utf-8') as f:
    f.write("[" + "\n"  + "{")
    for i in range(5):
        input_files.append(f"{input_file}{i+1}.json")
        output_files.append(f"{output_file}{i+1}.json")
        translator(input_files[i], f"{output_file}.json", lang)
    f.seek(0, 0)
    data = f.read()
    data = data.rstrip(',\n') + '\n]'
    f.seek(0, 0)
    f.write(data)



#part 2
time.sleep(1)
def translate_key_values():
    translator = Translator()
    with open('output.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Translate the strings that have :num
    for item in data:
        if ':num' in item['string']:
            words = item['string'].split()
            for i, word in enumerate(words):
                if word == ':num':
                    translated_word = translator.translate(words[i + 1], dest=lang).text
                    item['string'] = item['string'].replace(words[i + 1], translated_word)

    # Write the translated data to a new JSON file
    with open(f'output_final_{lang}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        

translate_key_values()
