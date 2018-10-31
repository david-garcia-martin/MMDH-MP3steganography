import codecs

from processbit import *

class rearrange:

    def __init__(self):
        self.create_mp3_file()

    def create_mp3_file(self):
        f = open('final.mp3',"wb")

        for key in processbit.final_dictionary.keys():
            if key=="Morralla_1":
                morralla_1_hex = hex(int(processbit.final_dictionary[key],2))
                morralla_1_ascii = codecs.decode(morralla_1_hex[2:-1],"hex")
                f.write(morralla_1_ascii)
        for key in sorted(processbit.final_dictionary.keys()):
            if key!="Morralla_1":
                values_hex = hex(int(processbit.final_dictionary[key],2))
                values_ascii=codecs.decode(values_hex[2:-1],"hex")
                f.write(values_ascii)
        f.close()






