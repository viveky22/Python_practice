class Testcheck:
    def test_a(self):
        assert type(4) == int
        
    def test_b(self):
        assert str.upper('python') == 'PYTHON'


# To run particular test in class : - py.test test_class.py::Testcheck::test_b -v -s
