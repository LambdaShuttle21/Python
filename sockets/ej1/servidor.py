import socket
import random
import threading

#socket = enchufe

def conexion():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#conexión fiable, como WhatsApp, no como UDP que es más “telegrama”)
        server_socket.bind(("0.0.0.0", 8082))#bind enchufa servidor_socket con una direccion IP y a un puerto especifico (8082)
        server_socket.listen(5)#el server se pone en modo escucha y defines cuantos pueden escucharlo al mismo tiempo (clientes)
        print("Servidor conectado en 0.0.0.0:8082...")

        while True:#empieza a escuchar...
            conn, addr = server_socket.accept()#conn = el socket especifico para hablar con ese cliente #addr = direccion del cliente, IP y puerto
            print(f"Conectado con {addr}")
            hilo = threading.Thread(target=game, args=(conn, addr))#Creas un hilo para el juego de adivinar al que le pasas el enchufe (metodos de socket)
            #y la direccion IP con el puerto del cliente
            hilo.start()
    except socket.error as e:
        print(e)
    finally:
        server_socket.close()

def game(conn, addr):
    random_num = random.randint(1, 10)#cada cliente tiene su propia partida (hilo)
    while True:
        print("Ingresa un numero del 1 al 10: ")
        data = conn.recv(1024)#recibe hasta 1024 bytes del socket del cliente 
        num = data.decode()#decodifica esos bytes a string y para compararlos con random, hacemos un cast a de string a int
        if (int(num) == random_num):#si acierta...
            print(f"Has acertado, el numero era {random_num}")
            conn.sendall(b"0")#se envia "0" al cliente y se rompe el bucle
            break
        elif (int(num) < random_num):#si es mayor se le envia 1 
            print("El numero es mayor")
            conn.sendall(b"1")
        else:#si es menor se le envia -1
            print("El numero es menor")
            conn.sendall(b"-1")

#El servidor puede tener varios clientes jugando a la vez, cada uno en su hilo game
conexion()