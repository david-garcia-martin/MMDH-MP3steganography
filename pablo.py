import binascii

class processbit:
    bits_before_1frame = []
    final_dictionary = {}

    def __init__(self, filename):
        binary = ""
        binary_array = []

        f = open(filename, "rb")
        with f:
            # el numero dentro del parentesis representa la PAREJA DE HEX que se lee
            byte = f.read()
            hexadecimal = binascii.hexlify(byte)
            for i in range(0, len(hexadecimal)):
                binary += bin(int(hexadecimal[i], 16))[2:].zfill(4)
            f.close()
            # print("hex: %s, decimal: %s, binary: %s" % (hexadecimal, decimal, binary))
            # print("hex: %s, binary: %s" % (hexadecimal, binary))
            '''
            print("cadena hex ---> " + str(hexadecimal))
            print("cadena bin ---> " + binary)'''

            # Paso a array el String
            for i in binary:
                binary_array.append(i)

            print("AKJSHDKJAHSKDJHAaKJSaAKJSD  " + str(len(binary_array)))
            self.find_next_syncword(binary_array)

    def find_next_syncword(self, binary_array):
        contador, pos, n_frame = 0, 0,0
        aux=""
        cnt = 0
        for i in range(11, len(binary_array)):
            pos += 1
            aux += str(binary_array[i - 11])
            if (binary_array[i] == "1") and (binary_array[i - 1] == "1") and (binary_array[i - 2] == "1"):
                if (binary_array[i - 3] == "1") and (binary_array[i - 4] == "1") and (binary_array[i - 5] == "1"):
                    if (binary_array[i - 6] == "1") and (binary_array[i - 7] == "1") and (binary_array[i - 8] == "1"):
                        if (binary_array[i - 9] == "1") and (binary_array[i - 10] == "1"):
                            contador+=1
                            if contador==1:
                                print("\n--------- FRAME " + str(n_frame) + "-------------")
                                n_frame += 1
                                self.final_dictionary["Morralla_1"] =aux
                                aux=""
                            if (len(aux) > 3000):
                                if (cnt==0):
                                    cnt+=1
                                    self.final_dictionary["Morralla_1"] =  self.final_dictionary["Morralla_1"] + aux
                                    print("Length of unuseful bits ----> "+str(len(self.final_dictionary["Morralla_1"])))
                                    print("Morralla_1: " + str(self.final_dictionary["Morralla_1"])+"\n")
                                print("\n--------- FRAME " + str(n_frame) + "-------------")
                                print("\tSyncword starts at ---> " + str(pos + 1))
                                print("\tLength of frame ---> " + str(len(aux)))
                                self.final_dictionary[str(n_frame)] = aux
                                n_frame += 1
                                aux=""

        print("\nTotal number of frames: "+str(n_frame))
        print(str(self.final_dictionary["1"]))


if __name__ == '__main__':
    print(" \n====================== MMDH v.01 ====================== ")

    src_filename = input("Insert input filename[sample.mp3]:")
    if (src_filename == ""):
        src_filename = "sample.mp3"
    """dst_filename = input("Insert output filename[bitstream.json]:")
    if (dst_filename == ""):
        dst_filename = "bitstream.json"
    frame_cnt_limit = int(input("Insert limit number of frames decoded(0=no_limit)[100]:"))
    if (frame_cnt_limit == ""):
        frame_cnt_limit = 100
    """
    print("\nLoading MP3 into memory...")

    p = processbit(src_filename)
