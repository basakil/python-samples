#!/usr/bin/env python

import re
# import pathlib
import fire


class LogParser:

    _access_log_re_str = r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.[01]")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])"""

    def __init__(self):
        self._access_log_re = re.compile(LogParser._access_log_re_str, re.IGNORECASE)

    def parse_access_log(self, log_path):
        ret = ''
        total_bytes = 0
        not_found = set()
        with open(log_path, 'r') as f:
            for line in f:
                res = re.match(self._access_log_re, line)
                if res:
                    statuscode = res.group('statuscode')
                    if statuscode.startswith('4'):
                        not_found.add(res.group('url'))
                    bytessent = res.group('bytessent')
                    total_bytes += int(bytessent)
                else:
                    print(f'regex did not match for line:\n {line}\n')
        ret = '' + str(total_bytes) + '\n' + '\n'.join(not_found) + '\n'
        return ret


if __name__ == '__main__':
    fire.Fire(LogParser)
