from common import *


class sender:
    ACK = 0
    RTT = 20

    currentSeqNum = 0
    currentPacket = None

    def isCorrupted(self, packet):
        #  Check if a received packet (ACK) has been corrupted during transmission.
        # similar to the corresponding function in receiver side
        # 3 points
        sum = packet.seqNum + packet.ackNum
        if packet.checksum == sum:
            return False
        return True

    def isDuplicate(self, packet):
        # checks if an ACK is duplicate or not
        # similar to the corresponding function in receiver side
        # 2 points
        if packet.ackNum == self.currentSeqNum:
            return False
        return True

    def getNextSeqNum(self):
        # generate the next sequence number to be used
        # similar to the corresponding function in receiver side
        # 2 points
        self.currentSeqNum += 1
        self.currentSeqNum %= 2
        self.ACK = self.currentSeqNum
        return self.currentSeqNum

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: " + str(self.entity))

    def init(self):
        # initialize the currentSeqNum  and currentPacket
        # 4 points
        self.currentSeqNum = 0
        self.currentPacket = None
        return

    def timerInterrupt(self):
        # what the sender does in case of timer interrupt?
        # It sends the packet again.
        # It starts the timer, sets the timeout value to be twice the RTT
        # 6 points
        self.networkSimulator.udtSend(A, self.currentPacket)
        self.networkSimulator.startTimer(A, 2 * self.RTT)
        return

    def output(self, message):
        # if current packet is not transmitted ignore the message
        # else prepare a packet and send it through the network layer
        # call utdSend
        # start the timer
        # 12 points
        checksum = self.currentSeqNum + self.ACK
        for m in message.data:
            checksum += ord(m)

        self.currentPacket = Packet(self.currentSeqNum, self.ACK, checksum, message.data)
        self.networkSimulator.udtSend(A, self.currentPacket)
        self.networkSimulator.startTimer(A, self.RTT)
        return

    def input(self, packet):
        # If ACK isn't corrupted or duplicate, transmission complete.
        # so the currentPacket should be set to None
        # You do not need to do anything else.
        if not self.isDuplicate(packet) and not self.isCorrupted(packet):
            self.networkSimulator.stopTimer(A)
            self.currentPacket = None
            self.currentSeqNum = self.getNextSeqNum()
            return
        # In the case of duplicate ACK the packet will be sent again.
        # since you do not change the current packet in that case
        # 8 points
        self.networkSimulator.udtSend(A, packet)
        return
