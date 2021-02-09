"""Unit Test for Router Module"""
import pytest
import Router

def test_create_router():
    assert  Router.Router(), "test failed"

def test_named_router():
    name = "Test Name"
    router1 = Router.Router(name)
    assert router1.name == name, "test failed"

def test_fullinfo_router():
    name = "Test Name"
    model = "Test Model"
    vendor = "Test Vendor"
    router1 = Router.Router(name, model, vendor)
    assert router1.name == name, 'test failed'
    assert router1.model == model, 'test failed'
    assert router1.vendor == vendor, 'test failed'

def test_add_interface():
    router1 = Router.Router('Test name', 'Test Model', 'Test vendor')
    router1.add_interface('Gigabit Ethernet', '0/0')
    assert router1.interfaces.get('G0/0', False), 'test failed'

def test_view_interface_router():
    router1 = Router.Router('Test name', 'Test Model', 'Test vendor')
    router1.add_interface('Gigabit Ethernet', '0/0')
    assert router1.interfaces.get('G0/0').attached_router.name == 'Test name', 'test failed'

def test_connect_interface():
    router1 = Router.Router('Test name 1', 'Test Model 1', 'Test vendor 1')
    router2 = Router.Router('Test name 2', 'Test Model 2', 'Test vendor 2')
    router1.add_interface('Gigabit Ethernet', '0/0')
    router2.add_interface('Gigabit Ethernet', '0/1')
    router1.connect_interface('G0/0', router2.interfaces.get('G0/1'))
    assert router1.interfaces.get('G0/0').connected_interface.attached_router == router2, 'test failed'
    assert router2.interfaces.get('G0/1').connected_interface.attached_router == router1, 'test failed'

def test_assign_ip_int():
    router1 = Router.Router('Test name 1', 'Test Model 1', 'Test vendor 1')
    router1.add_interface('Gigabit Ethernet', '0/0')
    router1.assign_ip_int('G0/0', '172.168.1.1', '255.255.255.0')
    assert router1.interfaces.get('G0/0').ip_address == '172.168.1.1', 'test failed'
    assert router1.interfaces.get('G0/0').subnet_mask == '255.255.255.0', 'test failed'

def test_stringify_router():
    router1 = Router.Router('Test name 1', 'Test Model 1', 'Test vendor 1')
    router1_string = "Router Name:%s\nModel:%s\nVendor:%s\nThis Router has no interface."%('Test name 1', 'Test Model 1', 'Test vendor 1')
    assert str(router1) == router1_string, 'test failed'

def test_stringify_router_with_interfaces():
    router1 = Router.Router('Test name 1', 'Test Model 1', 'Test vendor 1')
    router1_string = "Router Name:%s\nModel:%s\nVendor:%s\n"%('Test name 1', 'Test Model 1', 'Test vendor 1')
    router1.add_interface('Gigabit Ethernet', '0/0')
    router1.add_interface('Gigabit Ethernet', '0/1')
    router1.add_interface('Gigabit Ethernet', '1/0')
    router1.assign_ip_int('G0/0', '172.168.1.1', '255.255.255.0')
    router1_string += "Interfaces:\tType\t\t\tPortNum\t\tIP\t\tMask\n"
    router1_string += "\t\tGigabit Ethernet\t0/0\t\t172.168.1.1\t255.255.255.0\n"
    router1_string += "\t\tGigabit Ethernet\t0/1\t\tnot assign\tnot assign\n"
    router1_string += "\t\tGigabit Ethernet\t1/0\t\tnot assign\tnot assign"

    print(router1)

    assert router1_string == str(router1), 'test failed'




test_list = [
    test_create_router,
    test_named_router,
    test_fullinfo_router,
    test_add_interface,
    test_view_interface_router,
    test_connect_interface,
    test_assign_ip_int,
    test_stringify_router,
    test_stringify_router_with_interfaces
]

for test in test_list:
    test()
