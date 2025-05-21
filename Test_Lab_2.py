import Lab_2.Lab_2 as L2

def test_min():
    test_list = [0,2,1,-1,-3,5]
    assert(L2.min_temperature(test_list) == -3)

def test_average():
    test_list = [0,2,1,-1,-2]
    assert(L2.calc_average_temp(test_list) == 0)

def test_median():
    test_list = [0,2,1,-1,-2]
    assert(L2.median_temp(test_list) == 0)