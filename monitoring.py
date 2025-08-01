import socket
import time 
import mcp3008 as mcp

class MonitoringDevice: #same format as previous runfiles
    def __init__(self,name,address):
        self.name = name
        self.address = address
        
    def get_data(self):
        pass 

    def send_data(self,channels,values,times): 
        pass
    
    def connect(self,address):
        pass
    
    def disconnect(self):
        pass

class RPI(MonitoringDevice):    
    def __init__(self,name,address,port,device_names=[],timeout=1.0): 
    #device_names and timeout are set as default as [] as 1.0, also initializing this overwrites parent class attr
        self.name = name #name of raspberrypi
        self.address = address #ip address of rpi
        self.port = port # port of rpi
        self.device_names = device_names #default is []. put e.g. [ionpump, photodiode]
        self.timeout = timeout #which we default set at 1.0
        data = self.get_data() #'temporary' variable
        
    def get_data(self): # defining a function here but is already used above see 'temporary' variable
        while True:            
            ports = [[mcp.CH0],[mcp.CH1],[mcp.CH2],[mcp.CH3],[mcp.CH4],[mcp.CH5],[mcp.CH6],[mcp.CH7]] #read function requires list input
            data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
            #loop through channels        
            for j in range(2):
                adc = mcp.MCP3008(device = j) #2 mcp3008 chips per rpi
                for i in range(len(ports)):
                    voltage = int(adc.read(ports[i])[0])*3.3/1023
                    data[i+8*j].append(voltage)
                adc.close()
            return data

    def send_data(self,data,data_server): #arguments are data, data_server
        values = data[:len(self.device_names)]  #slice 16-array data to no. of devices we have
        for i in range(len(values)):                   #eg if two devices in device_names then only two data
            dest = self.name + "." + self.device_names[i] #destination name
            data_send = values[i][0]
            t = str(time.time())     
            dest_enc = dest.encode('UTF-8')
            data_send_enc = str(data_send).encode('UTF-8')
            t_enc = t.encode('UTF-8')
            try:
                data_server.send(b'%s %s %s\n' % (dest_enc,data_send_enc,t_enc))
            except Exception as e:
                print(f"Error: {e}")
                    
        




    

