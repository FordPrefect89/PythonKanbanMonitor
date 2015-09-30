#!/usr/bin/python

class FileWrite:

    def XMLWrite(self, one, two, three, four, five, six, seven, eight):
        """ This writes the XML file to the RAM drive to minimize hits to SD card """
        filePath = "/mnt/RAM/kanban.xml"
        xmlFile = open(filePath, 'w')
        
        xmlFile.write('<kanban>\n')
        xmlFile.write('     <n1>%s</n1>\n' % one)
        xmlFile.write('     <n2>%s</n2>\n' % two)
        xmlFile.write('     <n3>%s</n3>\n' % three)
        xmlFile.write('     <n4>%s</n4>\n' % four)
        xmlFile.write('     <n5>%s</n5>\n' % five)
        xmlFile.write('     <n6>%s</n6>\n' % six)
        xmlFile.write('     <n7>%s</n7>\n' % seven)
        xmlFile.write('     <n8>%s</n8>\n' % eight)
        xmlFile.write('</kanban>')
