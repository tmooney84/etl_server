import socket
import time  #this will be used to emulate lead times

EXTRACT_HOST = "localhost"
EXTRACT_PORT = 5100

def read_data():
    with open("data.csv", "r") as file:
        for line in file:
            yield line

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.bind((EXTRACT_HOST, EXTRACT_PORT))
        s.listen()  #in C can say how many will listen to it
        print("Extract ready to receive connection...")
       ### 
        conn, addr = s.accept()
        with conn:
            print(f"Connected to {addr}")
            for line in read_data():
                conn.sendall(line.encode() +b"\n")
                print(f"Sending: {line}")
                time.sleep(1) #gives small delay to see stuff on screen
       ### 
if __name__ == "__main__":
    main()