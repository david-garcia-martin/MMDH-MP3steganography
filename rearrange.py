from processbit import *

class rearrange:

    def __init__(self):
        self.create_mp3_file()

    def create_mp3_file(self):
        f = open('final.mp3',"wb")

        for key in processbit.final_dictionary.keys():
            if key=="Morralla_1":
                morralla_1_hex = hex(int(processbit.final_dictionary[key],2))
                f.write(morralla_1_hex[2:-1])
        for key in sorted(processbit.final_dictionary.keys()):
            if key!="Morralla_1":
                values = hex(int(processbit.final_dictionary[key],2))
                f.write(values[2:-1])
        f.close()





