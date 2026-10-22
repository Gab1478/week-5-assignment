"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

class Record:
    def __init__(self, label, value, limit):
     self.label = label
     self.value = value
     self.limit = limit


# ==================================================================== RECORDS
r1 = Record("R=001", 87.0, 100.0)
r2 = Record("R-002", 95.0, 100.0)

print(r1.status())
print(r2.status())


# ==================================================================== OUTPUT


def print_report(r):
    print("=" * 34)
    print("Label:", r.label)
    print("Value:", r.value)
    print("Limit:", r.limit)
    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
