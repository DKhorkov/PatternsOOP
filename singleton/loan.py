from dataclasses import dataclass
from typing import AnyStr


@dataclass(frozen=True)
class Loan:
    id: int
    amount: float
    interest_rate: float
    term: int  # Years
    repayment_amount: float
    issued_by: AnyStr

    def __str__(self):
        amount_info: AnyStr = f'Amount: {self.amount:.2f}'
        interest_rate_info: AnyStr = f'Interest rate: {self.interest_rate:.2%}'
        term_info: AnyStr = f'Term: {self.term}'
        repayment_amount_info: AnyStr = f'Repayment amount: {self.repayment_amount:.2f}'
        issued_by_info: AnyStr = f'Issued by: {self.issued_by}'
        return '\n'.join(
            [
                amount_info,
                interest_rate_info,
                term_info,
                repayment_amount_info,
                issued_by_info
            ]
        )
