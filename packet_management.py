# FRAME_SIZE_BYTES: 32
# FLAG_SIZE_BYTES: 1
# ADDRESS_SIZE_BYTES: 8
# MAX_DATA_SIZE_BYTES: 2
# DATA: 0100001001101001011001010110111000100001
# TO_ADDRESS: info 1
# FROM_ADDRESS: info 2
# START_FLAG: 10111000
# END_FLAG: 11000011


message_data = "100001001101001011001010110111000100001" #We send it as a string?
max_data_size_bits = 16 #16 bits = 2 bytes

def data_segmentation(message_data, max_data_size_bits):
    print("Function to divide the data into smaller parts to send it later")
    segmented_message = [message_data[i : i + max_data_size_bits] for i in range(0, len(message_data), max_data_size_bits)]
    
    print( "Segmented message:", segmented_message)
    return segmented_message    
    
def add_address():
    print("8 byte address TO and FROM")

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
    
data_segmentation(message_data,max_data_size_bits)