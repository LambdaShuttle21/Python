import os

def hijo():
    print(f"Hola soy el proceso hijo con pid {os.getpid()} y mi padre tiene pid {os.getppid()}")
    os._exit(0)

def padre():
    while True:
        newpid = os.fork()
        if newpid == 0:
            hijo()
        else:
            print(f"Hola, soy padre con pid {os.getpid()} y el hijo tiene pid {newpid}")
            res = input("Otros hijos?")
            if res != "s":
                break

padre()