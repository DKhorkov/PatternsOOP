from typing import AnyStr, List

from singleton_metaclass import SingletonMetaclass
from configs import DEFAULT_BANK_START_BALANCE
from loan import Loan
from exceptions import NotEnoughFundsError, IncorrectLoanIssuerError


class Bank(metaclass=SingletonMetaclass):
    """
    Bank can be the only one. It can not be two VTB-banks of City-banks.
    """

    def __init__(self, name: AnyStr) -> None:
        self.__name: AnyStr = name
        self.__balance: float = DEFAULT_BANK_START_BALANCE

        self.__issued_loans: List[Loan] = list()

    def __str__(self) -> AnyStr:
        if self.__issued_loans:
            issued_loans_info: AnyStr = f'next loans:\n\n' \
                                        f'{f'\n'.join([str(loan) for loan in self.__issued_loans])}'
        else:
            issued_loans_info: AnyStr = 'no loans yet.'

        bak_info: AnyStr = f'{self.__name}-bank which currently has {self.__balance:.2f}$ on its accounts ' \
                           f'and issued {issued_loans_info}'
        return bak_info

    def issue_loan(
            self,
            amount: float,
            interest_rate: float,
            term: int  # Years
    ) -> Loan:

        self.__check_current_balance(loan_amount=amount)
        loan: Loan = Loan(
            id=len(self.__issued_loans),
            amount=amount,
            interest_rate=interest_rate,
            term=term,
            repayment_amount=self.__calculate_repayment_amount(
                amount=amount,
                interest_rate=interest_rate,
                term=term
            ),
            issued_by=self.__name
        )
        self.__issued_loans.append(loan)
        self.__balance -= amount
        return loan

    def repay_loan(self, loan: Loan) -> None:
        if not loan.issued_by == self.__name:
            raise IncorrectLoanIssuerError(f'Next loan does not belong to {self.__name}:\n\n{str(loan)}\n')

        self.__issued_loans.pop(loan.id)
        self.__balance += loan.repayment_amount
        print(f'Next loan was successfully repaid:\n\n{str(loan)}\n.')

    def __check_current_balance(self, loan_amount: float) -> None:
        if loan_amount > self.__balance:
            raise NotEnoughFundsError(
                f'Bank can not issue loan for the amount of {loan_amount:.2f}$ '
                f'due to lack of available funds'
            )

    @staticmethod
    def __calculate_repayment_amount(
            amount: float,
            interest_rate: float,
            term: int  # Years
    ) -> float:

        # Suppose, we capitalize loan interest as via deposits:
        repayment_amount: float = amount * (1 + interest_rate) ** term
        return repayment_amount

    @property
    def name(self) -> AnyStr:
        return self.__name

    @property
    def balance(self) -> float:
        return self.__balance
