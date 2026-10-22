# D1
class Record:
    def __init__(self, label, value, limit):
       self.label = label
       self.value = value
       self.limit = limit

r1=Record("R-001",87.0,100.0)
print(r1.label)
print(r1.value)
print(r1.limit)


# D2
r2=Record("R-002",120.0,100.0)
r1.value=95.0
print(r1.value)
print(r2.value)


# D3
record_dict={"label":"R-001","value": 87.0}
record_obj=Record("R-001",87.0,100.0)
#get label from dictionary
print(record_dict["label"])
#get label from object
print(record_obj.label)

# D4
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.label)


# D5
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    # add your summary method here
    def summary(self):

        return f"{self.label}: {self.value}/{self.limit}"

r = Record("R-001", 87.0, 100)
print(r.summary())



# D6
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def summary(self):
        return f"{self.label}{self.value}/{self.limit}"

        def status(self):
            percentage = (self.value / self.limit)*100

            if percentage <=100:
                return "OVERLIMIT"
            elif percentage >=90:
                return "WARNING"
            else:
                return "OK"

        r1 = Record("R-001", 87.0, 100.0)
        R2 = Record("R-002", 95.0, 100.0)
        r3 = Record("R-003", 120.0, 100.0)

        print(r1.status())
        print(r2.status())
        print(r3.status())


        # D7
def percent(self):
    return(self.value/self.limit)*100

def status(self):
    if self.percent() >=100:
        return "OVERLIMIT"
    elif self.percent() >=90:
        return "WARNING"
    else:
        return "OK"

    r = Record("R-001", 87.0, 100.0)

    print(r.percent())
    print(r.status())


    # D8
class Checker:
    def__init__(self):
    self.over_limit_count= 0
    self.over_limit_count += 1


     # D9
records =[Record("R-001", 87.0, 100.0),
          Record("R-002", 130.0, 100.0),
          Record("R-003", 45.0, 100.0)
          ]

for r in records:
    print(r.label,r.status())


    # D10
class counted:
    count = 0

    def __init__(self):
        counted.count += 1

c1 = counted()
c2 = counted()
c3 = counted()

print(counted.count)


# D11
def load_record(path):
    records = []
    with open (path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            r = Record(label, float(value), float(limit))
            records.append(r)
            return records
        records = load_record("records.txt")
        for r in records:
            print(r.label, r.status())


            # C1
def is_over(self):
    return self.value > self.limit


# C2
fail(self) print (anna.locked())
print (ben.ocked())


