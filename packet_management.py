# FRAME_SIZE_BYTES: 32
# FLAG_SIZE_BYTES: 1
# ADDRESS_SIZE_BYTES: 8
# MAX_DATA_SIZE_BYTES: 2
# DATA: 0100001001101001011001010110111000100001
# TO_ADDRESS: DNI de un miembro de la pareja
# FROM_ADDRESS: DNI del otro miembro de la pareja
# START_FLAG: 10111000
# END_FLAG: 11000011


message_data = "100001001101001011001010110111000100001" #Lo pasamos como string?
max_data_size_bits = 16 #16 bits = 2 bytes

def dataSegmentation(message_data, max_data_size_bits):
    print("FUNCION DE DIVIDIR TRAMOS")
    segmented_message = [message_data[i : i + max_data_size_bits] for i in range(0, len(message_data), max_data_size_bits)]
    
    print( "Segmented message:", segmented_message)
    return segmented_message    
    
def addAddress():
    print("Dir de destino y origen en 8 bytes")

def addBitStuffing():
    print("Insertamos bits en los datos")

def addPadding():
    print("Agregar bits adicionales para alcanzar una longitud")

def addFlags():
    print("Datos de inicio y final")

def concatenateFrames():
    print("Juntar toda la info para que un solo mensaje sea transmitido")
    
def sendMessage():
    print("MENSAJE")
    
dataSegmentation(message_data,max_data_size_bits)