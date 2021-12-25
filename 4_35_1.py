import threading





class Counter(threading.Thread):

    counter = 0
    rounds = 100000

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None, lock=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon, args=args, kwargs=kwargs)

        self.res = None
        self.args = args
        self.lock = lock

    def run(self):
        x = 0
        # self.lock.acquire()
        for _ in range(self.__class__.rounds):

            self.__class__.counter += 1
            x += 1
        # self.lock.release()
        return x

    def join(self, timeout=None):
        super().join(timeout)
        return self.res


lock = threading.Lock()

threads = []
for i in range(2):
    thr = Counter(name=f"Thread-{i}", lock=lock)
    threads.append(thr)
    thr.start()

for thr_ in threads:
    print(thr_.join())


print(Counter.counter)
