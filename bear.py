res[0] = self.ID >> 8
            res[1] = self.ID % 256
            # ......
            res[2] = (self.QR << 7)+self.opcode+self.AA+self.TC+self.RD
            res[3] = self.RA+self.zero+self.rcode
            # question
            res[4] = self.data[4]
            res[5] = self.data[5]
            # answer rrs
            res[6] = self.data[6]
            res[7] = self.data[7]
            # authoritative rrs
            res[8] = self.data[8]
            res[9] = self.data[9]
            # addition rrs
            res[10] = self.data[10]
            res[11] = self.data[11]
            # queries
            for i in range(12, 16 + self.name_length):
                res[i] = self.data[i]
            # ......
            # answer
            # answer_name

            # answer_type
            res[16+self.name_length] = bytearray([0])
            res[17+self.name_length] = bytearray([5])
            # answer_class
            res[18+self.name_length] = bytearray([0])
            res[19+self.name_length] = bytearray([1])
            # answer_ttl
            res[20+self.name_length] = bytearray([0])
            res[21+self.name_length] = bytearray([0])
            res[22+self.name_length] = bytearray([15])
            res[23+self.name_length] = bytearray([15])
            # answer_data_length

            # Authoritative nameservers
            # An_name 2byte

            # An_type 2byte
            res[24+self.name_length] = bytearray([0])
            res[25+self.name_length] = bytearray([5])
            # An_class 2byte
            res[26+self.name_length] = bytearray([0])
            res[27+self.name_length] = bytearray([1])
            # An_ttl 4byte
            res[28+self.name_length] = bytearray([0])
            res[29+self.name_length] = bytearray([0])
            res[30+self.name_length] = bytearray([15])
            res[31+self.name_length] = bytearray([15])
            # An_length 2byte