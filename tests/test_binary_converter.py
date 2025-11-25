from src.binary_converter import decimal2binary


def test_decimal2binary() -> None:
    assert decimal2binary(0) == "0"
    assert decimal2binary(8) == "1000"
    assert decimal2binary(10) == "1010"
    try:
        decimal2binary(-5)
        assert False
    except ValueError as _:
        assert True
