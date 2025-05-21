import Rooms
ok = False
while not ok:
    try:
        size = int(input('Please enter your room size(bigger than 5):'))
        if size < 5:
            print('Please enter a number bigger than 5.')
        else:
            ok = True
            gamemap = Rooms.GenerateRooms(size)
            Rooms.roomgenerator2(gamemap, size)
            Rooms.display_map(gamemap)
    except ValueError:
        print('Please enter a number.')
print('Thanks for playing!')
