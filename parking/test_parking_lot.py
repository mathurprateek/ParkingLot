from unittest import TestCase
from parking.parking_lot import ParkingLot

class TestParkingLot(TestCase):
    def test_parking_lot(self):
        p = ParkingLot(3, {1})
        self.assertEqual(p.parking_lot(), {1: 'ENTRY GATE', 2: 'vacant', 3: 'vacant'})
        self.assertEqual(p.slots, 3)
        self.assertEqual(p.entries, {1})
