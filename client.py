import socket


def send_data(client, data_len_byte, data):
    """
    the func send to the client data from server and length
    :param client: where to send
    :param data:the data to send
    :return:none
    """
    if type(data) == str:
        data = data.encode()
    try:
      client.send(str(len(data)).zfill(data_len_byte).encode())
      client.send(data)
    except Exception as e:
        print(f"error in recv/send try again {str(e)}")



my_sock = socket.socket()

ip_to_host = {"1.1.1.1":"king"}

msg = "choose:\n1 - ip\n2 - domain\n9 - exit:\nchoose: "

while True:
    try:
        my_sock.connect(("127.0.0.1", 53))
    except Exception as e:
        print(f"server is down - {str(e)}")
        break

    while True:

        data = input(msg)

        if data == "1":
            data  = input("enter ip to search")
            parts = data.split(".")

            try:
                one = int(parts[0])
                two = int(parts[1])
                three = int(parts[2])
                four = int(parts[3])
            except Exception as e:
                print(f"error in casting - {str(e)}")
                print("not legal ip")
                continue

            if not (0 <= one < 256 and 0 <= two < 256 and 0 <= three < 256 and 0 <= four < 256) or len(parts) != 4:
                print("error in the ip try again")
                continue

        elif data == "2":
            data  = input("enter domain to search ")
        elif data == "9":
            break

        else:
            print("you chose something illegal try again")
            continue

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
            send_data(my_sock, 2, data)
            data_recv_len = int(my_sock.recv(2).decode())
            data_recv = my_sock.recv(data_recv_len).decode()
        except Exception as e:
            print(f"server is down - try again {str(e)}" )
            break

        print(data_recv)
        if not data_recv == "not exist":
            ip_to_host[data] = data_recv


    my_sock.close()
    print("bye bye")
    break





