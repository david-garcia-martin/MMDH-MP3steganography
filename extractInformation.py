from processbit import *
from MMDH_tables import *

boolean_morralla = False
class extractInformation:
    def __init__(self):
        self.decode_frame_header()

    def decode_frame_header(self):
        for key in sorted(processbit.final_dictionary.keys()):
            "No key and value, too long. Just key."
            if key=="Morralla_1" and boolean_morralla:
                print("Previous information of frame 1: "+str(processbit.final_dictionary[key][1]))
            elif key!="Morralla_1":
                mpeg_version = mp3_hdr_ver_tbl[processbit.final_dictionary[key][12]]
                layer = mp3_hdr_layer_tbl[processbit.final_dictionary[key][13]+processbit.final_dictionary[key][14]]
                hasCRC = True
                if processbit.final_dictionary[key][15]=="1":
                    hasCRC=False
                bitrate = mp3_hdr_bitrate_tbl[processbit.final_dictionary[key][16]+processbit.final_dictionary[key][17]+processbit.final_dictionary[key][18]+processbit.final_dictionary[key][19]]
                sample_rate= mp3_hdr_smpl_rate_tbl[processbit.final_dictionary[key][20]+processbit.final_dictionary[key][21]]
                padding = True
                if processbit.final_dictionary[key][22]=="0":
                    padding = False
                channel_mode = mp3_hdr_channel_mode_tbl[processbit.final_dictionary[key][24]+processbit.final_dictionary[key][25]]
                if (channel_mode == "mono"):
                   n_channels = 1
                else:
                    n_channels = 2
                print("\nFrame #"+str(key))
                print("\tFrame header info")
                print("\t\tVersion: " + str(mpeg_version))
                print("\t\tLayer: "+str(layer))
                print("\t\tHas CRC?: "+str(hasCRC))
                print("\t\tBitrate(kps): "+str(bitrate))
                print("\t\tSample Rate: "+str(sample_rate))
                print("\t\tPadding: " +str(padding))
                print("\t\tChannel Mode: "+str(channel_mode))
                print("\t\tNumber of channels: "+str(n_channels))
        
                main_data =processbit.final_dictionary[key][32]+processbit.final_dictionary[key][33]+processbit.final_dictionary[key][34]+processbit.final_dictionary[key][35]+processbit.final_dictionary[key][36]+processbit.final_dictionary[key][37]+processbit.final_dictionary[key][38]+processbit.final_dictionary[key][39]+processbit.final_dictionary[key][40]
                print("\tMain data begins in position : " + str(int(main_data,2))+" bytes before this frame.")


