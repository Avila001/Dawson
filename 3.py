# put your python code here
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу


def remove_sym(chars=" !?"):
    def decorator(func):
        def remove_add_sym(*args, **kwargs):
            s = func(*args, **kwargs)
            s = ''.join(['-' if i in chars else i for i in s])
            while '--' in s:
                s = s.replace('--', '-')
            return s.lstrip('-').rstrip(' ')
        return remove_add_sym
    return decorator


@remove_sym(chars="?!:;,. ")
def translation(s):
    s = s.lower()
    s = ''.join([t.get(i, i) for i in s])
    # s = ''.join([t[i] if i in t else i for i in s])
    return s


s = ' э программа Декоратghfghоры - это круто!!..:  !   '
print(translation(s))
