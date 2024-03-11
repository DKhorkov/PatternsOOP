from war_game_client import WarGameClient


if __name__ == '__main__':
    client: WarGameClient = WarGameClient()
    client.view_saves()

    client.buy_tank()
    client.buy_soldier()
    client.buy_soldier()
    client.buy_soldier()
    client.save_game('3 solders in tank')
    client.view_saves()

    client.buy_tank()
    client.buy_soldier()
    client.buy_soldier()
    client.save_game('2 tanks with 5 solders')
    client.view_saves()

    client.buy_tank()
    client.sell_soldier()
    client.sell_soldier()
    client.save_game('3 solders in 3 solders')
    client.view_saves()

    client.delete_save(2)
    client.view_saves()

    client.load_game(1)
    client.view_saves()

