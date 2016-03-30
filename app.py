from tasks import add

for x in range(10000):
    add.delay(x, x)
