from itertools import zip_longest
from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from random import randint
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

rand = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes']

class Storage:
    db = defaultdict(list)
    vA = []
    def __init__(self, name=None, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        Storage.di = list(zip_longest(self.name, self.age, self.location))
        for n, a, l in Storage.di:
            Storage.db[n].append([a, l])
        s = (list(Storage.db.values()))
        for x in range(len(Storage.db)):
            Storage.vA.append(s[x][0][0])

    def lookup(self, name=None, age=None, loc=None):
        n = ''
        agelist = []
        loclist = []
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
            plt.figure("Graph 1")
            plt.title("Average age of individuals")
            bins = [x for x in range(min(Storage.vA)-3,max(Storage.vA)+4)]
            plt.hist(Storage.vA,bins,histtype='bar',rwidth=0.8,label='People',color='g')
            plt.legend()
            plt.show()
            return "Age graph"

    def mean(self,it=2):
        style.use("fivethirtyeight")
        fig = plt.figure("Lol")
        ax = fig.add_subplot(1,1,1)
        m = []
        dx = []
        Storage.addObject(self, it)
        for i in range(1,len(Storage.vA)):
            m += [sum(Storage.vA[:i]) / len(Storage.vA[:i])]
        x = np.linspace(1, it + len(ages), num=len(m))
        print(x)
        xnew = np.linspace(x.min(), x.max(), 300)
        print(len(x)); print(len(m))
        spl = make_interp_spline(x, m, k=3)
        dx = spl(xnew)
        def animate(i):
            ax.set_ylim(-0.2,5)
            ax.clear()
            ax.plot(xnew[:i],dx[:i])
            plt.xlabel("Amount of individuals added")
            plt.ylabel("Average age")
        ani = animation.FuncAnimation(fig,animate,interval=25, repeat=False,blit=False)


        plt.title("Database statistics")
        plt.show()
    def addObject(self,amt):
        for x in range(amt):
            names.append(rand[randint(0,99)])
            Storage.vA.append(randint(10,98))
    def __str__(self):
        return str(Storage.db)

    def __len__(self):
        return len(Storage.db)


names = ["Xavier", "Josh", "Bendy", "Aaron", "Eric", "Noah", "Aaron"]
ages = [15, 24, 34, 24, 15, 17]
loc = ["A", None, "B", "C", "D", "E", "F"]
st = Storage(names, ages, loc)
print(st)
print(st.lookup(loc="A", age=15))
print(len(st))
st.graph()
st.mean(20)
print(names)
print(ages)