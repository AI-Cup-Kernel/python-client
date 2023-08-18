def initializer(game):
    temp = game.get_turn_number()['turn_number']
    print("temp", temp)
    print(game.put_one_troop(temp))
    print("player id", end=' ')
    print(game.get_player_id()['player_id'])

def turn(game):
    print("hello")
    print(game.get_owner())
    print(game.get_number_of_troops())
    print(game.put_troop(0, 4))
    game.next_state()
    print(game.attack(0, 2, 0))
    print(game.next_state())
    print(game.get_turn_number())
    print(game.move_troop(0, 1, 3))
    print(game.get_number_of_troops())
    print(game.move_troop(0, 1,1))
    #print(game.get_adj())

