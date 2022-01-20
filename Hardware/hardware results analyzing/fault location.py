
import binascii
import random
import numpy as np
from array import *

##CRAFT Cipher##
S = [0xc, 0xa, 0xd, 0x3, 0xe, 0xb, 0xf, 0x7, 0x8, 0x9, 0x1, 0x5, 0x0, 0x2, 0x4, 0x6]
P = [0xF, 0xC, 0xD, 0xE, 0xA, 0x9, 0x8, 0xB, 0x6, 0x5, 0x4, 0x7, 0x1, 0x2, 0x3, 0x0]
Q = [0xC, 0xA, 0xF, 0x5, 0xE, 0x8, 0x9, 0x2, 0xB, 0x3, 0x7, 0x4, 0x6, 0x0, 0x1, 0xD]
RC3 = [0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1,
       0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5]
RC4 = [0x1, 0x8, 0x4, 0x2, 0x9, 0xc, 0x6, 0xb, 0x5, 0xa, 0xd, 0xe, 0xf, 0x7, 0x3, 0x1, 0x8, 0x4, 0x2, 0x9, 0xc, 0x6,
       0xb, 0x5, 0xa, 0xd, 0xe, 0xf, 0x7, 0x3, 0x1, 0x8]
R = 31
dec = 0
Stt = {}
Sttf = {}
TC = {}
r = 0

## Enc() ==> dec = 0;
##Dec() ==> dec = 1;
# A17D6BD4BEEB996F
#0x5734F006D8D88A3E
Plain = 0xA17D6BD4BEEB996F  ##// Plain

Plainfulty =[0x3000000B6700300B
             ,0x2B00400B0000000B
             ,0xA2BB0000000F000B
             ,0x2600400B0500500B
             ,0x67BB600E60639535
             ,0x0730002000000200
             ,0x0200000000C05000
             ,0x02A0000B0D000000
             ,0x0012B00000000000
             ,0x3701000000000007
            ,0x0000AF300E100072
            ,0x0000AF300E100008
            ,0x300100B000B0F000
            ,0x8900380000002008
            ,0x02930000000A3660
            ,0x0693700000003600
            ,0x0663500000C00600
            ,0x068000FF0D60F000
            ,0x02000340F00F2900
            ,0x0C0E00007F6E0C50
            ,0x00000F000F0000FF
            ,0x200000000F0000FF
            ,0x000000000F0000FF
            ,0x07C027E00CF07200
            ,0x2C0000000F0040FF
            ,0x200000000F0040FF
            ,0x2C0C00000F0040FF
            ,0x0C0C0C00000F0000
            ,0x040C0C00000F0000
            ,0x0C0C00000F0000FF
            ,0x000C00000F0000FF
            ,0x00000000000000FF
            ,0x0011100010F00620
            ,0x0011100000F00620
            ,0x00111000000C0620
            ,0x00111000000C0000
            ,0x00111000000C0020
            ,0x000077770F0000FF
            ,0x000007770F0000FF
            ,0x000000770F0000FF
            ,0x000000000F000000
            ,0x20020000FF50E0F7
            ,0x00000000F708F00E
            ,0x7B00240000000000
            ,0x7700240000000000
            ,0x0004400047700040
            ,0x00000000400BF00C
            ,0x0800F49704000E00
            ,0x0800F4F700040000
            ,0x0EF0400C7A600C00
            ,0xC904C00000088000
            ,0x4204020000000000
            ,0xE00040020A600C00
            ,0x07000EE0C000EE0C
            ,0x800F0900C0000E00
            ,0x0000CA0070A9E0FF
            ,0xC00044404000F0C4
            ,0x000000000F0C0CFF
            ,0x00000000080A0A88
            ,0x7032738380000000
            ,0x00000000000A0A88
            ,0x0000000000000A88
            ,0x340C000000000000
            ,0x0000000006002D86
            ,0x3203800000000000
            ,0x02000000060A0A66
            ,0x00000000060A0A66
            ,0x0000000000000A66
            ,0x0000000000000066
            ,0x0000000000000006
            ,0x0000000000100A66
            ,0xA0000002060A0066
            ,0xA0BF0002060A0066
            ,0xA0BF00B0060A0066
            ,0xA0BF00B0000A0066
            ,0xA0BF00B0000F00B0
            ,0x000000A3060A0A66
            ,0x6030030E33300400
            ,0x00BF00B0060A0A66
            ,0x000000B0060A0A66
            ,0xA088880000000E28
            ,0xA088880000000028
            ,0xA088880000000008
            ,0xA088880000000000
            ,0xFC00C00A00000B01
            ,0x000007720F0A0AFF
            ,0x001007720F0A0AFF
            ,0x001000720F0A0AFF
            ,0x001000020F0A0AFF
            ,0x001000000F0A0AFF
            ,0x000000000F0A0AFF
            ,0x00000000000A0AFF
            ,0x0000000000000AFF
            ,0x000000000000000A
            ,0x0F0000000F0A0AFF
            ,0x0F000F000F0A0AFF
            ,0x004000A30F0A0AFF
            ,0x000000A30F0A0AFF
            ,0x00000F000F0A0AFF
            ,0x00A0F00D00D07700
            ,0x00A0F006D8D07700
            ,0x000040000200000E
            ,0x0A0B800E00800000
            ,0x000000F8A00C2CE0
            ,0x022C500000000A0E
            ,0x0101010101010901
            ,0x046D500000000A40
            ,0x1FF9012070000F00
            ,0x004A00300640F220
            ,0x0C00000C30000FF0
            ,0x000FF00EFEFEE000
            ,0x070F0FF000F0FF00
            ,0x100C300CA0000400
            ,0x100C300C83300000
            ,0x00E3BC07020000B0
            ,0x60000062B090C30C
            ,0xF000000C00000000
            ,0x70BFF0000700043C
            ,0x8000507FF0000000
            ,0x0FC0000005200000
            ,0x094000300F09FD60
            ,0x096000300F09FD60
            ,0x08100210F00F0600
            ,0x08130230F00F0600
            ,0x2002847242000000
            ,0x0735B000006FF0E0
            ,0x000000002020BA0B
            ,0x0B00B000006FF000
            ,0x000F00B90060BA0B
            ,0xF7000000000000B0
            ,0x000000002020BA0B
            ,0x6000C00B00000000
            ,0xD000C00BF0000000
            ,0x07B00000E055E0BB
            ,0x5000400000000000
            ,0x0003111000000000
            ,0x0003111100000000
            ,0x200000000000000E
            ,0x0002500802000022
            ,0x0000000802000022
            ,0x0000000002000022
            ,0x0000000000000022
            ,0x0000000000000002
            ,0xFB00BA00BA00BA00
            ,0x2C002A02009F0001
            ,0x27040C002000006B
            ,0x0033002000280220
            ,0x0200009B0B0000BB
            ,0x02000000000000BB
            ,0x00000000000000BB
            ,0x000000000B0000BB
            ,0x0000028000000B20
            ,0x0000028000000000
            ,0x003A07000070EF30
            ,0x0035A1D002D00020
            ,0x0000040000000000
            ,0x0000040000000005
            ,0x0F0000000B0000BB
            ,0x00A300A00B0000BB
            ,0x000000A00B0000BB
            ,0x0800800020000000
            ,0x0800800000000000
            ,0x0070518000000000
            ,0x0000600000000000
            ,0x8002E50000080008
            ,0x8002E5E020080008
            ,0xF000000000000000
            ,0x0004008F00000B00
            ,0x0400000000020A67
            ,0x0400310F00020667
            ,0x00080800007C0880
            ,0x00080800007C4C80
            ,0x427060F020000000
            ,0x000000000F0202FF
            ,0x00000000000202FF
            ,0xA1D61D0000050000
            ,0x0800022000020222
            ,0x0700200002620022
            ,0x00008BB6000B0B00
            ,0x000000B6000B0B00
            ,0x3C300006000B0B70
            ,0x0000000B000B0B00
            ,0x0000000000000B00
            ,0xC00012101000D0B0
            ,0x0005001115000000
            ,0x0005001111000000
            ,0xC00200200100E00B
            ,0x59009000110B3001
            ,0x0600000400000300
            ,0x0000060107000000
            ,0xC050B00CC0C000A0
            ,0x0050B00CC0C000AC
            ,0x00000007001202B0
            ,0x11110100001202B0
            ,0x11110100000000B0
]




