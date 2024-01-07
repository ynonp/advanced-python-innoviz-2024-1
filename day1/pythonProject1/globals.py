g_total = 0

def show():
    print(g_total)


def add(val):
    global g_total
    g_total += int(val)

add(10)
add('20')
add(5)
show()
