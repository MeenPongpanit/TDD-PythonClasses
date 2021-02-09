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
    assert router1.interfaces.get('G0/0').connected_interface.attached_router.name == 'Test name 2', 'test failed'


test_list = [
    test_create_router,
    test_named_router,
    test_fullinfo_router,
    test_add_interface,
    test_view_interface_router,
    test_connect_interface
]

for test in test_list:
    test()
