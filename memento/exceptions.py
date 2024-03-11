class NotEnoughMoneyError(Exception):

    def __init__(self, msg='Not enough money to buy this unit.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class NoUnitsToSellError(Exception):

    def __init__(self, msg='No units of this type to sell.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
