from processbit import processbit
from extractInformation import extractInformation
from rearrange import rearrange
from changebits import changebits
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
    extractInformation()
    position = input("\nInsert the position of the bit you want to change:")
    changebits(position)
    #rearrange()
