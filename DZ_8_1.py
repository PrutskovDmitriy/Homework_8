import re


def email_parse(e_adress):
    parse = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = parse.findall(e_adress)
    if not result:
        raise ValueError(f'Электронный адрес недействителен: {e_adress}')
    return result


print(*email_parse('russo_mafia@mail.ru'))
