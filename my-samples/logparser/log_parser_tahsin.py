import re
import time
import sys
import fire
from time import strftime
arraynm = set()

size = 0



class Pal():

    def parse_access_log(self, file):
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            ip = r'^(?P<host>.*?)'; space = r'\s'; x = r'\S+'; usr = r'\S+'; time = r'(?P<time>\[.*?\])'; request = r'\"(?P<request>.*?)\"'; status = r'(?P<status>\d{3})'; size = r'(?P<size>\S+)'
            regex = ip + space + x + space + usr + space + time + space + request + space + status + space + size + space
            rs = re.search(regex, line)
            request = rs.group('request')
            status = rs.group('status')
            size = rs.group('size')


            if status != 200:
                parsed = request.split(' ')
                name = parsed[1]
                arraynm.add(name)
        for line2 in arraynm:
            print(line2.split())

if __name__ == '__main__':
    fire.Fire(Pal)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
