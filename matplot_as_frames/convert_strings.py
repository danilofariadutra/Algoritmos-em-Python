import os

file = r'C:/Users/Autaza/Desktop/Aero/beacon_reading_cdp.txt'

xyz = list()
pos = 0

with open(file) as file:
    x, y, z = str(), str(), str()
    for line in file:
        if 'Stationary beacon:' not in line:
            unique_line = str()
            for item in range(len(line)):
                if 'X' in line[item]:
                    x = str(list(line.split())[8]).replace('X=', '')
                    # print(x)
                
                if 'Y' in line[item]:
                    y = str(list(line.split())[10])
                    # print(y)
                    
                if 'Z' in line[item]:
                    z = str(list(line.split())[11]).replace('Z=', '')
                    # print(z)
                str_xyz = '[' + str(pos) + ', ' + x + ', ' + y + ', ' + z + ']'
                if unique_line != str_xyz:
                    xyz.append(str_xyz)
                    unique_line = str_xyz
        pos = pos + 1
 
if os.path.exists('C:/Users/Autaza/Desktop/Aero/testes.txt'):
    open('C:/Users/Autaza/Desktop/Aero/testes.txt', 'a').close()
    
with open(r'C:/Users/Autaza/Desktop/Aero/testes.txt', 'w') as file:
    for coords in xyz:
        file.write(coords)
        file.write('\n')
        