import socket
import time 
import mcp3008 as mcp

#import os
#def check_open_fds(tag=''):
#    fd_path = f"/proc/{os.getpid()}/fd"
#    try:
#        num_fds = len(os.listdir(fd_path))
#        print(f"[FD Check] {tag} Open FDs: {num_fds}")
#    except Exception as e:
#        print(f"[FD Check] Failed to list FDs: {e}")

class MonitoringDevice: 
    
    def __init__(self,name,address):
        self.name = name
        self.address = address
        
    def get_data(self):
    #raise NotImplementedError('error! get_data is not implemented in class.')
        pass 

    def send_data(self,channels,values,times): 
    # kind of like a guidebook to other subclasses on how to write your def function w the arguments 
        pass
    
    def connect(self,address):
        pass
    
    def disconnect(self):
        pass

temp = False

class RPI(MonitoringDevice):    
    def __init__(self,name,address,port,device_names=[],timeout=1.0): 
    #device_names and timeout are set as default as [] as 1.0, also initializing this overwrites parent class attr
        self.name = name #name of arduino
        self.address = address #ip address of arduino shield
        self.port = port # port of arduino
        self.device_names = device_names #default is []. put e.g. [ionpump, photodiode]
        self.timeout = timeout #which we default set at 1.0
        #self.device = self.connect() #create variable called device that is then stored inside the class
        data = self.get_data() #'temporary' variable
        #self.adc = adc
            #print("Initialised")
       # except Exception as e:
        #    print(f"Failed to initialise adc: {e}")
        #self.adc_1 = adc_1
        
#    def connect(self):
#        print("here")
#        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        sock.settimeout(self.timeout) #which default is 1
#        sock.connect((self.address, self.port))
#        print("[RPI] Connected to server at {self.address}:{self.port}")
#        
#        return sock
        
    def get_data(self): # defining a function here but is already used above see 'temporary' variable
        while True:
            
            ports = [[mcp.CH0],[mcp.CH1],[mcp.CH2],[mcp.CH3],[mcp.CH4],[mcp.CH5],[mcp.CH6],[mcp.CH7]]
            data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#            for j in range(2):
#                if j == 0:
#                    for i in range(len(ports)):
#                        voltage = float(str(self.adc.read(ports[i]))[1:-1])*3.3/1023
#                        data[i+8*j].append(voltage)
#                else:
#                    for i in range(len(ports)):
#                        voltage = float(str(adc_1.read(ports[i]))[1:-1])*3.3/1023
#                        data[i+8*j].append(voltage)
                    
            for j in range(2):
#                check_open_fds("before calling mcp")
                adc = mcp.MCP3008(device = j)
#                check_open_fds("after calling mcp")
                for i in range(len(ports)):
                    voltage = float(str(adc.read(ports[i]))[1:-1])*3.3/1023
                    data[i+8*j].append(voltage)
                    #time.sleep(0.01)
                adc.close()
            return data

    def send_data(self,data,data_server): #arguments are data, data_server
        values = data[:len(self.device_names)]  #slice 16-array data to no. of devices we have
        for i in range(len(values)):                   #eg if two devices in device_names then only two data
            dest = self.name + "." + self.device_names[i] #destination name
            data_send = (values[i][0])
            t = str(time.time())
            #print(values[i][0])
            
            dest_enc = dest.encode('UTF-8')
            data_send_enc = str(data_send).encode('UTF-8')
            t_enc = t.encode('UTF-8')
            try:
                data_server.send(b'%s %s %s\n' % (dest_enc,data_send_enc,t_enc))
            except Exception as e:
                print(f"Error: {e}")
#                if str(e) == '[Errno 104] Connection reset by peer':
#                    print(e)
#                    global temp
#                    temp = True
#                    print(temp)
#                    print(f"Error: {e}")
#                else:
#                    print(f"Error: {e}")
#                    print("1")
#                    print(e)
#                    print(temp)
                    #time.sleep(0.5)
                    
                    
#    def check_errno104(self):
#        global temp
#        print("Temp: "+str(temp))
#        if temp == True:
#            return True
#        else:
#            pass





    

