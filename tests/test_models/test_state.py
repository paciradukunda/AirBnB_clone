#!/usr/bin/python3
"""test the state"""

import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_state_creation(self):
        state = State(name="California")
        self.assertEqual(state.name, "California")

