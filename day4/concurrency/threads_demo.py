from threading import Thread
import _thread as thread

def go():
    for i in range(10):
        print("Hi! I'm thread {id} counting {i}\n".format(
            id=thread.get_ident(),
            i=i), end='')

for _ in range(4):
    t = Thread(target=go)
    t.start()

threads = [Thread(target=go) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()