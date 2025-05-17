# Extract Server <----------- Transform Client
# Transform Server <--------- Load Client




# Client to Extract
# Client to Load

import socket
import time

# Extract Server
EXTRACT_HOST = "localhost"
EXTRACT_PORT = 5100

# Transform Info
TRANSFORM_HOST = "localhost"
TRANSFORM_PORT = 5001


def transform_line(line):
    fields = line.split("|")
    if len(fields) < 8:
        return None

def transform_line(line):
    fields = line.split("|")
    if len(fields) < 10:
        return None
    game_id, score, team_1, team_2, team_3, _ , points, description = fields
    
    return f"{game_id}, {score}, {team_1}, {team_2}, {team_3}, {_}, {points}, {description}"

#nesting two sockets open at the same time
def main():
    # Transform CLIENT (To Extract)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as extract_socket:
        extract_socket.connect((EXTRACT_HOST, EXTRACT_PORT))
        print("Transform CLIENT connected to Extract...")

        # Transform SERVER (To Load)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as transform_socket:
            transform_socket.bind((TRANSFORM_HOST, TRANSFORM_PORT))
            transform_socket.listen(1)
            print("Transform Server waiting for LOAD connection...")

            load_conn, _ = transform_socket.accept()

            with load_conn, extract_socket:
                print("T-Client connected to Extract| Load connected to T-Server")

                while True: 
                    data = extract_socket.recv(1024)
                    if not data:
                        break
                    for line in data.decode().split("\n"): 
                        if line:
                                load_conn.sendall(line.encode() +b"\n")
                                print(f"Receive data: {line}. Sending data: {t_data}")


if __name__ == "__main__":
    main()