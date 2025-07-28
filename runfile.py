from monitoring import RPI
import socket
import time 

CARBON_HOST = '172.29.10.14' 
CARBON_PORT = 2003

temp = True

if __name__ == "__main__": 
    #PROCEED WITH DATA COLLECTION AND SENDING TO GRAFANA
    def data_acquire_send_loop(device): #argument is any instance-ed device
<<<<<<< HEAD
        global temp        
=======
        global temp
>>>>>>> 2fe2860c1f3b9e9b1a24079b2f2704d25a308202
        while temp == True:
            try:
                print("Trying to connect to server...")
                data_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                data_server.settimeout(10)
                data_server.connect((CARBON_HOST, CARBON_PORT))
                data_server.setsockopt(socket.SOL_SOCKET,socket.SO_KEEPALIVE,1)
                print(f"[Client] Connected from {data_server.getsockname()} to {data_server.getpeername()}")
<<<<<<< HEAD
                
=======
>>>>>>> 2fe2860c1f3b9e9b1a24079b2f2704d25a308202
                print("Connected to server")
                temp = False
            except Exception as e:
                print(f"Connection failed: {e}. Retrying in 1 second ...")
                temp = True
                time.sleep(1)
        
        while True:
            try:
<<<<<<< HEAD
                data = device.get_data()
=======
>>>>>>> 2fe2860c1f3b9e9b1a24079b2f2704d25a308202
                device.send_data(data,data_server)
                time.sleep(0.5)
            except Exception as e:
                print(f"Error: {e}. Retrying in 1 second ...")
                time.sleep(1)
                
    rp_device_names = ['R0_0','R0_1','R0_2','R0_3','R0_4','R0_5','R0_6','R0_7','R1_0','R1_1','R1_2','R1_3','R1_4','R1_5','R1_6','R1_7']
    rpi = RPI(name = 'rpi', address=CARBON_HOST, port = CARBON_PORT, device_names=rp_device_names)
    print("[Main] Starting data acquisition process")
    data_acquire_send_loop(rpi)
    print("[Main] Process started")
<<<<<<< HEAD

=======
>>>>>>> 2fe2860c1f3b9e9b1a24079b2f2704d25a308202
    
	


