from common import *

class receiver:
    ACK = 1
    #expectedSeqNum 
    
    def isCorrupted(self, packet):
        #  Check if a received packet has been corrupted during transmission.
        #Return true if computed checksum is different than packet checksum.
        #3 points
        return
   

    def isDuplicate(self, packet):
        #check if packet sequence number is the same as expected sequence number
        #2 points
        return
   

    def getNextExpectedSeqNum(self):
        #Use modulo-2 arithmetic to ensure sequence number is 0 or 1.
        #2 points
        return
   

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing receiver: B: "+str(self.entity))


    def init(self):
        #initialise expected packet sequence number
        #2 points
        return

    def input(self, packet):
        #This method will be called whenever a packet sent from the sender
        #arrives at the receiver.
        
        # If packet is corrupted or duplicate: send ACK with wrong sequence number.
        #If packet is OK, deliver it and send correct ACK.
        #update expected sequence number
        #12 points
        return
