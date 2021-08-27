import re
import fire

total_size = 0
arr = set()

class Log():
    def parse_access_log(self, filename): ##changed name and signature
        with open(filename) as FileObj:
            for lines in FileObj:
                HOST = r'^(?P<host>.*?)'
                SPACE = r'\s'
                IDENTITY = r'\S+'
                USER = r'\S+'
                TIME = r'(?P<time>\[.*?\])'
                REQUEST = r'\"(?P<request>.*?)\"'
                STATUS = r'(?P<status>\d{3})'
                SIZE = r'(?P<size>\S+)'
                REGEX = HOST + SPACE + IDENTITY + SPACE + USER + SPACE + TIME + SPACE + REQUEST + SPACE + STATUS + SPACE + SIZE + SPACE

                m = re.search(REGEX, lines)
                ip = m.group('host')
                time = m.group('time')
                request = m.group('request')
                status = m.group('status')
                size = m.group('size')
                global total_size
                total_size += (int)(size)

                if status != 200:
                    splitted_request = request.split(' ')
                    name = splitted_request[1]
                    arr.add(name)

        print(total_size)

        for i in arr:
            print(i)

if __name__ == '__main__':
    fire.Fire(Log)
