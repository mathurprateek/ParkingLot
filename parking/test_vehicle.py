from unittest import TestCase
from unittest import mock
from parking.vehicle import Vehicle

class TestVehicle(TestCase):
    def test_parking_lot_color(self):
        with mock.patch('builtins.input', return_value='red'):
            v = Vehicle('reg1', 'car')
            self.assertEqual(v.reg_num, 'reg1')
            self.assertEqual(v.vehicle_type, 'car')
            self.assertEqual(v.color, 'red')

    def test_parking_lot_make(self):
        with mock.patch('builtins.input', return_value='mnm'):
            v = Vehicle('reg1', 'car')
            self.assertEqual(v.reg_num, 'reg1')
            self.assertEqual(v.vehicle_type, 'car')
            self.assertEqual(v.make, 'mnm')

    def test_parking_lot_repr(self):
        with mock.patch('builtins.input', return_value=''):
            v = Vehicle('reg1', 'car')
            self.assertEqual(v.reg_num, 'reg1')
            self.assertEqual(v.vehicle_type, 'car')
            self.assertEqual(v.__repr__(), 'Registration Number: reg1, Color: , Make: , Vehicle Type: car')        
