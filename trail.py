import time 

def power(limit):
    return [x**2 for x in range(limit)]

start = time.time()

power(1000)

end = time.time()

print(end -start)


