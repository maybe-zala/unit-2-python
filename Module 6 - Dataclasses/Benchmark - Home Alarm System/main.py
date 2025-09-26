from dataclasses import dataclass

@dataclass
class Alarm:
    code:int
    alarm:str
    door:str


def main():
    code = Alarm(input("Alarm Code? "), "Off", "Closed")
    print("Alarm:",code.alarm)
    print("Door:",code.door)
    while True:
        options = input("turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> ")
        if options == "on":
            if code.door=="Open":
                code.alarm="Off"
                print("Alarm:",code.alarm)
                print("Door:",code.door)
            elif code.alarm == "Off":
                code.alarm = "On"
                print("Alarm:",code.alarm)
                print("Door:",code.door)
            elif code.alarm=="On" and code.door=="Open":
                print("Alarm: *SIREN*")
                print("Door:",code.oor)
            elif code.alarm == "*SIREN*" and code.door == "Open":
                print("Alarm: *SIREN*")
                print("Door:",code.door)   
            else:
                print("Alarm: *SIREN*")
                print("Door:",code.door)  
        elif options == "off":
            us_input =input("Alarm Code? ")
            if us_input == code.code:
                code.alarm = "Off"
            elif us_input != code.code:
                code.alarm = "*SIREN*"
            print("Alarm:",code.alarm)
            print("Door:",code.door)
        elif options == "open":
            if code.alarm == "On":
                code.door = "Open"
                print("Alarm: *SIREN*")
                print('Door:',code.door)
            elif code.alarm == "Off":
                code.door = "Open"
                print("Alarm:",code.alarm)
                print("Door:",code.door)
            elif code.alarm == "*SIREN*":
                code.door = "Open"
                print("Alarm: *SIREN*")
                print("Door:",code.door) 
        elif options == "close":
            if code.alarm == "On" and code.door == "Open":
                code.alarm="*SIREN*"
                code.door="Closed"
                print("Alarm:",code.alarm)
                print("Door:",code.door)
            else:
                code.door = "Closed"
                print("Alarm:",code.alarm)
                print("Door:",code.door)
        elif options == "quit":
            quit()
        else:
            print("Invalid input.")
            print("Alarm: *SIREN*")
            print("Door:",code.door)

if __name__ == '__main__':
    main()