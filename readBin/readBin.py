import struct
with open('../data.bin', 'rb') as f:
    while True:
        data = f.read(4)
        if not(data):
            break
        v0, = struct.unpack('f', data)
        v1, = struct.unpack('f', f.read(4))
        v2, = struct.unpack('f', f.read(4))
        out = f"{v0},{v1},{v2}"
        print(out)