import json

def dict_ignore_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k not in d:
           d[k] = v
    return d

with open('./testing0.json') as i:
    a = json.load(i, object_pairs_hook=dict_ignore_on_duplicates)    

    counts={}
    totalpacketcount=0
    index=1 
    print("index\t\tpacket size (bytes)\tNth packet with <packet_size>\t\ttime stamp\t\t\t\ttime delta\t\tpacket type")
    for packet in a:
        
        totalpacketcount = totalpacketcount + 1

        packet_size = int(packet['_source']['layers']['frame']['frame.len'])
        time_stamp = float(packet['_source']['layers']['frame']['frame.time_epoch'])
        time_delta = float(packet['_source']['layers']['frame']['frame.time_delta'])
        packet_type = int(packet['_source']['layers']['frame']['frame.encap_type'])
        #packet_type_subtype = int(packet['_source']['layers']['wlan']['wlan.fc_tree']['wlan.fc.subtype'])
        #mac_time = int(packet['_source']['layers']['wlan_radio']['wlan_radio.timestamp'])
        #signal = int(packet['_source']['layers']['wlan_radio']['wlan_radio.signal_dbm'])
        #channel = int(packet['_source']['layers']['wlan_radio']['wlan_radio.channel'])
        #sa = packet['_source']['layers']['wlan']['wlan.sa']
        #da = packet['_source']['layers']['wlan']['wlan.da']
        #data_data = packet['_source']['layers']['data']['data.data']


        if packet_size in counts:

            print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t"
                  "{}\t\t{}".format(index, packet_size, counts[packet_size], time_stamp, time_delta, packet_type), '\n')

            index = index + 1
            counts[packet_size] = counts[packet_size] + 1
            #counts[time_stamp] = counts[time_stamp] + 1
        else:
            counts[packet_size] = 1
            #counts[time_stamp] = 1

print("index\t\tpacket size (bytes)\tNth packet with <packet_size>\t\ttime stamp\t\t\t\ttime delta\t\tpacket type")


packetslost = totalpacketcount-index

print('\n'"TOTAL PACKET COUNT: {}".format(totalpacketcount), '\n')
print("PACKETS OMITTED(DUPLICATES?) = {}".format(packetslost),'\n')
print(counts,'\n')
