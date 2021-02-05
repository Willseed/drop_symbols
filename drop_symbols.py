import re
import os

def replace_items_symbol(text: str) -> str:
    regex = re.compile(r'^.*([(|（].[)|）]).*$')
    try:
        inside_item = regex.match(text).group(1)
        return text.replace(inside_item, '')
    except AttributeError:
        return text

def get_xml_text(xml_file_path: str) -> list:
    result = []
    with open(xml_file_path, 'r', encoding='utf-8') as f:
        for i in  f.readlines():
            result.append(i)
    return result

def list_files() -> list:
    paths = []
    for root, dirs, files in os.walk(dir_path):
        if len(files) >= 2:
            set_output_path(output_path)
        for file in files:
            if file.lower().endswith('.di'):
                paths.append(os.path.join(root, file))
    return paths

def set_output_path(output_path: str):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

def exectue_drop(root: str, destination: str):
    text = get_xml_text(root)
    for line in text:
        result = replace_items_symbol(line)
        with open(destination, 'a', encoding='utf-8') as f:
            f.write(result)

dir_path = os.path.dirname(os.path.realpath(__file__))
output_path = os.path.join(dir_path, 'output')
for file in list_files():
    filename = file.replace(dir_path, '').replace('\\', '')
    final_path = os.path.join(output_path, filename)
    exectue_drop(file, final_path)
