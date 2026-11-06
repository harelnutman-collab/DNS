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




def get_key(value_to_search, d):
    """
    the func get value and return the key
    :param value_to_search: the value
    :param d: the dict
    :return: the key of the value
    """
    key_to_search = None
    if type(value_to_search) == str and type(d) == dict:
        for key, value in d.items():
            if value == value_to_search:
                key_to_search = key
                break
    return key_to_search


server_sock_1 = socket.socket()
server_sock_1.bind(("0.0.0.0", 53))
server_sock_1.listen(3)

my_sock = socket.socket()
ip_to_host = {"1.1.1.1":"king", "2.2.2.2":"loser"}



while True:
    try:
        client_sock, addr = server_sock_1.accept()
        my_sock.connect(("127.0.0.1", 54))
        print(f"{addr[0]} - connected")
    except Exception as e:
        print(f"error in connect - {str(e)}")
        break

    while True:
        try:
            data_len = int(client_sock.recv(2).decode())
            data = client_sock.recv(data_len).decode()

        except Exception as e:
            print(f"error in recv {str(e)}")
            continue

        found = False

        if data in ip_to_host:
            data = str(ip_to_host[data])
            found = True
            print(data)

        elif get_key(data, ip_to_host) in ip_to_host:
            data = get_key(data, ip_to_host)
            found = True
            print(data)

        if found:
            try:
                send_data(client_sock, 2, data)
                continue
            except Exception as e:
                print(f"error in send - {str(e)}")
                continue
        else:
            try:
                send_data(my_sock, 2, data)
                new_data_len = int(my_sock.recv(2).decode())
                new_data = my_sock.recv(new_data_len).decode()
                send_data(client_sock, 2, new_data)
            except Exception as e:
                print(f"server is down - try again {str(e)}" )
                break

    my_sock.close()



