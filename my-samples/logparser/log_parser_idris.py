import sys
import re
import fire

arraynm = set()

size = 0
class Pal():
    def parse_access_log(self, file):
        f = open(file, 'r')
        for i in f:
            ip = r'^(?P<host>.*?)'
            bosluk = r'\s'
            idn = r'\S+'
            usr = r'\S+'
            time = r'(?P<time>\[.*?\])'
            request = r'\"(?P<request>.*?)\"'
            status = r'(?P<status>\d{3})'
            size = r'(?P<size>\S+)'
            regex = ip + bosluk + idn + bosluk + usr + bosluk + time + bosluk + request + bosluk + status + bosluk + size + bosluk
            rs = re.search(regex, i)
            request = rs.group('request')
            status = rs.group('status')
            size = rs.group('size')


            if status != 200:
                parsed = request.split(' ')
                name = parsed[1]
                arraynm.add(name)

        for j in arraynm:
            print(j)


if __name__ == '__main__':
    fire.Fire(Pal)







