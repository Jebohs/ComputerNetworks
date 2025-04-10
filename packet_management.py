# FRAME_SIZE_BYTES: 32
# FLAG_SIZE_BYTES: 1
# ADDRESS_SIZE_BYTES: 8
# MAX_DATA_SIZE_BYTES: 2
# DATA: 0100001001101001011001010110111000100001
# TO_ADDRESS: info 1
# FROM_ADDRESS: info 2
# START_FLAG: 10111000
# END_FLAG: 11000011


message_data = "0100001001101001011001010110111000100001" #We send it as a string?
max_data_size_bits = 16 #16 bits = 2 bytes

def data_segmentation(message_data, max_data_size_bits):
    print("Function to divide the data into smaller parts to send it later")
    segmented_message = [message_data[i : i + max_data_size_bits] for i in range(0, len(message_data), max_data_size_bits)]
    print( "Segmented message:", segmented_message)
    return segmented_message    
    
def add_address(segmented_message,address_destination,address_origin):
    #Final print -> [Dest Ori (SEGMENT),Desti Origi (SEGMENT)]
    
    message_with_address = []
    for segment in segmented_message:
        temp_string = ''+ address_destination + address_origin + segment
        message_with_address.append(temp_string)
    print("Message with DESTINATION and ORIGIN: ", message_with_address)
    return message_with_address


def add_bit_stuffing():
    print("Add bits to the beginning and end of the data")

def add_padding():
    print("Fill up the data with aditional bits in order to reach the needed length for the package")

def add_flags():
    print("Start and end flags")

def join_frames():
    print("Join up all the information together")
    
def send_message():
    print("MESSAGE:")


#Actual program runs here
    
address_origin = "0011000000110001001100010011100000110111001101000011011000110100_" #Felix. remove '_' its for debugging
address_destination = "0011000000110011001101010011000000110011001100110011100100110000_" #Roman, remove '_' ***
add_address(data_segmentation(message_data,max_data_size_bits),address_destination,address_origin) #Change up later?