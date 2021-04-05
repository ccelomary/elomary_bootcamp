import time

def     number_operation(l):
    old = time.time()
    t = 0
    for i in range(0, l + 1):
        yield i
        new = time.time() - old
        t = new * l
        c = int((i * 30) / l)
        print("\rETA: {:.2f}s [{:3d}%][".format(t, int((i * 100) / l)) + "[" + "=" * c + ">" + " " * (30 - c) +  "]" + "] {}/{} | elapsed time {:.2f}s".format(i, l, i * new), end="")
        old = time.time()
        i += 1
if __name__ == '__main__':
    for i in number_operation(50):
        time.sleep(1)
    print()