import random
import numpy as np



nibble0 = {"TK3[0]","TK3[1]","TK3[2]","TK3[5]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[13]","TK3[14]"}
nibble1 = {"TK3[1]","TK3[2]","TK3[3]","TK3[6]","TK3[9]","TK3[10]","TK3[11]","TK3[13]","TK3[14]","TK3[15]"}
nibble2 = {"TK3[0]","TK3[2]","TK3[3]","TK3[7]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[14]","TK3[15]"}
nibble3 = {"TK3[0]","TK3[1]","TK3[3]","TK3[4]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[13]","TK3[15]"}
nibble4 = {"TK3[0]","TK3[1]","TK3[4]","TK3[8]","TK3[9]","TK3[12]","TK3[13]","TK3[14]","TK3[15]"}
nibble5 = {"TK3[2]","TK3[3]","TK3[7]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[13]","TK3[14]","TK3[15]"}
nibble6 = {"TK3[2]","TK3[3]","TK3[6]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[13]","TK3[14]","TK3[15]"}
nibble7 = {"TK3[0]","TK3[1]","TK3[5]","TK3[7]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[13]","TK3[14]","TK3[15]"}
nibble8 = {"TK3[0]","TK3[1]","TK3[2]","TK3[5]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[13]","TK3[14]"}
nibble9 = {"TK3[1]","TK3[2]","TK3[3]","TK3[6]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[13]","TK3[14]","TK3[15]"}
nibble10 = {"TK3[0]","TK3[2]","TK3[3]","TK3[7]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[14]","TK3[15]"}
nibble11 = {"TK3[0]","TK3[1]","TK3[3]","TK3[4]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[12]","TK3[13]","TK3[15]"}
nibble12 = {"TK3[0]","TK3[8]","TK3[11]","TK3[12]"}
nibble13 = {"TK3[1]","TK3[3]","TK3[8]","TK3[9]","TK3[10]","TK3[11]","TK3[13]","TK3[15]"}
nibble14 = {"TK3[2]","TK3[9]","TK3[10]","TK3[14]"}
nibble15 = {"TK3[1]","TK3[9]","TK3[10]","TK3[13]"}

ave = 0
faild = 0
Candidia = [nibble0,nibble1,nibble2,nibble3,nibble4,
            nibble5,nibble6,nibble7,nibble8,nibble9,
            nibble10,nibble11,nibble12,nibble13,nibble14,nibble15]
#nibble = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range (1):

    
    for f1 in range (16):
        for f2 in range (16):
            if (f2==f1):
                faild = faild+1
                continue
            else:
                  #print("location of injection : ",f1,f2)
                  cardinality = (Candidia[f1]) | (Candidia[f2]) - (Candidia[f1]&Candidia[f2])
                  #print("Number of bits for recovery : ",len(cardinality)*4)
                  #print("-----------------------------------")
                  ave = ave + ((len(cardinality))*4)
print(faild)
average = (ave/(256-(faild/1)))/1

print(average)






















