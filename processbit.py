import binascii

class processbit:
    bits_before_1frame = []
    final_dictionary = {}

    def __init__(self, filename):
        binary = ""
        binary_array = []
        prueba_binary_array=[]

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
            self.prueba_binary_array=binary_array
            print("Total number of bits founded in file: " + str(len(binary_array)))
            self.find_next_syncword(binary_array)

    def find_next_syncword(self, binary_array):
        contador, pos, n_frame ,index= 0,0,0,1
        aux,string_frame="",""
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
                                #print("\n--------- FRAME " + str(n_frame) + "-------------")
                                #print("FRAME POSITION: ")
                                n_frame += 1
                                self.final_dictionary["Morralla_1"] =aux
                                aux=""
                            if (len(aux) > 3000):
                                if (cnt==0):
                                    cnt+=1
                                    self.final_dictionary["Morralla_1"] =  self.final_dictionary["Morralla_1"] + aux
                                    print("Length of unuseful bits: "+str(len(self.final_dictionary["Morralla_1"])))
                                    #print("Morralla_1: " + str(self.final_dictionary["Morralla_1"])+"\n")
                                break

        self.prueba_binary_array=self.prueba_binary_array[len(self.final_dictionary["Morralla_1"]):]

        array_frames=self.split((self.prueba_binary_array),3344)
        print("Length of each frame: " + str(len(array_frames[0])) + " bits")

        for i in range(0, len(array_frames)):
            for j in range(0, len(array_frames[i])):
                string_frame+=array_frames[i][j]
            self.final_dictionary[index]=string_frame
            index += 1
            string_frame=""

        "Accessing to bits and length of frame 1"
        #print(str(self.final_dictionary[1]))
        #print(len(self.final_dictionary[1]))

    def split(self,arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs
