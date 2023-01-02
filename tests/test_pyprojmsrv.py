"""
Template's unit tests
"""


from pyprojmsrv.msrv import main, greeting


def test_main():
    """Test main"""

    main()


def test_greeting():
    """Test greeting"""

    output = greeting("ppmstest")
    assert output == "Hello ppmstest"
