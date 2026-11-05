import socket


def send_data(client, data):
    """
    the func send to the client data from server and length
    :param client: where to send
    :param data:the data to send
    :return:none
    """
    if type(data) == str:
        data = data.encode()
    try:
        client.send(data)
    except Exception as e:
        print(f"error in recv/send try again {str(e)}")


my_sock = socket.socket()

ip_to_host = {"1.1.1.1":"king", "2.2.2.2":"loser", "3.3.3.3":"my server"}

msg = "choose:\n1 - to get 1.1.1.1 ip host name\n2 - to get 2.2.2.2 ip host name\n3 - to get 3.3.3.3 ip host name\n4 - to get 4.4.4.4 ip host name\n5 - to get the ip of server - 'king'\n6 - to get ip of server - 'loser'\n7 - to get ip of server - 'my server'\n8 - to get ip of server - 'blabla'\n9 - exit:\nchoose: "

try:
    my_sock.connect(("127.0.0.1", 53))
except Exception as e:
    print(f"server is down - {str(e)}")

while True:
    data = input(msg)


    if data == "1":
        data  = "1.1.1.1"
    elif data == "2":
        data = "2.2.2.2"
    elif data == "3":
        data = "3.3.3.3"
    elif data == "4":
        data = "4.4.4.4"
    elif data == "5":
        data = "king"
    elif data == "6":
        data = "loser"
    elif data == "7":
        data = "my server"
    elif data == "8":
        data = "blabla"
    elif data == "9":
        break

    found = False
    for key, value in ip_to_host.items():
        if key == data:
            print(value)
            found = True
            break
        elif value == data:
            print(key)
            found = True
            break

    if found:
        continue

    try:
        send_data(my_sock, data)
        data_recv_len = int(my_sock.recv(2).decode())
        data_recv = my_sock.recv(data_recv_len).decode()
        print(data_recv)
        continue
    except Exception as e:
        my_sock.close()
        print(f"server is down - try again {str(e)}" )
        continue



print("bye bye")
my_sock.close()



