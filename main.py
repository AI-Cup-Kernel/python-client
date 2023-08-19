import random

def initializer(game):
    print(game.get_strategic_nodes())
     
    strategic_nodes = game.get_strategic_nodes()['strategic_nodes']
    score = game.get_strategic_nodes()['score']
    owner = game.get_owners()
    for i in strategic_nodes:
        if owner[str(i)] == -1:
            print(game.put_one_troop(i))
            return 
    for i in owner.keys():
        if owner[i] == -1:
            print(game.put_one_troop(i))
            return 
    list_of_my_nodes = []
    for i in owner.keys():
        if owner[i] == game.get_player_id()['player_id']:
            list_of_my_nodes.append(i)
    print(game.put_one_troop(random.choice(list_of_my_nodes)))

def turn(game):
    print(game.get_number_of_troops_to_put())
    owner = game.get_owners()
    list_of_my_nodes = []
    for i in owner.keys():
        if owner[str(i)] == game.get_player_id()['player_id']:
            list_of_my_nodes.append(i)
    print(game.put_troop(random.choice(list_of_my_nodes), game.get_number_of_troops_to_put()['number of troops']))
    print(game.get_number_of_troops_to_put())

    print(game.next_state())

    # find the node with the most troops that I own
    max_troops = 0
    max_node = -1
    owner = game.get_owners()
    for i in owner.keys():
        if owner[str(i)] == game.get_player_id()['player_id']:
            if game.get_number_of_troops()[i] > max_troops:
                max_troops = game.get_number_of_troops()[i]
                max_node = i
    # find a neighbor of that node that I don't own
    adj = game.get_adj()
    for i in adj[max_node]:
        if owner[str(i)] != game.get_player_id()['player_id']:
            print(game.attack(max_node, i, 1))
            break
    print(game.next_state())
    print(game.get_state())
    # get the node with the most troops that I own
    max_troops = 0
    max_node = -1
    owner = game.get_owners()
    for i in owner.keys():
        if owner[str(i)] == game.get_player_id()['player_id']:
            if game.get_number_of_troops()[i] > max_troops:
                max_troops = game.get_number_of_troops()[i]
                max_node = i
    print(game.get_reachable(max_node))
    destination = random.choice(game.get_reachable(max_node)['reachable'])
    print(game.move_troop(max_node, destination, 1))
    #print(game.get_player_id())
    #print(game.get_turn_number())
    #print(game.get_number_of_troops())
    #print(game.get_adj())
    #print(game.next_state())
    #print(game.get_state())
    #print(game.next_state())
    #print(game.get_state())
    #print(game.next_state())
    #print(game.get_state())
    #print(game.next_state())
    #print(game.get_state())
    '''
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
    '''

