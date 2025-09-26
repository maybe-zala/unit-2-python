from main import *

def test_destinations():
    assert destinations("Midgard") == midgard_INFO
    assert destinations("Test")!= f"You cannot go to Test from Midgard!"

def test_adventure():
    assert adventure("Midgard") == True
    assert adventure("Test") != True