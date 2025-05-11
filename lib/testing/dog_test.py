#!/usr/bin/env python3

from dog import Dog

import io
import sys
import types


class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog("Dog")
        assert (type(fido) == Dog)


class TestBark:
    '''Dog.bark() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog("Dog")
        assert (type(fido.bark) == types.MethodType)

    def test_prints_woof(self):
        '''prints "Woof!"'''
        fido = Dog("Dog")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.bark()
        sys.stdout = sys.__stdout__
        assert (captured_out.getvalue() == "woof!\n")


class TestSit:
    '''Dog.sit() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog("Dog")
        assert (type(fido.sit) == types.MethodType)

    def test_prints_the_dog_is_sitting(self):
        '''prints "The dog is sitting."'''
        fido = Dog("Dog")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.sit()
        print(f"{fido.name} is sitting.")
        sys.stdout = sys.__stdout__
        assert (captured_out.getvalue() == "Dog is sitting.\n")
