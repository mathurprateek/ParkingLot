from unittest import TestCase, mock
from importlib.machinery import SourceFileLoader
import types


class TestApp(TestCase):

    lot_size1 = '5'
    entry_slots1 = '1 3'
    action_choice = 'q'

    @mock.patch('builtins.input', side_effect=[lot_size1, entry_slots1, action_choice])
    def test_app_1(self, mock_inputs):
        loader = SourceFileLoader('__main__', 'app.py')
        loaded = types.ModuleType(loader.name)
        loader.exec_module(loaded)

