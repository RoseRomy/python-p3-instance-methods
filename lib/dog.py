#!/usr/bin/env python3

class Dog:
    def __init__(self, name):
        self.name = name
        self.is_sitting = False  # Initialize is_sitting to False

    def bark(self):
        print("woof!")

    def sit(self):
        self.is_sitting = True

    def stand(self):
        self.is_sitting = False
