import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#enchufe del cliente pa conectar al servidor, SOCK_STREAM = TCP

try:
    client_socket.connect(("127.0.0.1", 8082))#conectamos el cliente al servidor (0.0.0.0) en el server le permite al cliente conectarse por localhost (127.0.0.1)
    
    while True:#loop infinito 
        num = input("Ingresa un numero entre 1 y 10: ")
        client_socket.sendall(num.encode())#codigica el numero que metio el cliente para que el server lo pueda leer, y con el sendall se lo manda al servidor
        data = client_socket.recv(1024)#recv espera la respuesta del servidor (leeme hasta 1024 bytes que me pueda mandar el servidor)
        b = int(data.decode())#decodificamos data con decode y casteamos a int porque el decode nos devolvio un string, lo guardamos
        if (b == 0):#aca el servidor envia 0, 1 o -1 y eso nos dice si acertamos o no, al acertar se rompe el bucle
            print("Has acertado")
            break
        elif (b == 1):
            print("El numero es mayor")
        else:
            print("El numero es menor")
except socket.error as e:
    print(f"Excepcion de socket: {e}")
finally:
    client_socket.close()#se cierra en encufe o conexion del cliente