import json
from googletrans import Translator
import sys


def translator(input, output, dest_lang):
# The language to translate the input JSON to


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
        if "_" in item["string"] or ":" in item["string"]:
            continue
        item["string"] = translated_strings[j]
        j += 1

    # Write the translated data to the output JSON file
    with open(output, "w",  encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
input_file3 = sys.argv[3]
input_file4 = sys.argv[4]
input_files = [input_file1, input_file2, input_file3, input_file4]

output_file1 = sys.argv[5]
output_file2 = sys.argv[6]
output_file3 = sys.argv[7]
output_file4 = sys.argv[8]
output_files = [output_file1, output_file2, output_file3, output_file4]


lang = sys.argv[9]
for i in range(4):
    translator(input_files[i], output_files[i], lang)