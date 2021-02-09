"""Unit Test for Router Module"""
import pytest
import Router

def test_create_router():
    assert  Router.Router(), "test failed"

def test_named_router():
    name = "Test Name"
    router1 = Router.Router(name)
    assert router1.name == name, "test failed"

test_list = [
    test_create_router,
    test_named_router
]

for test in test_list:
    test()
