__author__ = 'srkiyengar'

fname = "data.txt"



class labviewProcessor():

    def __init__(self, fname):
        with open(fname, "r") as qfile:
            lines = qfile.readlines()
            self.data = []
            for line in lines[6:]:
                if 'Both' not in line:
                    self.extract_qdata(line)

    def extract_qdata(self,line_data):

        data = line_data[line_data.rfind(':')+2:-2].split(' *** ')
        tool1 = data[0].split(',')
        tvector1 = map(float,tool1[:3])
        qvector1 = map(float,tool1[3:-1])

        tool2 = data[1].split(',')
        tvector2 = map(float,tool2[:3])
        qvector2 = map(float,tool2[3:])
        self.data.append([tvector1,qvector1,tvector2,qvector2])



if __name__ == '__main__':
    vect = labviewProcessor(fname)

    j = 0
    new_file = open('pqvector.txt', "w")
    for i in vect.data:
        c = vect.data[j]
        p1 = c[0]
        q1 = c[1]
        p2 = c[2]
        q2 = c[3]
        result_str = str(j+1) + ": "+str(p1) + '--' + str(q1) + '**'+ str(p2) + '--' + str(q2) + '\n'
        new_file.write(result_str)
        j +=1

    new_file.close()