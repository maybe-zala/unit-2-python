from dataclasses import dataclass

@dataclass
#Class for the glass
class Glass:
    capacity:int
    current_amount:int
    #Pours water in glass(adds to amount)
    def pour_in(self, pour_in_glass:int)-> None:
        self.current_amount = int(pour_in_glass) + int(self.current_amount)
        if int(self.current_amount) >= int(self.capacity):
            self.current_amount = self.capacity
        
    #Pours water out of glass(subtracts from amount)
    def pour_out(self, amount:int)-> None:
        self.current_amount = int(self.current_amount) - int(amount)
        if int(self.current_amount) < 0:
            self.current_amount = 0

def main():
    #Asks user what they want capacity to be
    capacity=int(input('Capacity? '))
    glass = Glass(capacity,0)
    
    while True:
        #Starting amount and capacity
        print(f"Glass capacity: {glass.capacity}")
        print(f'Glass amount:',glass.current_amount)
        options = input("Pour [in], pour [out], or [quit]? ")
        if options == "in":
            pour_in_glass=int(input("Amount? "))
            glass.pour_in(pour_in_glass)
        elif options == "out":
            amount=input("Amount? ")
            glass.pour_out(int(amount))
        elif options == "quit":
            break
        else:
            #if user enters anything other than options
            print("Invalid action. Please enter 'in', 'out', or 'quit'.")

if __name__ == "__main__":
    main()