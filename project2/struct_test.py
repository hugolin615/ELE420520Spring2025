import struct

# = : native
# < : little endian
# > : big endian
var = struct.pack('=hhl', 1,2,3)  
# var = struct.pack('hhl', 1,2,3)
print(var)

a = [1,2,3]
var = struct.pack('=iii', *a)
print(var)

b = [2,3]
var = struct.pack('=hhh', 1, *b)
print(var)

result = struct.unpack('=hhh', var)
print(result)
