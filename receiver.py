from common import *


class receiver:
    ACK = 1

    expectedSeqNum = 0

    def isCorrupted(self, packet):
        #  Check if a received packet has been corrupted during transmission.
        # Return true if computed checksum is different than packet checksum.
        # 3 points
        sum = packet.seqNum + packet.ackNum
        for c in packet.payload:
            sum += ord(c)

        if sum == packet.checksum:
            return False

        return True

    def isDuplicate(self, packet):
        # check if packet sequence number is the same as expected sequence number
        # 2 points
        if packet.seqNum == self.expectedSeqNum:
            return False
        return True

    def getNextExpectedSeqNum(self):
        # Use modulo-2 arithmetic to ensure sequence number is 0 or 1.
        # 2 points
        self.expectedSeqNum += 1
        self.expectedSeqNum %= 2
        return self.expectedSeqNum

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing receiver: B: " + str(self.entity))

    def init(self):
        # initialise expected packet sequence number
        # 2 points
        self.expectedSeqNum = 0
        return

    def input(self, packet):
        # This method will be called whenever a packet sent from the sender
        # arrives at the receiver.

        # If packet is corrupted or duplicate: send ACK with wrong sequence number.
        if self.isCorrupted(packet) or self.isDuplicate(packet):
            packet.payload = ''
            packet.ackNum += 1
            packet.ackNum %= 2
            packet.checksum = packet.seqNum + packet.ackNum
            self.networkSimulator.udtSend(B, packet)
            return

        # If packet is OK, deliver it and send correct ACK.
        # update expected sequence number
        # 12 points
        self.networkSimulator.deliverData(B, packet.payload)
        packet.payload = ''
        packet.checksum = packet.seqNum + packet.ackNum
        self.networkSimulator.udtSend(B, packet)
        self.expectedSeqNum = self.getNextExpectedSeqNum()

        return
