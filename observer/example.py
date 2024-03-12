from customer import Customer
from shop import Shop


if __name__ == '__main__':
    lenta: Shop = Shop(name='Lenta')
    perekrestok: Shop = Shop(name='Perekrestok')

    sergey: Customer = Customer(name='Sergey')
    sergey.subscribe(publisher=lenta)
    sergey.subscribe(publisher=perekrestok)
    print(
        f'{sergey.name} has next subscribes: {', '.join([str(publisher) for publisher in sergey.publishers])}',
        end='\n\n'
    )

    danila: Customer = Customer(name='Danila')
    danila.subscribe(publisher=lenta)
    print(
        f'{danila.name} has next subscribes: {', '.join([str(publisher) for publisher in danila.publishers])}',
        end='\n\n'
    )

    perekrestok.goods = {
        'meat': 99.50,
        'cheese': 34.50
    }

    lenta.goods = {
        'banana': 7.86,
        'apple': 22.50
    }

    sergey.unsubscribe(publisher=perekrestok)
    print(
        f'{sergey.name} has next subscribes: {', '.join([str(publisher) for publisher in sergey.publishers])}',
        end='\n\n'
    )

    # Noone will receive:
    perekrestok.goods = {
        'tomatoes': 15.22
    }

    sergey.unsubscribe(publisher=lenta)
    print(
        f'{sergey.name} has next subscribes: {', '.join([str(publisher) for publisher in sergey.publishers])}',
        end='\n\n'
    )

    # Only Danila will receive:
    lenta.goods = {
        'milk': 18.75
    }
