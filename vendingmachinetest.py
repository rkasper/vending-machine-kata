import unittest

from coin import Coin
from product import Product
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

    # Select Product
    #
    # As a vendor
    # I want customers to select products
    # So that I can give them an incentive to put money in the machine
    #
    # There are three products: cola for $1.00, chips for $0.50, and candy for $0.65. When the respective button is
    # pressed and enough money has been inserted, the product is dispensed and the machine displays THANK YOU. If the
    # display is checked again, it will display INSERT COIN and the current amount will be set to $0.00. If there is
    # not enough money inserted then the machine displays PRICE and the price of the item and subsequent checks of the
    # display will display either INSERT COIN or the current amount as appropriate.
    def test_select_product(self):
        vm = VendingMachine()

        # TODO Rename method to reflect user's experience. Try deposit_coin().
        vm.accept_coin(Coin.QUARTER)
        vm.accept_coin(Coin.QUARTER)
        vm.accept_coin(Coin.QUARTER)
        vm.accept_coin(Coin.QUARTER)
        product = vm.select_product(Product.CHIPS)
        self.assertEqual(Product.CHIPS, product)
        self.assertEqual("THANK YOU", vm.display())



if __name__ == '__main__':
    unittest.main()