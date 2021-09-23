# Info about this program

In this question, students should implement their own monitoring tool in order to check network
performance within their AS (My AS number was 51). As we know, 2 major indicators for characterizing network 
behavior is the latency and the number of hops between 2 nodes. 

In previous questions, ping and traceroute tools were used in order to study the communication between hosts. Also, ping
provides information for the latency over a path between 2 hosts.

Now, students should create their custom monitoring mechanism for the latency and the number
of intermediate routers (hops) among a path. In more details, the system should follow the 
client-server architecture. Assume, a host in your AS is interested in monitoring the latency and
the number of hops for the paths connecting a group of hosts in the network. This host acts
as a client in the application, triggering the hosts described in group of hosts to start running
measurements about the latency and the number of hops between them as well as the sequence of
intermediate routers that form the path for a pair of hosts, acting as servers. The measurement
process should be executed by each possible pair of hosts in the list. The measurements should
use ping and traceroute commands. When each host in the above list has accomplished the
measurements for the other members, this information should be transmitted and stored in the
client host. 

For the communication and data exchange between hosts, **TCP sockets** should be
utilized. When the client host has received the measurements about the latency, the number of
hops and the sequence of routers in terms of IPs for the path for each pair of hosts, the client
has a detailed overview for the communication between the server hosts based on fundamental
network indicators. For your application, Python should be used as programming language.
Based on the above description, your application in the client side should be executed as

**> python client.py [host1, host2, · · · , hostN]**

where client.py is the client part of your application that should inform the server hosts
described in the list [host1, host2, · · · , hostN] in order to start executing measurements about the
latency, the number of hops and the routers that form the path for each possible pair between
them. The list [host1, host2, · · · , hostN] contains the hosts that act as servers with
their host names (not their IPs). 

For this reason, you should use a configuration file in .txt form that includes the 
IPs that you assigned to each host and each router interface. 

Your client script should initially read this configuration file and translate each host name in the
list [host1, host2, · · · , hostN] to the corresponding IP assigned to each host. So the initial list
[host1, host2, · · · , hostN] should be translated to the list [IP1, IP2, · · · , IPN], where IP_i
is the IP assigned to host_i. 

The above list including host IPs should be transmitted to the server
hosts for the measurement process. When each server has finished the measurements, the results
should be transmitted to the client host, that stores this information. When the client
receives the traceroute output from a server, each IP described as hop in the traceroute should
be also translated to the corresponding router name. This is feasible using the configuration
file. 

So finally, for each pair of hosts in the initial list, the client should store the latency,
the number of hops and the full description of the path in terms of router names
between the 2 hosts. 

On the other hand, the hosts described in the list, act as servers that start
executing measurements using ping and traceroute tools for the other hosts in the list when they
are triggered by the client. Also, as soon as each measurement is accomplished, they transmit
the required information to the client. The server functionality should be implemented in the
server.py file.
