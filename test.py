import re

# Ваша строка с ссылкой
text = "https://www.youtube.com/watch?v=-7YzTaaPSpU"

# Регулярное выражение для поиска ссылок и параметров
pattern = r'(https:\/\/(?:youtu\.be\/|www\.youtube\.com\/watch\?v=)([A-Za-z0-9_-]+))(?:&[^ ]*)?'

# Функция для замены ссылок
def replace_link(match):
    video_id = match.group(2)
    print(video_id)
    return f'[MEDIA=youtube]{video_id}[/MEDIA]'

# Замена ссылок в тексте
result = re.sub(pattern, replace_link, text)

# Вывод результата
print(result)
