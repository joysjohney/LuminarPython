from  threading import *
import  time
def display():
    for i in range(1,10):
        time.sleep(5)
        print("Child thread executing")
    print(current_thread().getName())

t=Thread(target=display) #creation of new thread
t.start()

for i in range(1, 10):
    time.sleep(5)
    print("Main thread executing")
print(current_thread().getName())
