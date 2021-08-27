import re

import fire

total_size = 0
arr = set()

def get_name(request):
    splitted_request = request.split(' ')
    name = splitted_request[1]
    if name != '/':
        arr.add(name)


def assign_variables(REGEX,line):
    m = re.search(REGEX, line)
    ip = m.group('host')
    time = m.group('time')
    request = m.group('request')
    status = m.group('status')
    size = m.group('size')
    global total_size

    total_size += (int)(size)

    if status != 200:
        get_name(request)
       # print(size)

def log_parser(line):
    HOST = r'^(?P<host>.*?)'
    SPACE = r'\s'
    IDENTITY = r'\S+'
    USER = r'\S+'
    TIME = r'(?P<time>\[.*?\])'
    REQUEST = r'\"(?P<request>.*?)\"'
    STATUS = r'(?P<status>\d{3})'
    SIZE = r'(?P<size>\S+)'
    REGEX = HOST + SPACE + IDENTITY + SPACE + USER + SPACE + TIME + SPACE + REQUEST + SPACE + STATUS + SPACE + SIZE + SPACE
    assign_variables(REGEX,line)

class LogParser:
    def parse_access_log(self, log_path):
        file = open('nas.log','r')
        for line in file:
            log_parser(line)

        print(total_size)

        for i in arr:
            print(i)





if __name__ == '__main__':
    fire.Fire(LogParser)

