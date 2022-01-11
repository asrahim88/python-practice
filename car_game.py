command = ''
started = False
while True:
    command = input("> ").lower()
    if command == 'help':
        print("""
start - to start car ready to go...
stop - to stop the car 
quit - to exit the game
        """)
    elif command == 'start':
        if started:
            print("Car is already started...")
        else:
            started = True
            print("start car ready to go")
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("stopped the car")
    elif command == 'quit':
        break
    else:
        print("I don't understand command. type 'help' for proper command usage.")