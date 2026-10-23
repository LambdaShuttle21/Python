import os

# //El padre debe mostrar:

# PADRE -> PID: 5000
# PADRE -> He creado al hijo: 5001

# El hijo:

# HIJO -> PID: 5001
# HIJO -> Mi padre es: 5000

# El padre debe esperar a que termine el hijo antes de imprimir:

# PADRE -> El hijo ha terminado

# Necesitarás principalmente os.fork(), os.getpid(), os.getppid() y os.wait().

pid = os.fork()#0 al hijo y PID del hijo al padre
if pid == 0:
    pid_hijo = os.getpid()
    print(f"HIJO -> {pid_hijo}")
    print(f"HIJO -> Mi padre es: {os.getppid()}")
else:
    print(f"PADRE -> PID: ${os.getpid()}")
    print(f"PADRE -> He creado al hijo: {pid}")
    os.wait()#espera hijo
    print(f"PADRE -> El hijo ha terminado")

