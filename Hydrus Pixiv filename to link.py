import re

with open('input.txt', 'r', encoding='utf-8') as f_in, \
     open('output.txt', 'w', encoding='utf-8') as f_out:
    
    for line in f_in:
        # Ищем число перед _p0 в конце строки\Searching numbers before _p0 at the end of the string
        match = re.search(r'(\d+)_p\d+$', line)
        if match:
            f_out.write(f"https://www.pixiv.net/en/artworks/{match.group(1)}\n")

