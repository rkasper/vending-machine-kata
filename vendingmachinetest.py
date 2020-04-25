import unittest

from coin import Coin
from vendingmachine import VendingMachine


class VendingMachineTest(unittest.TestCase):
    # Make sure the unittest system works properly
    def test_unittest_works_properly(self):
        self.assertTrue(True)

    # Accept Coins
    #
    # As a vendor
    # I want a vending machine that accepts coins
    # So that I can collect money from the customer
    #
    # The vending machine will accept valid coins (nickels, dimes, and quarters) and reject invalid ones (pennies).
    # When a valid coin is inserted the amount of the coin will be added to the current amount and the display will be
    # updated. When there are no coins inserted, the machine displays INSERT COIN. Rejected coins are placed in the
    # coin return.
    #
    # NOTE: The temptation here will be to create Coin objects that know their value. However, this is not how a real
    # vending machine works. Instead, it identifies coins by their weight and size and then assigns a value to what
    # was inserted. You will need to do something similar. This can be simulated using strings, constants, enums,
    # symbols, or something of that nature.
    def test_accept_coins(self):
        vm = VendingMachine()

        # When we turn on the vending machine, it displays "INSERT COIN".
        self.assertEqual("INSERT COIN", vm.display())

        # When we add a nickel, it displays the balance: $0.05.
        self.assertTrue(vm.accept_coin(Coin.NICKEL))
        self.assertEqual("$0.05", vm.display())
        self.assertEqual(Coin.NONE, vm.coin_returned(), "The coin return slot should be empty.")

        # When we add another nickel, it displays the new balance: $0.10
        self.assertTrue(vm.accept_coin(Coin.NICKEL))
        self.assertEqual("$0.10", vm.display())

        # When we add a dime, it displays the new balance: $0.20
        self.assertTrue(vm.accept_coin(Coin.DIME))
        self.assertEqual("$0.20", vm.display())

        # When we add a quarter, it displays the new balance: $0.45
        self.assertTrue(vm.accept_coin(Coin.QUARTER))
        self.assertEqual("$0.45", vm.display())

        # When we try to add a penny, the penny is placed in the coin return and the balance doesn't change.
        self.assertFalse(vm.accept_coin(Coin.PENNY), "Should not accept a penny")
        self.assertEqual("$0.45", vm.display())
        self.assertEqual(Coin.PENNY, vm.coin_returned(), "Rejected penny should be in coin return slot")


if __name__ == '__main__':
    unittest.main()
