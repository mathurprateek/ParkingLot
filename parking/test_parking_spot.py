from unittest import TestCase
from unittest.mock import patch
from parking import parking_spot


class TestParkingSpot(TestCase):
    lot_size1 = '-1'
    entry_slots1 = '1 5 9'
    lot_size2 = '10'
    lot_size3 = '\n'
    lot_size4 = 'we'
    reg_num1 = 'reg1'
    criteria_q = 'q'

    @patch('builtins.input', side_effect=[lot_size2, entry_slots1])
    def test_parking_lot_entry_slots_setup(self, mock_inputs):
        parking_spot.parking_lot_entry_slots_setup()

    @patch('builtins.input', side_effect=[lot_size1, entry_slots1, lot_size2, entry_slots1])
    def test_parking_lot_entry_slots_setup_else_coverage(self, mock_inputs):
        parking_spot.parking_lot_entry_slots_setup()

    @patch('builtins.input', side_effect=[lot_size3, lot_size2, entry_slots1])
    def test_parking_lot_entry_slots_setup_index_error(self, mock_inputs):
        parking_spot.parking_lot_entry_slots_setup()

    @patch('builtins.input', side_effect=[lot_size4, lot_size2, entry_slots1])
    def test_parking_lot_entry_slots_setup_value_error(self, mock_inputs):
        parking_spot.parking_lot_entry_slots_setup()

    @patch('builtins.input', side_effect=[reg_num1, 'bike', criteria_q])
    def test_parking_lot_park(self, mock_inputs):
        parking_spot.park()

    @patch('builtins.input', side_effect=['1'])
    def test_get_entry_slot(self, mock_inputs):
        gate = parking_spot.get_entry_slot()
        self.assertEqual(gate, 1)

    @patch('builtins.input', side_effect=['2', '1'])
    def test_get_entry_slot_else(self, mock_inputs):
        gate = parking_spot.get_entry_slot()
        self.assertEqual(gate, 1)
        
    @patch('builtins.input', side_effect=['re', '1'])
    def test_get_entry_slot_value_error(self, mock_inputs):
        gate = parking_spot.get_entry_slot()
        self.assertEqual(gate, 1)
