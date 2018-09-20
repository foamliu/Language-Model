from os import walk

from os.path import join


def cleanse(content):
    content = content.replace('\u3000', '')
    return content


def load_file(folder):
    paths = [join(dirpath, name)
             for dirpath, dirs, files in walk(folder)
             for name in files
             if not name.startswith('.')]
    concat = ''
    for path in paths:
        with open(path, 'r', encoding='utf-8') as myfile:
            # print(path)
            content = myfile.read()
            concat += cleanse(content)

    return concat


if __name__ == '__main__':
    folder = 'data/《刘慈欣作品全集》(v1.0)'
    concat = load_file(folder)
    print(concat[20000:20000 + 100])
    print("Full text length %d" % len(concat))

    with open('data/liucixin.txt', 'w', encoding='utf-8') as file:
        file.write(concat)
