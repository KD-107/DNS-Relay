class DNS_query():
    def __init__(self,data):
        Msg_arr = bytearray(data)
        QNAME_STRAT = 12
        Qname = bytearray()
        while Msg_arr[QNAME_STRAT] != 0:
            Qname = Qname + Msg_arr[QNAME_STRAT+1:QNAME_STRAT + 1 + Msg_arr[QNAME_STRAT]]
            QNAME_STRAT = QNAME_STRAT + 1 + Msg_arr[QNAME_STRAT]
        Qname = Qname + bytearray([0])
        QTYPE_START = QNAME_STRAT + 1
        Qtype = Msg_arr[QTYPE_START:QTYPE_START + 2]
        QCLASS_START = QTYPE_START + 2
        Qclass = Msg_arr[QCLASS_START:QCLASS_START + 2]

        self.name = Qname
        self.name_length = len(Qname)
        self.qtype = Qtype
        self.qclass = Qclass

    def name(self):
        return self.name,self.name_length



