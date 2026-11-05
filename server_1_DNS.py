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
    key_to_search = ""
    if type(value_to_search) == str and type(d) == dict:
        found = False
        for key, value in d.items() and not found:
            if value == value_to_search:
                key_to_search = key
                found = True
                break
        return key_to_search


server_sock = socket.socket()
server_sock.bind(("0.0.0.0", 53))
server_sock.listen(3)

my_sock = socket.socket()
ip_to_host = {"1.1.1.1":"king", "2.2.2.2":"loser", "3.3.3.3":"my server", "4.4.4.4":"blabla"}

while True:

    client_sock, addr = server_sock.accept()
    print(f"{addr[0]} - connected")

    try:
        data = client_sock.recv(2).decode()
    except Exception as e:
        print(f"error in recv {str(e)}")
        continue
    if data == "1":
        data = "1.1.1.1"
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


    found = False
    if data in ip_to_host:
        data = ip_to_host[data]
        found = True
        print(data)

    elif get_key(data, ip_to_host) in ip_to_host:
        data = get_key(data, ip_to_host)
        found = True
        print(data)

    if found:
        try:
            send_data(server_sock, 2, data)
            new_data = my_sock.recv(2).decode()
            send_data(client_sock, 2, new_data)
            continue
        except Exception as e:
            print(f"error in send - {str(e)}")
            continue
    else:
        try:
            my_sock.connect(("127.0.0.1", 54))
            send_data(server_sock, 2, data)
        except Exception as e:
            my_sock.close()
            print(f"server is down - try again {str(e)}" )





