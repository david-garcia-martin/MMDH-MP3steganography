from processbit import *
import codecs

"""pablo = 01110000 01100001 01100010 01101100 01101111 00001010"""

class changebits:
    message = "011100000110000101100010011011000110111100001010"
    def __init__(self,position):
        #self.change()
        self.change_v1bit(position)
        self.write_mp3()

    def split(self,arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs

    def change(self):
        cnt = 0
        "Separate the message into blocks of 8 bits"
        array_blocks = self.split(self.message, 8)
        for key in sorted(processbit.final_dictionary.keys()):
            if key!="Morralla_1":
                "This is for changing the last 20 bits of each frame"
                """
                if processbit.final_dictionary[key][len(processbit.final_dictionary[key])-1] == "1":
                    processbit.final_dictionary[key] = processbit.final_dictionary[key][:-20] + "00000000000000000000"
                    print (processbit.final_dictionary[key][len(processbit.final_dictionary[key])-1])
                    print (len(processbit.final_dictionary[key]))
                elif processbit.final_dictionary[key][len(processbit.final_dictionary[key])-1] == "0":
                    processbit.final_dictionary[key] = processbit.final_dictionary[key][:-20] + "00000000000000000000"
                    print (processbit.final_dictionary[key][len(processbit.final_dictionary[key]) - 1])
                    print (len(processbit.final_dictionary[key]))
                """

                if(cnt<len(array_blocks)):
                    processbit.final_dictionary[key] = processbit.final_dictionary[key][:-8] + array_blocks[cnt]
                    cnt += 1

    def change_v1bit(self,position):
        for key in sorted(processbit.final_dictionary.keys()):
            if key != "Morralla_1":
                if processbit.final_dictionary[key][position] =="1":
                    processbit.final_dictionary[key] = processbit.final_dictionary[key][:position] + "0" + processbit.final_dictionary[key][position+1:]
                elif processbit.final_dictionary[key][position] =="0":
                    processbit.final_dictionary[key] = processbit.final_dictionary[key][:position] + "1" + processbit.final_dictionary[key][position + 1:]

    def write_mp3(self):
        f = open('final.mp3', "wb")
        for key in processbit.final_dictionary.keys():
            if key == "Morralla_1":
                morralla_1_hex = hex(int(processbit.final_dictionary[key], 2))
                morralla_1_ascii = codecs.decode(morralla_1_hex[2:-1], "hex")
                f.write(morralla_1_ascii)
        for key in sorted(processbit.final_dictionary.keys()):
            if key != "Morralla_1":
                values_hex = hex(int(processbit.final_dictionary[key], 2))
                values_ascii = codecs.decode(values_hex[2:-1], "hex")
                f.write(values_ascii)
        f.close()




