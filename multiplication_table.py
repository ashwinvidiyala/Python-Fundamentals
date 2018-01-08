line1 = ["x"]
line2 = [1]
line3 = [2]
line4 = [3]
line5 = [4]
line6 = [5]
line7 = [6]
line8 = [7]
line9 = [8]
line10 = [9]
line11 = [10]
line12 = [11]
line13 = [12]

for i in range(1, 13):
    line1.append(i)
    line2.append(i)
    line3.append(2 * i)
    line4.append(3 * i)
    line5.append(4 * i)
    line6.append(5 * i)
    line7.append(6 * i)
    line8.append(7 * i)
    line9.append(8 * i)
    line10.append(9 * i)
    line11.append(10 * i)
    line12.append(11 * i)
    line13.append(12 * i)

def horizontal_print(list):
    for x in list:
        print x,
    print ""

horizontal_print(line1)
horizontal_print(line2)
horizontal_print(line3)
horizontal_print(line4)
horizontal_print(line5)
horizontal_print(line6)
horizontal_print(line7)
horizontal_print(line8)
horizontal_print(line9)
horizontal_print(line10)
horizontal_print(line11)
horizontal_print(line12)
horizontal_print(line13)
