from threading import Thread

counter = 0

def increment_thread():
    global counter
    for i in range(100000):
        counter += 1

def decrement_thread():
    global counter
    for i in range(100000):
        counter -= 1

thread1 = Thread(target=increment_thread)
thread2 = Thread(target=decrement_thread)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Counter: ", counter)