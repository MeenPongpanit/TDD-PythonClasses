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

test_list = [
    test_create_router,
    test_named_router,
    test_fullinfo_router,
    test_add_interface
]

for test in test_list:
    test()
