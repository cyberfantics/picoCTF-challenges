import random
import subprocess

# from packet 1
arrival_time = 1614044650.913789387

data = None

# read my data extracted from wireshark
with open('flagdata', 'r') as f:
    data = f.read()

# remove newlines
data = bytearray([int(d, 16) if d != '' else 0 for d in data.split('\n')])

# manually deal with malformed packets
data[434-1] = 0x23
data[1700-1] = 0x0f

random.seed(int(arrival_time))

# create a known array and shuffle it to create a mapping to reverse the shuffle
control = [i for i in range(len(data))]
random.shuffle(control)

decoded = bytearray([0 for i in range(len(data))])

# go through each byte of data
for i in range(len(data)):
    # generate a number for the port, for two reasons:
    #   1. so I can check them against those in wireshark
    #   2. to keep the random number generation in the same order as in send.py
    port = random.randrange(65536)

    # apply the same XOR as in send.py (it is its own inverse) and de-shuffle
    decoded[control[i]] = data[i]^random.randrange(256)

# write the decoded data out to a file
with open('decoded', 'wb') as f:
    f.write(decoded)
