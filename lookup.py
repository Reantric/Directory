#LANG: PYTHON 3.6+

from itertools import zip_longest
from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt


def choose(fl, sl, o=True):
    if o:
        return len(fl) if len(fl) >= len(sl) else len(sl)
    return len(sl) if len(fl) >= len(sl) else len(fl)


class Storage:
    db = defaultdict(list)

    def __init__(self, name=None, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        Storage.di = list(zip_longest(self.name, self.age, self.location))
        for n, a, l in Storage.di:
            Storage.db[n].append([a, l])

    def lookup(self, name=None, age=None, loc=None):
        n = ''
        agelist = []
        loclist = []
        fL = []
        fLen = 0
        if name:
            n = Storage.db[name]

        if age:
            fLen += 1
            for i in Storage.db.items():
                for e in i[1]:
                    if e[0] == age:
                        agelist.append(i[0])

        if loc:
            fLen += 1
            for i in Storage.db.items():
                for e in i[1]:
                    if e[1] == loc:
                        loclist.append(i[0])

        if n:
            return f"Details for user(s) {name}: {n}"

        mL = loclist + agelist
        fL = Counter(mL)
        count = Counter(fL.values())
        mL = []
        if count and list(fL.most_common(max(count.most_common())[1]))[0][1] == fLen:
            for x in list(fL.most_common(max(count.most_common())[1])):
                if [name, age, loc].count(None) == 2:
                    return loclist if loclist else agelist
                if [age, loc] in Storage.db[x[0]]:
                    mL.append(x)

        return mL if mL else "Unable to find recipients"

    def graph(self):
        vA = []
        s = (list(Storage.db.values()))
        for x in range(len(Storage.db)):
            vA.append(s[x][0][0])
        print(vA)
        bins = [x for x in range(min(vA)-3,max(vA)+4)]
        plt.hist(vA,bins,histtype='bar',rwidth=0.8,label='People',color='g')
        plt.legend()
        plt.show()

    def __str__(self):
        return str(Storage.db)

    def __len__(self):
        return len(Storage.db)


names = ["Shreyas","Xavier", "Josh", "Bendy", "Aaron", "Eric", "Sanjit", "Aaron"]
ages = [99,15, 14, 14, 14, 15, 15, 420]
loc = ["Shreyville","Martinsville", None, "Raritan", "Bridgewater", "Bridgewater", "Bridgewater", "Ninety"]
st = Storage(names, ages, loc)
#print(st)
print(st.lookup(loc="Shreyville"))

#print(len(st)) not needed
#st.graph() not needed
