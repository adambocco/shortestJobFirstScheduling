
class Process:
    n = 0
    def __init__(self, p,b,a):
        Process.n+=1
        self.p = p
        self.b = b
        self.a = a
        self.finish = None
        self.turn = None
        self.wait = None
        self.index = None

def sjn(a):
    time = 0
    returnDict = {}
    while True:
        arr = []
        for i in range(len(a)):
            if a[i].a <= time:
                a[i].index = i
                arr.append(a[i])
        try:
            shortest = a[0]
        except:
            break
        arr2 = []
        for i in arr:
            if i.b < shortest.b:
                shortest = i
        for i in arr:
            if i.b == shortest.b:
                arr2.append(i)
        if len(arr2) > 1:
            for i in arr2:
                if i.a < shortest.a:
                    shortest = i
        print("ProcessID: ", shortest.p)
        time+=shortest.b
        shortest.finish = time
        shortest.turn = shortest.finish - shortest.a
        shortest.wait = shortest.turn - shortest.b
        returnDict[shortest.p] = a.pop(shortest.index)
        print("FINISHED AT: ", time)
        print("\n")
    return returnDict
            



pid = [1,2,3,4,5,6,7,8,9,10]
burst = [100, 200, 50, 150, 100, 250, 300, 50, 400, 200]
arrival = [0, 10, 30, 40, 60, 90, 100, 120, 130, 140]
num=10

arr = []
for i in range(num):
    arr.append(Process(pid[i], burst[i], arrival[i]))

y = sjn(arr)
print("I       Arrival        Burst       W(Pi)       Turnaround")
for i in range(1,11):
    print(y[i].p, "        ", y[i].a, "         ", y[i].b, "       ", y[i].wait, "          ", y[i].turn)