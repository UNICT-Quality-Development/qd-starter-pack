import src.ex3 as ex3
from pytest_mock import MockerFixture

def test_main(mocker : MockerFixture) -> None:
    #arrange  
    expected_outputs = ["44th president of the United States", "Former President of the Italian Republic", "Former President of South Africa", "Bapu", "Creator of LaTeX", "Creator of C", "Invalid input! Please enter a good name!"]
    spy = mocker.spy(ex3, "main");

    #act
    actual_outputs = []
    for name in expected_outputs:
        actual_outputs.append(ex3.main(name))
    
    #assert
    assert ex3.main("BarackObama") == "44th president of the United States"
    assert ex3.main("SandroPertini") == "Former President of the Italian Republic"
    assert ex3.main("NelsonMandela") == "Former President of South Africa"
    assert ex3.main("MahatmaGandhi") == "Bapu"
    assert ex3.main("DonaldKnuth") == "Creator of LaTeX"
    assert ex3.main("DennisRitchie") == "Creator of C"
    assert ex3.main("InvalidName") == "Invalid input! Please enter a good name!"

    assert spy.call_count == 7
    assert spy.spy_return == expected_outputs
