from mypackage import recursion
from mypackage import sorting

def test_sum_array():
    """make sure sum of array works correctly"""
    assert recursion.sum_arr([1,2,3,4,5,6]) == 21, 'incorrect'
    assert recursion.sum_arr(["a","b","c"]) == "abc", 'incorrect'
    assert recursion.sum_arr([1,2,3,4,5,6]) == 21, 'incorrect'

def test_fibonacci():
    assert recursion.fibonacci(10) == 55, 'incorrect'
    assert recursion.fibonacci(9) == 34, 'incorrect'
    assert recursion.fibonacci(7) == 13, 'incorrect'

def test_factorial():
    assert recursion.factorial(10) == 3628800, 'incorrect'
    assert recursion.factorial(6) == 720, 'incorrect'
    assert recursion.factorial(5) == 120, 'incorrect'

def test_reverse():
    assert recursion.reverse('Hello') == 'olleH', 'incorrect'
    assert recursion.reverse('123') == '321', 'incorrect'
    assert recursion.reverse('Hello Kwazikwakhe Buthelezi') == 'izelehtuB ehkawkizawK olleH', 'incorrect'

def test_bubble_sort():
    assert sorting.bubble_sort([8,2,1,3,5,4]) == [1, 2, 3, 4, 5, 8], 'incorrect'
    assert sorting.bubble_sort(['Kwazi','Buthelezi','Shenge']) == ['Buthelezi', 'Kwazi', 'Shenge'], 'incorrect'
    assert sorting.bubble_sort([8,2,1]) == [1, 2, 8], 'incorrect'

def test_merge_sort():
    assert sorting.merge_sorts([8,2,1,3,5,4]) == [1, 2, 3, 4, 5, 8], 'incorrect'
    assert sorting.merge_sorts(['Kwazi','Buthelezi','Shenge']) == ['Buthelezi', 'Kwazi', 'Shenge'], 'incorrect'
    assert sorting.merge_sorts([8,2,1]) == [1, 2, 8], 'incorrect'


def test_quick_sort():
    assert sorting.quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90], 'incorrect'
    assert sorting.quick_sort(['Kwazi','Buthelezi','Shenge', 'Enzokuhle']) == ['Buthelezi', 'Enzokuhle', 'Kwazi', 'Shenge'], 'incorrect'
    assert sorting.quick_sort([64, 1, 25, 12, 10, 11, 90]) == [1, 10, 11, 12, 25, 64, 90], 'incorrect'
