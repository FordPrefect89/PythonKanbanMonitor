#!/usr/bin/python

class CurrentStatus:

    def SlotStatus(self, rangeInfo):
        """ This determines if the slot is empty or full depending on the range gate """
        if rangeInfo >= 3 and rangeInfo <=10:
            """ Full Slot """
            status = 1
            return status
        else:
            """ Empty Slot """
            status = 0
            return status
