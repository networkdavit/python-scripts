import json
from googletrans import Translator
import sys


def translator(input, output, dest_lang):
    # Read the input JSON file
    with open(input, "r") as f:
        data = json.load(f)

    # Concatenate all the "locale" values into a single string
    locales_to_translate = [item["locale"] for item in data]
    locales_to_translate = "\n".join(locales_to_translate)

    # Translate the concatenated "locale" values
    translator = Translator()
    translated_locales = translator.translate(text=locales_to_translate, dest=dest_lang).text
    translated_locales = translated_locales.split("\n")

    # Split the translated string back into individual strings
    j = 0
    for i, item in enumerate(data):
        item["locale"] = translated_locales[j]
        j += 1

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