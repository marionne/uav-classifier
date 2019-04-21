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

    counts = {}
    for packet in a:
        packet_size = int(packet['_source']['layers']['frame']['frame.len'])

        if packet_size in counts:
            counts[packet_size] = counts[packet_size] + 1
        else:
            counts[packet_size] = 1
    
    print(counts)

