import struct

def read_addresses(file_name):

    addresses = []

    if file_name.endswith(".txt"):
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    addresses.append(int(line))
    else:
        with open(file_name, "rb") as file:
            while True:
                data = file.read(4)

                if not data:
                    break

                address = struct.unpack(">I", data)[0] # <I little-endian, >I big-endian
                addresses.append(address)
    return addresses