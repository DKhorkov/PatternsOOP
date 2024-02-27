from bank import Bank
from loan import Loan


if __name__ == '__main__':
    vtb_north: Bank = Bank(name="VTB")
    print(f'VTB-north is {str(vtb_north)}', end='\n\n')

    loan: Loan = vtb_north.issue_loan(
        amount=12_000_000.00,
        interest_rate=0.12,
        term=3
    )
    print(f'Next loan has been just issued:\n\n{str(loan)}', end='\n\n')

    vtb_south: Bank = Bank(name="VTB")
    assert vtb_north == vtb_south
    print(f'VTB-north is {str(vtb_north)}', f'VTB-south is {str(vtb_south)}', sep='\n\n', end='\n\n')

    city: Bank = Bank(name="City")
    assert city != vtb_north and city != vtb_south
    print(str(city))
