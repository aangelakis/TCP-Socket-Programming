import socket
import sys
import re
import os

assert(len(sys.argv) == 1)

# Taking the IP of this server and storing it in TCP_IP.
#hostname = socket.gethostname()
pipe = os.popen("ifconfig")
ifconf_out = pipe.read()
index = ifconf_out.find('51')
TCP_IP = ifconf_out[index:(index+10)]

print("\nMy IP: " + TCP_IP)

# TCP_PORT is fixed: 50000.
TCP_PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # We create a TCP socket.
sock.bind((TCP_IP, TCP_PORT)) # We bind to the open socket.
sock.listen(1) # We expect only one client to connect with us.
conn, addr = sock.accept() # We accept the new sender.

print ('Connection established with', addr[0])

IP_str = conn.recv(150).decode('ascii')
IP_list = IP_str.split('\n')
IP_list.remove("")

print("\nIP_LIST:", IP_list)

OUT_msg = ""
# ping - traceroute
for ip in IP_list:
    if ip != TCP_IP:
        print('\n')
        ping_pipe = os.popen("ping -c 3 " + ip)
        ping_out = ping_pipe.read()
        output = ping_out.split()
        avg_rtt = output[len(output) - 2].split('/')
        print("Latency: ", avg_rtt[1])
        OUT_msg += avg_rtt[1] + "\n"
        print('\n')
        
        trace_pipe = os.popen("traceroute " + ip)
        trace_out = trace_pipe.read()
        hops = trace_out.count('\n')-1
        print('Number of HOPS: ',hops)
        path = re.findall(r'\(.*?\)', trace_out)
        path = [s.replace(")", "") for s in path]
        path = [s.replace("(", "") for s in path]
        path = [s.strip(' ') for s in path]
        del path[0]
        for i in range(len(path)):
            OUT_msg += path[i] + ","
        OUT_msg = OUT_msg[:-1]
        OUT_msg += "\n" + str(hops) + "\n"
        print("Traceroute path: ", path, '\n')


conn.send(OUT_msg.encode())

sock.close()
conn.close()
