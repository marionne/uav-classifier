import json
import math
from math import ceil
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import statistics

def dict_ignore_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k not in d:
           d[k] = v
    return d

#with open('./10Mar1-01.json') as i:
with open('./testing0.json') as i:
    a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)    

    counts={}
    totalpacketcount=0
    index=1 
    
    packet_size_sum = 0
    packet_size_average=0 
    packet_size_stddev=0

    packetsizes = []
    frequencies = []
    for packet in a:
        
        totalpacketcount = totalpacketcount + 1

        packet_size = int(packet['_source']['layers']['frame']['frame.len'])
        time_stamp = float(packet['_source']['layers']['frame']['frame.time_epoch'])
        time_delta = float(packet['_source']['layers']['frame']['frame.time_delta'])
        packet_type = int(packet['_source']['layers']['frame']['frame.encap_type'])
        #packet_type_subtype = int(packet['_source']['layers']['wlan']['wlan.fc_tree']['wlan.fc.subtype'])
        #mac_time = int(packet['_source']['layers']['wlan_radio']['wlan_radio.timestamp'])
        #signal = int(packet['_source']['layers']['wlan_radio']['wlan_radio.signal_dbm'])
#       channel = int(packet['_source']['layers']['wlan_radio']['wlan_radio.channel'])
        #sa = packet['_source']['layers']['wlan']['wlan.sa']
        #da = packet['_source']['layers']['wlan']['wlan.da']
        #data_data = packet['_source']['layers']['data']['data.data']

        
        if packet_size in counts:

            packetsizes.append(packet_size)
            frequencies.append(counts[packet_size])

            print("{}\t\t{}\t\t{}\t\t{}\t"
                  "{}\t {}"
                  "".format(index, packet_size, counts[packet_size], time_stamp, time_delta, packet_type), '\n') 
                      #packet_type_subtype),'\n')

            index = index + 1
            packet_size_sum = packet_size_sum + packet_size
            packet_size_average = packet_size_sum/index

            packet_size_stddev = math.sqrt((packet_size_stddev + pow(packet_size - packet_size_average, 2))/(index-1))

            counts[packet_size] = counts[packet_size] + 1

            #print("Index: {}\tPacket Size: {}\tPacket Size Sum: {}\tPacket average is {}\tStandard Deviation is {}\n".format(index,packet_size,packet_size_sum,ceil(packet_size_average), packet_size_stddev))
        else:
            counts[packet_size] = 1

print("Index\t\tPacket Size\tNth Packet\tTime Stamp\t\tTime Delta\tType\tSubtype")
print("\t\t(bytes)\t\t<packet size>")


packetslost = totalpacketcount-index

print('\n'"TOTAL PACKET COUNT: {}".format(totalpacketcount), '\n')
print("PACKETS OMITTED(DUPLICATES?) = {}".format(packetslost),'\n')
print("AVERAGE PACKET SIZE == {}\n".format(round(packet_size_average)))
print("STANDARD DEVIATION == {}\n".format(round(packet_size_stddev)))
#print(counts,'\n')

x = packetsizes
y = frequencies


plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(x, y, color = 'r')
plt.xlabel('Packet Size (bytes)')
plt.ylabel('Frequency (Occurences)')

plt.subplot(132)
plt.scatter(list(counts.keys()), counts.values(), color='g')
plt.xlabel('Packet Size (bytes)')
plt.grid(True)

plt.subplot(133)
plt.plot(x, y)

plt.xlabel('Packet Size (bytes)')

plt.suptitle('Packet Size v. Packet Frequency')

plt.show()