##// Plain
Tweak = 0x54CD94FFD0670A58  ##// Tweak
Key_0 = 0x27A6781A43F364BC  ##// Key 0
Key_1 = 0x916708D5FBB5AEFE  ##// Key 1
i = 0
j = 0
TK = {}

#TRUEC = 0x590e8e03289c0d4b  ##true ciphertext
dec=1
for d in range (194):
        def initialize():
            for i in range(16):
                Stt[i] = ((Plain >> (4 * (15 - i))) & 0xf)
                Sttf[i] = (((Plainfulty[d]^Plain ) >> (4 * (15 - i))) & 0xf)

            for i in range(16):
                TK[0, i] = ((Key_0 >> (4 * (15 - i))) & 0xf)
            for i in range(16):
                TK[1, i] = ((Key_1 >> (4 * (15 - i))) & 0xf)
            for i in range(16):
                TK[2, i] = TK[0, i]
            for i in range(16):
                TK[3, i] = TK[1, i]

            for i in range(16):
                TK[0, i] ^= ((Tweak >> (4 * (15 - i))) & 0xf)
            for i in range(16):
                TK[1, i] ^= ((Tweak >> (4 * (15 - i))) & 0xf)
            for i in range(16):
                TK[2, i] ^= ((Tweak >> (4 * (15 - Q[i]))) & 0xf)
            for i in range(16):
                TK[3, i] ^= ((Tweak >> (4 * (15 - Q[i]))) & 0xf)

            if (dec == 1):
                    for j in range (4):
                        for i in range (4):
                            TK[j,i] ^= ( (TK[j,i + 8]) ^ (TK[j,i + 12]))
                            TK[j,i + 4] ^= TK[j,i + 12]




        def Round(r):
            # MixColumn
            counter = 0
            kepper = {}
            for i in range(4):
                Stt[i] ^= (Stt[i + 8] ^ Stt[i + 12])
                Stt[i + 4] ^= Stt[i + 12]
                Sttf[i] ^= (Sttf[i + 8] ^ Sttf[i + 12])
                Sttf[i + 4] ^= Sttf[i + 12]
            for i in range(16):
                kepper[i] =  Sttf[i]^Stt[i]
            for i in range(16):
                if (kepper[i]>0x0):
                    counter = counter +1
            if (counter<=5):
                print("round number : ", r)
                print("subfunction : MixC ")
                print("vector",d)
            counter = 0
            # AddConstant
            ind = r
            if dec:
                ind = R - r
            Stt[4] ^= RC4[ind]
            Stt[5] ^= RC3[ind]
            Sttf[4] ^= RC4[ind]
            Sttf[5] ^= RC3[ind]
            for i in range(16):
                kepper[i] = Sttf[i] ^ Stt[i]
            for i in range(16):
                if (kepper[i] > 0x0):
                    counter = counter + 1
            if (counter <= 5):
                print("round number : ", r)
                print("subfunction : AddConstant")
                print("vector", d)
            counter = 0
            # AddTweakey
            for i in range(16):
                Stt[i] ^= TK[ind % 4, i]
                Sttf[i] ^= TK[ind % 4, i]
            for i in range(16):
                kepper[i] = Sttf[i] ^ Stt[i]
            for i in range(16):
                if (kepper[i] > 0x0):
                    counter = counter + 1
            if (counter <= 5):
                print("round number : ", r)
                print("subfunction : AddTweakey")
                print("vector", d)
            counter = 0
            # Permutation
            Temp = {}
            Tempf = {}
            for i in range(16):
                Temp[P[i]] = Stt[i]
                Tempf[P[i]] = Sttf[i]
            for i in range(16):
                kepper[i] = Sttf[i] ^ Stt[i]
            for i in range(16):
                if (kepper[i] > 0x0):
                    counter = counter + 1
            if (counter <= 5):
                print("round number : ", r)
                print("subfunction : Permutation")
                print("vector", d)
            counter = 0

            for i in range(16):
                Stt[i] = S[Temp[i]]
                Sttf[i] = S[Tempf[i]]
            for i in range(16):
                kepper[i] = Sttf[i] ^ Stt[i]
            for i in range(16):
                if (kepper[i] > 0x0):
                    counter = counter + 1
            if (counter <= 5):
                print("round number : ", r)
                print("subfunction : SBox")
                print("vector", d)
            counter = 0



        def HalfRound(r):
            # MixColumn
            counter = 0
            kepper= {}
            for i in range(4):
                Stt[i] ^= (Stt[i + 8] ^ Stt[i + 12])
                Stt[i + 4] ^= Stt[i + 12]

                Sttf[i] ^= (Sttf[i + 8] ^ Sttf[i + 12])
                Sttf[i + 4] ^= Sttf[i + 12]
            for i in range(16):
                kepper[i] = Sttf[i] ^ Stt[i]
            for i in range(16):
                if (kepper[i] > 0x0):
                    counter = counter + 1
            if (counter <= 5):
                print("round number : ", r)
                print("subfunction : MixColumn last round")
                print("vector", d)
            counter = 0
            # AddConstant
            ind = r
            if dec:
                ind = R - r
            Stt[4] ^= RC4[ind]
            Stt[5] ^= RC3[ind]
            Sttf[4] ^= RC4[ind]
            Sttf[5] ^= RC3[ind]

            for i in range(16):
                kepper[i] = Sttf[i] ^ Stt[i]
            for i in range(16):
                if (kepper[i] > 0x0):
                    counter = counter + 1
            if (counter <= 5):
                print("round number : ", r)
                print("subfunction : AddConstant last round")
                print("vector", d)
            # AddTweakey
            for i in range(16):
                Stt[i] ^= TK[ind % 4, i]
                Sttf[i] ^= TK[ind % 4, i]
            for i in range(16):
                kepper[i] = Sttf[i] ^ Stt[i]
            for i in range(16):
                if (kepper[i] > 0x0):
                    counter = counter + 1
            if (counter <= 5):
                print("round number : ", r)
                print("subfunction : AddTweakey last round")
                print("vector", d)
            #PT = "0x"
            #PTf = "0x"
            # Next State
            #print()
            #print("Plain text : ", R);
            #for i in range(16):
                #PT = PT + (str(hex(Stt[i]))[2])
            #print(PT)
            #print("Plain text f : ", R);
            #for i in range(16):
                #PTf = PTf + (str(hex(Sttf[i]))[2])
            #print(PTf)



        def main():
            r = 0
            rf = 0
            #print("_CRAFT_")
            initialize()
            print()
            print()
            for r in range(R):
                Round(r)
            HalfRound(R)
            print()
        if __name__ == "__main__":
            main()


print(":)")
