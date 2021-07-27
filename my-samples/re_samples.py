#!/usr/bin/env python

import re

line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'
r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r' - (?P<User>\w+) '
r += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
r += r' (?P<Request>".+")'

m = re.search(r, line)

ip = m.group('IP')
user = m.group('User')
time = m.group('Time')
request = m.group('Request')

print(f'ip = {ip}, user={user}, time={time}, request={request}')