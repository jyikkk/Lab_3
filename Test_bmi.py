import Lab_2.bmi as bmi

def test_bmi_normal_weight():
    assert (bmi.calculate_bmi(1.76, 60) == 0)
def test_bmi_over_weight():
    assert (bmi.calculate_bmi(1.76, 100) == 1)
def test_bmi_under_weight():
    assert (bmi.calculate_bmi(1.76, 40) == -1)