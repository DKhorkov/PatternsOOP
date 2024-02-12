from .tax_strategy import TaxStrategy
from .sole_trader_tax_strategy import SoleTraderTaxStrategy
from .self_employed_tax_strategy import SelfEmployedTaxStrategy
from .regular_tax_strategy import RegularTaxStrategy
from .employee import Employee
from .exceptions import TaxLawsViolationsException


"""
Strategy is a behavioral design pattern, designed to define a family of algorithms, 
encapsulate each of them, and ensure their interchangeability. 

This allows client to select an algorithm by defining the appropriate class.
"""
