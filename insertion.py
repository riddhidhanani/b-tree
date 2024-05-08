#python program for B treesa
class BTree:
    def __init__(self):
        #node declartion
        self.d = [0] * 6
        self.child_ptr = [None] * 7
        self.l = True
        self.n = 0

#creation of node
def init():
    np = BTree()
    np.l = True
    np.n = 0
    return np

#traverse the tree 
def traverse(p):
    if p is not None:
        for i in range(p.n):
            if not p.l:
                traverse(p.child_ptr[i])
            print(p.d[i], end=" ")
        if not p.l:
            traverse(p.child_ptr[p.n])
 #sort the tree   
def sort(p, n):
    for i in range(n):
        for j in range(i, n+1):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]

def split_child(x, i):
    np3 = init()
    #create new node
    np3.l = True
    if i == -1:
        mid = x.d[2]
        #find mid
        x.d[2] = 0
        x.n -= 1
        np1 = init()
        np1.l = False
        x.l = True
        for j in range(3, 6):
            np3.d[j-3] = x.d[j]
            np3.child_ptr[j-3] = x.child_ptr[j]
            np3.n += 1
            x.d[j] = 0
            x.n -= 1
        for j in range(6):
            x.child_ptr[j] = None
        np1.d[0] = mid
        np1.child_ptr[np1.n] = x
        np1.child_ptr[np1.n + 1] = np3
        np1.n += 1
        return np1
    else:
        y = x.child_ptr[i]
        mid = y.d[2]
        y.d[2] = 0
        y.n -= 1
        for j in range(3, 6):
            np3.d[j-3] = y.d[j]
            np3.n += 1
            y.d[j] = 0
            y.n -= 1
        x.child_ptr[i + 1] = y
        x.child_ptr[i + 1] = np3
    return mid

def insert(a):
    global r, x
    if r is None:
        r = init()
        x = r
    else:
        if x.l and x.n == 6:
            t = split_child(x, -1)
            x = r
            for i in range(x.n):
                if a > x.d[i] and a < x.d[i + 1]:
                    i += 1
                    break
                elif a < x.d[0]:
                    break
                else:
                    continue
            x = x.child_ptr[i]
        else:
            while not x.l:
                for i in range(x.n):
                    if a > x.d[i] and a < x.d[i + 1]:
                        i += 1
                        break
                    elif a < x.d[0]:
                        break
                    else:
                        continue
                if x.child_ptr[i].n == 6:
                    t = split_child(x, i)
                    x.d[x.n] = t
                    x.n += 1
                    continue
                else:
                    x = x.child_ptr[i]
    x.d[x.n] = a
    sort(x.d, x.n)
    x.n += 1
if __name__ == '__main__':
    r = None
    x = None
    insert(90)
    insert(20)
    insert(60)
    insert(40)
    insert(50)
    print("Insertion Done")
    print("B tree:")
    traverse(r)