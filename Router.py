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

class Interface():
    def __init__(self, attached_router, port_type, port_number):
        self.attached_router = attached_router
        self.port_type = port_type
        self.port_number = port_number
