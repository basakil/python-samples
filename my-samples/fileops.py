

def write_text(filename, text):
    with open(filename, 'w') as opened_file:
        opened_file.write(text)


def read_text(filename, text):
    with open(filename, 'r') as opened_file:
        lines = opened_file.readlines()
    return lines


if __name__ == '__main__':
    text_global = '''export STAGE=PROD
export TABLE_ID=token-storage-1234'''
    write_text('tempfile.txt', text_global)
    rt = read_text('tempfile.txt', text_global)
    print(f'\r\nread file as:\r\n{rt}')

    import pathlib

    path = pathlib.Path('tempfile.txt')
    path.write_text(text_global + '\r\n17')
    rt = path.read_text()
    print(f'\r\nread with pathlib as:\r\n{rt}')
