import requests

codechefs_languages_map = dict()
geeksforgeeks_languages_map = dict()
leetcodes_languages_map = dict()
# geeksforgeeks_supported_languages = ["Python", "Python3", "Cpp", "Cpp14", "Java", "Csharp", "C", "Php", "Scala", "Perl"]

geeksforgeeks_languages_map = dict()
# input => data_input , lang = cpp ,typed_code <= sourcecode

# leetcodes_supported_languages = ["cpp", "java", "python", "python3", "c", "csharp", "javascript", "ruby", "swift", "kotlin", "scala", "bash", "go"]

supported_languages = dict()
supported_languages_extension = dict()


def set_codechefs_languages_mapping(id, lang_code):
    """
        codechef uses lang_code for languages to identify which interpreter/compiler to use
    """
    codechefs_languages_map[id] = lang_code


def set_geeksforgeeks_language_mapping(id, geekslang):
    geeksforgeeks_languages_map[id] = geekslang
    # geeksforgeeks_languages_map.update(map(id, geekslang))


def set_leetcodes_language_mapping(id, leetslang):
    leetcodes_languages_map[id] = leetslang
    # leetcodes_languages_map.update(map(id, leetslang))


def load_supported_languages():
    """
        codeched has extensive range of languages so using it as base for all supported languages by ccr
    """
    response = requests.get('https://www.codechef.com/api/ide/undefined/languages/all').json()
    # response = response.json()
    id = 1
    for lang_code, payload in response['languages'].items():
        lang = "_".join(payload['full_name'].lower().split())
        supported_languages[lang] = id

        supported_languages_extension[payload['extension']] = id
        geekslang = leetslang = None
        if lang == 'cpp':
            geekslang = 'Cpp14'
            leetslang = 'cpp'
        elif lang == 'java':
            geekslang = 'Java'
            leetslang = 'java'
        # map codechef languages to other clients
        elif lang == 'python' or lang == 'python3' or lang == 'pypy':
            geekslang = "Python3"
            leetslang = "Python"
        elif lang == 'c':
            geekslang = 'C'
            leetslang = 'c'
        elif lang == 'c#':
            geekslang = 'Csharp'
            leetslang = 'csharp'
        elif lang == 'scala':
            geekslang = 'Scala'
            leetslang = 'scala'
        elif lang == 'php':
            geekslang = 'Php'
        elif lang == 'perl':
            geekslang = 'Perl'
        elif lang == 'go':
            leetslang = 'go'
        elif lang == 'swift':
            leetslang = 'swift'
        elif lang == 'ruby':
            leetslang = 'ruby'
        elif lang == 'kotlin':
            leetslang = 'kotlin'
        elif lang == 'bash':
            leetslang = 'bash'

        if geekslang:
            set_geeksforgeeks_language_mapping(id, geekslang)
        if leetslang:
            set_leetcodes_language_mapping(id, leetslang)
        set_codechefs_languages_mapping(id, payload['id'])

        id += 1


def get_id_from_file_extension(ext):
    try:
        return supported_languages_extension[ext]
    except KeyError:
        return None


load_supported_languages()

# print(supported_languages)
# print("******************")
# print(supported_languages_extension)
# print("******************")
# print(codechefs_languages_map)
# print("******************")
# print(geeksforgeeks_languages_map)
# print("******************")
# print(leetcodes_languages_map)
