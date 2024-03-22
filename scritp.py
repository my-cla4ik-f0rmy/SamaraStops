import re

def replace_street_names(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Паттерн для поиска улиц внутри тегов <title>
    pattern = r'<title>\s*ул\.\s+(.*?)\s*</title>'
    
    # Функция замены текста
    def replace(match):
        street_name = match.group(1)
        new_street_name = street_name.replace("ул. ", "Улица ")  # Заменяем "ул. " на пустую строку
        return f'<title>{new_street_name}</title>'
    
    # Замена текста с использованием регулярного выражения
    new_content = re.sub(pattern, replace, content)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Пример использования
replace_street_names("stopsFullDB.xml")
