# Travel and Tour Management System

A robust, console-based Python application designed to streamline travel bookings, manage domestic and international vacation packages, apply dynamic discounts, and handle customer feedback using Object-Oriented Programming (OOP) principles.

## 🚀 Key Features
- **Dual Tour Categories:** Handles both International Tours (in USD with hidden visa fees) and Local Tours (in PKR with dynamic transport options like Jeep, Luxury Bus, etc.).
- **Dynamic Discount Manager:** Automatically applies specific discount rates for Students (15%) and Families (10%).
- **Feedback & Review System:** Allows customers to leave text reviews and star ratings (1-5 ⭐) after confirmation.
- **Bulletproof Input Validation:** Built-in validation loops and `try-except` blocks ensure the application handles invalid choices or accidental string inputs without crashing.

## 🛠️ OOP Concepts Applied
- **Inheritance:** `InternationalTour` and `LocalTour` inherit core behaviors from the parent `TravelPackage` class.
- **Polymorphic Method Overriding:** The `calculate_bill()` function is overridden across classes to handle specific pricing logic dynamically at runtime.
- **Encapsulation:** Private variables (like `__visa_fee`, `__discount`, and customer data) ensure proper data hiding and security.

## 💻 Tech Stack
- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)

## 📋 How to Run
1. Clone this repository or copy the code from `main.py`.
2. Run the file in any Python environment:
   
```bash
   python main.py
# Travel-and-Tour-Management-System
A Python-based console application for managing local and international travel bookings using Object-Oriented Programming (OOP) principles.
