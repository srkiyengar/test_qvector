__author__ = 'srkiyengar'

import math

file_name = "vector_addition.txt"
out_put = "vector_addition_result"

with open(file_name, "r") as my_file:
    new_file = open(out_put, "w")
    #my_lines = []
    for each_line in my_file:
        each_line = each_line.strip('\r\n')
        if each_line:
            time_str = each_line[12:38]
            sp_line = each_line[51:]
            sp_line = sp_line.translate(None,'***')
            my_list = sp_line.split(',')
            new_list = []
            for val in my_list:
                new_list.append(float(val))
            if 0.000000 not in new_list:
                #my_lines.append(sp_line)
                a = new_list[0]-new_list[7]
                b = new_list[1]-new_list[8]
                c = new_list[2]-new_list[9]
                l = math.sqrt(math.pow(a,2)+math.pow(b,2)+math.pow(c,2))
                result_str = str(l) + ',' + str(a) + 'i+'+ str(b) + 'j+' + str(c) + 'k' + '\n'
                #q_str = str(new_list)
                #q_str = q_str.strip('[')
                #q_str = q_str.strip(']')
                new_file.write(result_str)
    new_file.close()



a = 5


