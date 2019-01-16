import csv
import os


class Firewall:
    file_path = '/Users/tanvibhardwaj/Desktop/illumio/input.csv'
    # parameterized constructor
    def __init__(self, file):
        self.file_path = file
        #print('inside the constructor')
        with open('/Users/tanvibhardwaj/Desktop/illumio/input.csv') as file:
            read_file = csv.reader(file, delimiter=',')
            for line in read_file:
                print(line)

    def display(self):
        print(self.file_path)

    #accept packet function to determine if the traffic is allowed or not
    def accept_packet(self,direction,protocol,port,ip_address):
        self.direction = direction
        self.protocol = protocol
        self.port = port
        self.ip_address = ip_address

        if ((direction == 'inbound' or direction == 'outbound')
                and (protocol == 'tcp' or protocol == 'udp')
                and (0<=port<=65535)
                and (ip_address == '192.168.1.2'or ip_address == '192.168.2.1'or ip_address == '192.168.10.11'or ip_address == '192.168.1.2')):
            return True
        else:
            return False


if __name__ == '__main__':
    #Creating a firewall object
    fw = Firewall('/Users/tanvibhardwaj/Desktop/illumio/input.csv')
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 53, "192.168.1.2"))  # matches third rule
    print(fw.accept_packet("outbound", "tcp", 10234, "192.168.1.2"))  # matches second rule
    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))






