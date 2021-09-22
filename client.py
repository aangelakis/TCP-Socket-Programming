import socket
import sys
import time

assert(len(sys.argv) == 2)


# Taking the string with the hosts from the arguments.
hosts_list = sys.argv[1]

# We are removing [] from the string because hosts_list was not a list.
chars_to_remove = "[]"
for character in chars_to_remove:
    hosts_list = hosts_list.replace(character,"")

hosts_list = hosts_list.split(',')

# Opening the Configuration file.
configFile = open("ConfigurationFile.txt", "r")
#print ("\nOpening:", configFile.name)

# Read everyline of the ConfigurationFile and store it in a list.
FileLines = configFile.readlines()


IP_str = ""

# Find the IPs of each host from the ConfigurationFile and store it
# in the IP_list.
for host in hosts_list:
    for line in FileLines:
        line_list = line.split(', ')
        if(host == line_list[0]):
            IP_str += line_list[1]

IP_list = IP_str.split('\n')
IP_list.remove('')


TCP_server_ports = 50000 # The port number of the receiver..

#print("\nIP_list = ",IP_list,"\n")


auxil_list = []

for i in range(len(IP_list)):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # We create a TCP socket.
    sock.connect((IP_list[i], TCP_server_ports))#We connect to the ports of receiver servers
    sock.send(IP_str.encode()) # We send the message.
    msg_list = sock.recv(1024).decode('ascii').split('\n') # decode byte msg and store it as a list
    msg_list.remove('')
    index = 0
    for j in range(len(IP_list)):# Each Output line that we want has 4 domains
        if i != j:
            str_aux = "HOST:" + hosts_list[i] + "->" + hosts_list[j]
            str_aux += "\tLATENCY:" +msg_list[index]
            index += 1
            path_str = ""
            path = msg_list[index].split(',')
            for line in FileLines:
                for k in range(len(path)):
                    line_list = line.split(', ')
                    for hop in line_list:
                        if hop == path[k]:
                            path_str += line_list[0] + "-"
            path_str = path_str[:-1]
            str_aux += "\tPATH:" + hosts_list[i] + "-" + path_str + "-" + hosts_list[j]
            index += 1
            str_aux += "    HOPS:" + msg_list[index]
            index += 1
            auxil_list.append(str_aux)
    sock.close() # We close the socket.



for i in range(len(auxil_list)):
    print(auxil_list[i],'\n')


configFile.close()
