import os
import time

def padre():
    introduceNum = input("Introduce cuantos procesos hijos quieres: ")
    respuesta = int(introduceNum)

    for x in range(respuesta):
        newPid = os.fork()
        if newPid == 0:
            hijo()

        
def hijo():
    print("PID del hijo: %d" % os.getpid(), "creado")
    time.sleep(5)
    print("\nHijo con PID: %d terminado " % os.getpid())
    os._exit(0)

if __name__ == "__main__":
    padre()