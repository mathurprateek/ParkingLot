from unittest import TestCase
from unittest.mock import patch
import parking


class TestParking(TestCase):
    criteria_p = 'p'
    criteria_u = 'u'
    criteria_s = 's'
    criteria_h = 'h'
    criteria_q = 'q'
    criteria_r = 'r'
    criteria_v = 'v'
    criteria_c = 'c'
    criteria_m = 'm'
    reg_num1 = 'reg1'
    reg_num2 = 'reg2'
    reg_num3 = 'reg3'
    vehicle_type1 = 'car'
    color1 = 'red'
    make1 = 'mnm'
    entry_slot1 = '1'
    entry_slot2 = '5'
        
    @patch('builtins.input', side_effect=[criteria_p, reg_num1, vehicle_type1, color1, make1, entry_slot1, criteria_q])
    def test_select_action_p_right(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=['p', 'reg2', 'bus', 'black', 'leyland', '8', criteria_q])
    def test_select_action_p_left(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_s, criteria_q])
    def test_select_action_s(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_p, reg_num1, vehicle_type1, color1, make1, entry_slot1, criteria_h, criteria_r, reg_num1, criteria_q])
    def test_select_action_h_reg_num(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_h, criteria_r, reg_num3, criteria_q])
    def test_select_action_h_no_reg_num(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_h, 'w', criteria_r, reg_num3, criteria_q])
    def test_select_action_h_no_criteria_match(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_h, criteria_r, '\n', criteria_q])
    def test_select_action_h_no_val_entered_reg_num(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_p, reg_num1, vehicle_type1, color1, make1, entry_slot1, criteria_h, criteria_v, vehicle_type1, criteria_q])
    def test_select_action_h_veh_type(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_h, criteria_v, '\n', criteria_q])
    def test_select_action_h_no_val_entered_veh_type(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_p, reg_num1, vehicle_type1, color1, make1, entry_slot1, criteria_h, criteria_c, color1, criteria_q])
    def test_select_action_h_color(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_h, criteria_c, '\n', criteria_q])
    def test_select_action_h_no_val_entered_color(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_p, reg_num1, vehicle_type1, color1, make1, entry_slot1, criteria_h, criteria_m, make1, criteria_q])
    def test_select_action_h_make(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_h, criteria_m, '\n', criteria_q])
    def test_select_action_h_no_val_entered_make(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_u, reg_num1, criteria_q])        
    def test_select_action_u_success(self, mock_inputs):
        parking.select_action()

    @patch('builtins.input', side_effect=[criteria_u, 'no_reg', criteria_q])
    def test_select_action_u_no_vehicle_found(self, mock_inputs):
        parking.select_action()
