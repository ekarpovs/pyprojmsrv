"""
Template's unit tests
"""


from pyprojmsrv import msrv


def test_main():
    """Test main"""

    msrv.main()


def test_greeting():
    """Test greeting"""

    output = msrv.greeting("ppmstest")
    assert output == "Hello ppmstest"
