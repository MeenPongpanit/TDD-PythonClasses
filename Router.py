"""Router"""

class Router():
    def __init__(self, name=None, model=None, vendor=None):
        """create router object with specific information"""
        self.name = name
        self.model = model
        self.vendor = vendor
        self.interfaces = dict()
    
    def add_interface(self, port_type, port_number):
        """create interface object and add to router interfaces dict"""
        interface = Interface(self, port_type, port_number)
        short_name = port_type[0] + port_number
        if short_name in self.interfaces:
            print(f'There is {short_name} already.')
        else:
            self.interfaces.update({short_name:interface})

    def connect_interface(self, short_name, target_interface):
        """connect interface with another one"""
        this_interface = self.interfaces.get(short_name)
        this_interface.connected_interface = target_interface
        target_interface.connected_interface = this_interface
    
    def assign_ip_int(self, short_name, ip_address, subnet_mask):
        """assign ip address to specific interface"""
        interface = self.interfaces.get(short_name)
        interface.ip_address = ip_address
        interface.subnet_mask = subnet_mask
    
    def __str__(self):
        """return string that shown all informations of router"""
        router_txt = "Router Name:%s\nModel:%s\nVendor:%s\n"%(self.name, self.model, self.vendor)
        interfaces_txt = '\n'.join(str(interface) for interface in self.interfaces.values())
        if interfaces_txt:
            router_txt += "Interfaces:\tType\t\t\tPortNum\t\tIP\t\tMask\n" + interfaces_txt
        else:
            router_txt+= "This Router has no interface."
        return  router_txt

class Interface():
    def __init__(self, attached_router, port_type, port_number):
        """create interface object with specific values"""
        self.attached_router = attached_router
        self.port_type = port_type
        self.port_number = port_number
        self.connected_interface = None
        self.ip_address = None
        self.subnet_mask = None

    def __str__(self):
        """return string that show all infomations of interface"""
        
        return ("\t\t%s\t%s\t\t%s\t%s"%(self.port_type, self.port_number, self.ip_address, self.subnet_mask)).replace("None", "not assign")
