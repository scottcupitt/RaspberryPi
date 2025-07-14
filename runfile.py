from monitoring import RPI

import socket
import time 
#import mcp3008 as mcp
#from multiprocessing import Process

CARBON_HOST = '172.29.10.14' 
CARBON_PORT = 2003

#import os
#def check_open_fds(tag=''):
#    fd_path = f"/proc/{os.getpid()}/fd"
#    try:
#        num_fds = len(os.listdir(fd_path))
#        print(f"[FD Check] {tag} Open FDs: {num_fds}")
#    except Exception as e:
#        print(f"[FD Check] Failed to list FDs: {e}")
#import subprocess
#def check2003():
#    output = subprocess.check_output(["ss","-tnp"],text=True)
#    for line in output.splitlines():
#        if "2003" in line or "python" in line:
#            print(line)
#def is_socket_connected(sock):
#    try:
#        sock.send(b'',socket.MSG_DONTWAIT | socket.MSG_NOSIGNAL)
#        return True
#    except:
#        return False
temp = True

if __name__ == "__main__": 
#    temp = True
#    number = 0
#    count = 0
    #PROCEED WITH DATA COLLECTION AND SENDING TO GRAFANA
    def data_acquire_send_loop(device): #argument is any instance-ed device
        global temp
#        if temp == True:
#            print("Trying to connect to server...")
#            data_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#            data_server.connect((CARBON_HOST, CARBON_PORT))
#            print("Connected to server")
#            temp = False
#        else:
#            print("Connection failed. Retrying in 1 second ...")
#            temp = True
#            time.sleep(1)
        
        while temp == True:
            try:
                print("Trying to connect to server...")
                data_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                data_server.settimeout(10)
                data_server.connect((CARBON_HOST, CARBON_PORT))
                data_server.setsockopt(socket.SOL_SOCKET,socket.SO_KEEPALIVE,1)
                print(f"[Client] Connected from {data_server.getsockname()} to {data_server.getpeername()}")
#                if not is_socket_connected(data_server):
#                    print("[Client] Connection lost")
                
                print("Connected to server")
                temp = False
            except Exception as e:
                print(f"Connection failed: {e}. Retrying in 1 second ...")
                temp = True
                time.sleep(1)
        
        while True:
            try:
#                check_open_fds("before getdata")
#                print("[Client] Getting data...")
                data = device.get_data()
#                check_open_fds("after getdata")
#                print("[Client] Sending data...")
#                if device.check_errno104() == True:
#                    #global temp
#                    print("here")
#                    temp = True
#                    break
                device.send_data(data,data_server)
#                check_open_fds("after send")
                time.sleep(0.5)
#                global number
#                global count
#                if number <0:
#                    number += 1
#                else:
#                    print("\n")
#                    count += 1
#                    number = 0
#                    check2003()
#                    print(is_socket_connected(data_server))
#                    print(count)
            except Exception as e:
                print(f"Error: {e}. Retrying in 1 second ...")
                time.sleep(1)
                
    rp_device_names = ['R0_0','R0_1','R0_2','R0_3','R0_4','R0_5','R0_6','R0_7','R1_0','R1_1','R1_2','R1_3','R1_4','R1_5','R1_6','R1_7']
    rpi = RPI(name = 'rpi', address=CARBON_HOST, port = CARBON_PORT, device_names=rp_device_names)
    print("[Main] Starting data acquisition process")
    data_acquire_send_loop(rpi)
    #p.start()
    print("[Main] Process started")
    
#    try:
#        while True:
#            pass
#    except KeyboardInterrupt:
#        pass
#        #p.terminate()
    
	


