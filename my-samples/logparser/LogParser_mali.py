import re
import fire

class LogParser:

    def parse_access_log(log_path):
        totalBytes = 0
        erroredPaths  = []
        file = open(log_path, "r")
        for line in file:
            regEx =  r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
            regEx += r' - - '
            regEx += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) \+0000\]'
            regEx += r' "(?P<RequestType>\w+)'
            regEx += r' (?P<Path>/[a-zA-Z0-9\_\-\?\=\./]*[\s]?)'
            regEx += r' (?P<Protocol>\w+\/\d+\.\d+)"'
            regEx += r' (?P<StatusCode>\d+)'
            regEx += r' (?P<Bytes>\d+)'
            match = re.search(regEx, line)
            ip = match.group('IP')
            time = match.group('Time')
            requestType = match.group('RequestType')
            path = match.group('Path')
            protocol = match.group('Protocol')
            statusCode = match.group('StatusCode')
            bytes = match.group('Bytes')
            #print(f'ip = {ip}, time={time}, requestType={requestType}, path={path}, statusCode={statusCode}, bytes={bytes}')
            if(statusCode[0]=='4'):
                erroredPaths.append(path)
            totalBytes += int(bytes)
        print(totalBytes)
        for path in set(erroredPaths):
            print(path)
            
    if __name__ == '__main__':
        fire.Fire()

