import re
from operator import itemgetter

def parse():
    data = []
    with open('sample_log.txt', 'r') as file:
        line = next(file)
        while line:
            _old = re.search(r"Old=(\d*\.\d+)", line)
            _new = re.search(r"New=(\d*\.\d+)", line)
            _time =re.search(r"T(\d*\:\d+\:\d+\.\d+)",line)
            if _old and _new and _time:
                data.append((_time.group(1), float(_old.group(1))))
                data.append((_time.group(1), float(_new.group(1))))
            line = next(file, None)
        data.sort(key=itemgetter(1))
        __ave = sum(x[1] for x in data) / len(data)
        return data, __ave

if __name__ == '__main__':
     data,__ave = parse()
     last = len(data) - 1
     middle = int(len(data) /2)
     print ("Average Stream rate: %f(MBps)" % __ave )
     print ("Min Stream rate: %f(MBps)" % data[0][1], "Time: %sZ" % data[0][0])
     print ("Max Stream rate: %f(MBps)" % data[last][1], "Time: %sZ" % data[last][0])
     print ("Middle Stream rate: %f(MPps)" % data[middle][1] , "Time: %sZ" % data[middle][0])