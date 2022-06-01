from src.binary_converter import binary_converter

def testBinaryConverter():
    assert binary_converter(1) == "0b1"
    assert binary_converter(10) == "0b1010"
    assert binary_converter(64) == "0b1000000"
    assert binary_converter(15) == "0b1111"

def main():
    testBinaryConverter()

main()
    