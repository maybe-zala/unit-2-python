class Calculator:
    current = 0

    def add(self, number): # Adds the given number to the current value.
        self.current += number

    def subtract(self, number): # Subtracts the given number from the current value.
        self.current -= number

    def multiply(self, number): #  Multiplies the current value by the given number.
        self.current *= number

    def divide(self, number): # Divides the current value by the given number.
        self.current /= number

    def exponentiate(self, power): # Raises the current value to the power of the given number.
        self.current = self.current**power
    
    def sqrt(self): # Calculates the square root of the current value.
        self.current = float(format(self.current**0.5, ".4f"))

    def reset(self): # Resets the current value back to 0.
        self.current = 0