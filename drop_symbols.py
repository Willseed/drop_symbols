import re

from bs4 import BeautifulSoup

def replace_items_symbol(text: str) -> str:
    regex = re.compile(r'^([(|（].*[)|）]).*$')
    try:
        insideItem = regex.match(text).group(1)
        return text.replace(insideItem, '')
    except AttributeError:
        return text

def get_xml_node_text(xml_file_path: str, node_name: str) -> list:
    with open(xml_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    soup = BeautifulSoup(text, 'lxml')
    return soup.find_all(node_name)

path = '<somefile.xml>'
elements = get_xml_node_text(path, 'text')
for element in elements:
    result = replace_items_symbol(element.text)
    print(result)

