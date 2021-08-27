import fire
import re


class LogParser():
    def parse_access_log(self, log_path):

        byteTotal = 0
        addresses = set()
        regex = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
        regex += r' - - \[.+\] "(\S+) (?P<ADDRESS>\S*)\s*(\S+)?\s*"'
        regex += r' (?P<CODE>\d{3})'
        regex += r' (?P<BYTE>\S+) ".+" ".+"'

        with open(log_path) as logfile:
            for line in logfile:
                match = re.search(regex, line)
                byteTotal += int(match.group('BYTE'))
                code = int(match.group('CODE'))
                if code >= 400:
                    addresses.add(match.group('ADDRESS'))

        print(byteTotal)
        for address in addresses:
            print(address)


if __name__ == '__main__':

    fire.Fire(LogParser)
