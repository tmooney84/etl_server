import socket

#at one moment needs to be a client and then a server

TRANSFORM_HOST = "localhost"
TRANSFORM_PORT = "5001" # Equal to the tranform port

def main():
    with socket.socket(socket.AF.INET, socket.SOCK_STREAM) as s:
        s.connect((TRANSFORM_HOST, TRANSFORM_PORT))
        print("LOAD client Connected to Transform Server")
        with open("my_loaded_data.csv", "w+") as file:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                file.write(data.decode() + b"\n")
                print(f"Transformed data received: {data.decode().split("\n")}")

if __name__ == "__main__":
    main()