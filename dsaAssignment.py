class Passenger:
    def __init__(self, name):
        self.name = name
        self.next = None

class Flight:
    def __init__(self, flight_name):
        self.flight_name = flight_name
        self.passengers = None
        self.next = None

class ReservationSystem:
    def __init__(self):
        self.flights = None

    def add_flight(self, flight_name):
        new_flight = Flight(flight_name)
        new_flight.next = self.flights
        self.flights = new_flight

    def reserve_ticket(self, flight_name, passenger_name):
        flight = self.find_flight(flight_name)
        if flight:
            new_passenger = Passenger(passenger_name)
            new_passenger.next = flight.passengers
            flight.passengers = new_passenger
            print(f"Reservation for {passenger_name} on {flight_name} successful.")
        else:
            print(f"Flight {flight_name} not found.")

    def cancel_reservation(self, flight_name, passenger_name):
        flight = self.find_flight(flight_name)
        if flight:
            prev_passenger = None
            current_passenger = flight.passengers

            while current_passenger:
                if current_passenger.name == passenger_name:
                    if prev_passenger:
                        prev_passenger.next = current_passenger.next
                    else:
                        flight.passengers = current_passenger.next
                    print(f"Reservation for {passenger_name} on {flight_name} canceled.")
                    return
                prev_passenger = current_passenger
                current_passenger = current_passenger.next

            print(f"No reservation found for {passenger_name} on {flight_name}.")
        else:
            print(f"Flight {flight_name} not found.")

    def check_reservation(self, passenger_name):
        current_flight = self.flights
        while current_flight:
            current_passenger = current_flight.passengers
            while current_passenger:
                if current_passenger.name == passenger_name:
                    print(f"{passenger_name} has a reservation on {current_flight.flight_name}.")
                    return
                current_passenger = current_passenger.next
            current_flight = current_flight.next
        print(f"No reservation found for {passenger_name} on any flight.")

    def display_passengers(self, flight_name):
        flight = self.find_flight(flight_name)
        if flight:
            print(f"Passengers on {flight_name}:")
            current_passenger = flight.passengers
            while current_passenger:
                print(current_passenger.name)
                current_passenger = current_passenger.next
        else:
            print(f"Flight {flight_name} not found.")

    def find_flight(self, flight_name):
        current_flight = self.flights
        while current_flight:
            if current_flight.flight_name == flight_name:
                return current_flight
            current_flight = current_flight.next
        return None

def main():
    reservation_system = ReservationSystem()

    while True:
        print("\nAirline Ticket Reservation System")
        print("1. Add Flight")
        print("2. Reserve a Ticket")
        print("3. Cancel Reservation")
        print("4. Check Reservation")
        print("5. Display Passengers for a Flight")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            flight_name = input("Enter the flight name: ")
            reservation_system.add_flight(flight_name)
        elif choice == "2":
            flight_name = input("Enter the flight name: ")
            passenger_name = input("Enter the passenger's name: ")
            reservation_system.reserve_ticket(flight_name, passenger_name)
        elif choice == "3":
            flight_name = input("Enter the flight name: ")
            passenger_name = input("Enter the passenger's name: ")
            reservation_system.cancel_reservation(flight_name, passenger_name)
        elif choice == "4":
            passenger_name = input("Enter the passenger's name: ")
            reservation_system.check_reservation(passenger_name)
        elif choice == "5":
            flight_name = input("Enter the flight name: ")
            reservation_system.display_passengers(flight_name)
        elif choice == "6":
            print("Thank you for using the Airline Ticket Reservation System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
