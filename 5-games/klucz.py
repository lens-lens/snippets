from random import randint #funkcja do wylosowania dowolnej liczby

game_width = 10
game_height = 10

key_x = randint(0, game_width)
key_y = randint(0, game_height)
player_x = 0
player_y = 0
player_found_key = False
steps = 0

print(key_x, key_y)

while not player_found_key:
    steps += 1
    print('Choose direction [W/A/S/D]: ')

    move = input('Where U going?')
 #W
    if move.lower() == 'w':
        player_y += 1
        if player_y > game_height:
            print('Ugh! There is a wall here!')
            player_y = game_height
 #S
    elif move.lower() == 's':
        player_y -= 1
        if player_y < 0:
            print('Ugh! There is a wall here!')
            player_y = 0
 #A
    elif move.lower() == 'a':
        player_x -= 1
        if player_x < 0:
            print('Ugh! There is a wall here!')
            player_x = 0
 #D
    elif move.lower() == 'd':
        player_x += 1
        if player_x > game_width:
            print('Ugh! There is a wall here!')
            player_x = game_width

    elif move.lower() == 'q':
        print('Game over')
        quit()
    elif move.lower() == '_':
        print('Idk where are you going')
        continue

    
    if player_x == key_x and player_y == key_y:
        print('You found key to Milenka heart!')
        print(f'You did {steps} steps!')
        quit()

    print(player_x, player_y)