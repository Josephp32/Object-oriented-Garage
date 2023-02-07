class parkingGarage():

    def __init__(self, handles, capacity, items, current_tickets):
        self.handles = handles
        self.capacity = capacity
        self.items = items
        self.current_tickets = current_tickets
            
        
        
        # Show capacity of Shopping cart
    # def showCapacity(self):
    #     print(f' Your capacity is: {self.capacity}')
            
        # Add items to shopping cart
    def addParkedCar(self):
        entry = input('What is your name? ')
        print('Welcome')
        self.items.append(entry)

    # delete items from shopping cart
    def deleteParkedCar(self):
        name = input('What is your name? ')
        if name.lower() in self.items:
            self.items.remove(name.lower())
            payment = input("Please enter payment: ")
            if True:
                print("thank you for the payment! You have 15 minutes to leave")
                self.current_tickets[name] = payment
        else: 
            print(f'{name} is not a valid entry, please try again.')
     # capacity of the parking lot
    def parkingSpaces(self, capacity):
        self.capacity = capacity
        if len(self.items) >= 10:
            print("Im sorry but the parking lot is full.")
        else:
            print('thank you')

dons_parking = parkingGarage(2, 10, [], {})

    # running parking garage function
def run():
    while True:
        response = input('Are you coming or leaving? ')
        
        if response.lower() == 'coming':
            dons_parking.addParkedCar()
        elif response.lower() == 'leaving':
            dons_parking.deleteParkedCar()
        else:
            print('Try another command')


run()   
