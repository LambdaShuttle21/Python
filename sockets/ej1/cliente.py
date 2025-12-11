import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(("127.0.0.1", 8082))
    
    while True:
        num = input("Ingresa un numero entre 1 y 10: ")
        client_socket.sendall(num.encode())
        data = client_socket.recv(1024)
        b = int(data.decode())
        if (b == 0):
            print("Has acertado")
            break
        elif (b == 1):
            print("El numero es mayor")
        else:
            print("El numero es menor")
except socket.error as e:
    print(f"Excepcion de socket: {e}")
finally:
    client_socket.close()