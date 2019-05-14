nameIndex = 2
emailIndex = 1
fileIndex = 3
printerIndex = 4
colorIndex = 5
addIndex = 6
nickIndex = 8
statusIndex = 9
timeIndex = 0

class PrintRequest:
    time = ''
    name = ''
    email = ''
    fileUrl = ''
    printer = ''
    color = ''
    additional = ''
    nickname = ''
    status = ''
    row = 0

    def __init__(self, list, rowNum):
        self.time = list[timeIndex]
        self.email = list[emailIndex]
        self.name = list[nameIndex]
        self.fileUrl = list[fileIndex]
        self.printer = list[printerIndex]
        self.color = list[colorIndex]
        self.additional = list[addIndex]
        self.nickname = list[nickIndex]
        self.row = rowNum
        if (len(list) >= 10):
            self.status = list[statusIndex]
        else:
            self.status = '0'

    def __str__(self):
        return 'NAME: ' + self.name + ' PRINTER:' + self.printer + ' COLOR:' + self.color + ' ADDITIONAL:' + self.additional

    def __gt__(self, other):
        return self.time > other.time

    def __lt__(self, other):
        return self.time < other.time

    def __hash__(self):
        return hash(self.fileUrl)

    def __eq__(self, other):
        return self.fileUrl == other.fileUrl

    def __ne__(self, other):
        return self.fileUrl != other.fileUrl
