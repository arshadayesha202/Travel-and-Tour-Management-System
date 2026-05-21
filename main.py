class TravelPackage:
    def __init__(self, destination, base_price, dest_id):
        self.destination = destination
        self.base_price = base_price
        self.dest_id = dest_id
    def calculate_bill(self, persons):
        return self.base_price * persons
    
class InternationalTour(TravelPackage):
    def __init__(self, destination, base_price, dest_id, passport_no):
        super().__init__(destination, base_price, dest_id)
        self.passport_no = passport_no
        self.__visa_fee = 150
    def calculate_bill(self, persons):
        total = super().calculate_bill(persons)
        return total + (self.__visa_fee * persons)
        
class LocalTour(TravelPackage):
    def __init__(self, destination, base_price, dest_id, transport_type):
        super().__init__(destination, base_price, dest_id)
        self.transport_type = transport_type
        
    def calculate_bill(self, persons):
        transport_charges = 0
        t_type = self.transport_type.lower().strip()
        if t_type == "luxury bus":
            transport_charges = 1000
        elif t_type == "jeep":
            transport_charges = 3000
        elif t_type == "car":
            transport_charges = 1500
        total = super().calculate_bill(persons)
        return total + (transport_charges * persons)
    
class DiscountManager:
    def __init__(self):
        self.__discount = 0
    def apply_discount(self, base_total, discount_type):
        if discount_type.lower() == "student":
            self.__discount = 0.15
            print(" Student Discount (15%) applied")
        elif discount_type.lower() == "family":
            self.__discount = 0.10
            print(" Family Discount (10%) applied")
        else:
            self.__discount = 0
        return base_total * (1 - self.__discount)

class Customer:
    def __init__(self, name, contact):
        self.__name = name
        self.__contact = contact
    def get_customer_info(self):
        return f"name: {self.__name}  contact: {self.__contact}"
    
class TourGuide:
    def __init__(self, name, language):
        self.name = name
        self.language = language

class ReviewAndRating:
    def __init__(self, review_id, customer_name, package_name, rating, comment):
        self.review_id = review_id
        self.customer_name = customer_name
        self.package_name = package_name
        self.rating = rating  
        self.comment = comment
    def display_review(self):
        print(f"REVIEW ID: {self.review_id}")
        print(f"Package: {self.package_name} | Rating: {'⭐' * self.rating}")
        print(f"Customer: {self.customer_name}")
        print(f"Feedback: {self.comment}")


print("        WELCOME TO TRAVEL AND TOUR MANAGEMENT SYSTEM   ")
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
user = Customer(name, phone)

while True:
    try:
        print("\n SELECT YOUR TOUR CATEGORY ")
        print("1. International Tour(USD)")
        print("2. Local Tour(PKR)")
        choice = int(input("Enter choice (1 or 2): "))
        if choice in [1, 2]:
            break
        print(" Invalid input! Please choose either 1 or 2.")
    except ValueError:
        print(" Invalid input! Please enter a number.")

selected_tour = None

if choice == 1:
    while True:
        print("\n INTERNATIONAL TOURS AVAILABLE:")
        print("ID  | Destination | Price")
        print("101 | Dubai       | $500")
        print("102 | Turkey      | $900")
        print("103 | Switzerland | $2000")
        print("104 | England     | $1500")
        print("105 | Sweden      | $1900")
        
        try:
            dest_id = int(input("Enter destination id: "))
            passport = input("Enter passport number: ")
            
            if dest_id == 101:
                selected_tour = InternationalTour("Dubai", 500, 101, passport)
                break
            elif dest_id == 102:
                selected_tour = InternationalTour("Turkey", 900, 102, passport)
                break
            elif dest_id == 103:
                selected_tour = InternationalTour("Switzerland", 2000, 103, passport)
                break
            elif dest_id == 104:
                selected_tour = InternationalTour("England", 1500, 104, passport)
                break
            elif dest_id == 105:
                selected_tour = InternationalTour("Sweden", 1900, 105, passport)
                break
            else:
                print(" Invalid ID entered! Try again.")
        except ValueError:
            print(" Invalid ID! Please enter a valid numerical ID.")

elif choice == 2:
    while True:
        print("\n LOCAL DESTINATIONS ")
        print("ID  | Destination  | Price")
        print("201 | Hunza Valley | 45000 PKR")
        print("202 | Skardu       | 55000 PKR")
        print("203 | Murree       | 15000 PKR")
        
        try:
            dest_id = int(input("Enter Destination ID: "))
            
            if dest_id in [201, 202, 203]:
                while True:
                    transport = input("Choose Transport (Luxury Bus / Jeep / Car): ").strip()
                    if transport.lower() in ["luxury bus", "jeep", "car"]:
                        break
                    print(" Invalid Transport type! Please choose from the given options.")
                
                if dest_id == 201:
                    selected_tour = LocalTour("Hunza Valley", 45000, 201, transport)
                elif dest_id == 202:
                    selected_tour = LocalTour("Skardu", 55000, 202, transport)
                elif dest_id == 203:
                    selected_tour = LocalTour("Murree", 15000, 203, transport) 
                break
            else:
                print(" Invalid ID entered! Try again.")
        except ValueError:
            print(" Invalid ID! Please enter a valid numerical ID.")


if selected_tour:
    while True:
        try:
            people = int(input("How many people are travelling? "))
            if people > 0:
                break
            print(" Number of travelers must be greater than 0.")
        except ValueError:
            print(" Invalid input! Please enter a number.")
            
    guide = TourGuide("Mustafa Khan", "English/Urdu")
    
    
    while True:
        print("\nAny Special Discount?")
        print("1. Student (15%) | 2. Family (10%) | 3. None")
        d_choice = input("Enter choice: ")
        
        if d_choice in ["1", "2", "3"]:
            discount_type = "none"
            if d_choice == "1":
                discount_type = "student"
            elif d_choice == "2":
                discount_type = "family"
            break
        print(" Invalid choice! Select 1, 2, or 3.")

    final_bill = DiscountManager().apply_discount(selected_tour.calculate_bill(people), discount_type)

    print("\n              BOOKING RECEIPT               ")
    print(user.get_customer_info())
    print(f"Destination is {selected_tour.destination}")
    print(f"Tour ID is {selected_tour.dest_id}")
    print(f"Tour Guide is {guide.name} language: {guide.language}")
    symbol = "$" if choice == 1 else "PKR "
    print(f"TOTAL PAYABLE: {symbol} {final_bill}")
    
    while True:
        try:
            confirmation = int(input("Enter 1 to confirm your booking or 0 to cancel: "))
            if confirmation in [0, 1]:
                break
            print(" Invalid input! Enter 1 to confirm or 0 to cancel.")
        except ValueError:
            print(" Invalid input! Please enter a number (1 or 0).")

    if confirmation == 1:
        print("Booking Status: Confirmed ")
        print("\nNow Time For feedback!")
        
        while True:
            give_review = input("Would you like to leave a review? (y/n): ").lower().strip()
            if give_review in ['y', 'n']:
                break
            print("Please enter 'y' for yes or 'n' for no.")
            
        if give_review == 'y':
            while True:
                try:
                    stars = int(input("Rating (1-5 stars): "))
                    if 1 <= stars <= 5:
                        break
                    print(" Rating must be between 1 and 5 stars.")
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    
            msg = input("Share your experience: ")
            rev = ReviewAndRating("R001", name, selected_tour.destination, stars, msg)
            rev.display_review()
    else:
        print("Booking Status: Cancelled ")
