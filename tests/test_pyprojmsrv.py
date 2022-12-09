"""
Template's unit tests
"""


from src.pyprojmsrv import pyprojmsrv


def test_main():
    """Test main"""

    pyprojmsrv.main()


def test_greeting():
    """Test greeting"""

    output = pyprojmsrv.greeting("ppmstest")
    assert output == "Hello ppmstest"
