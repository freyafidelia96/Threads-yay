# Function to calculate total sales for the day
def calculate_total_sales(morning_sales, evening_sales):
    return sum(morning_sales) + sum(evening_sales)

# Function to calculate worker's salary
def calculate_worker_salary(hourly_rate, hours_worked):
    return hourly_rate * hours_worked

# Function to calculate profit or loss
def calculate_profit(total_sales, total_cost):
    return total_sales - total_cost

# Function to calculate tips for a shift
def calculate_shift_tips(shift_sales):
    return sum(shift_sales) * 0.02

# Function to calculate total tips for the day
def calculate_total_tips(morning_sales, evening_sales):
    return calculate_shift_tips(morning_sales) + calculate_shift_tips(evening_sales)

# Function for user interface displaying menu
def display_menu():
    print("===== Accounting Automation System =====")
    print("1. Calculate Total Sales for the Day")
    print("2. Calculate Worker's Salary")
    print("3. Calculate Profit/Loss")
    print("4. Calculate Tips for a Shift")
    print("5. Calculate Total Tips for the Day")
    print("6. Exit")

# Main function
def main():
    morning_sales = [500, 700, 900]  # Example morning sales data
    evening_sales = [800, 600, 1000]  # Example evening sales data

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            total_sales = calculate_total_sales(morning_sales, evening_sales)
            print(f"Total Sales for the Day: ${total_sales}")

        elif choice == '2':
            hourly_rate = float(input("Enter worker's hourly rate: "))
            hours_worked = float(input("Enter hours worked by the worker: "))
            worker_salary = calculate_worker_salary(hourly_rate, hours_worked)
            print(f"Worker's Salary: ${worker_salary}")

        elif choice == '3':
            total_sales = float(input("Enter total sales: "))
            total_cost = float(input("Enter total cost: "))
            profit = calculate_profit(total_sales, total_cost)
            print(f"Profit/Loss: ${profit}")

        elif choice == '4':
            shift_sales = [float(x) for x in input("Enter shift sales (comma-separated): ").split(',')]
            shift_tips = calculate_shift_tips(shift_sales)
            print(f"Tips for the Shift: ${shift_tips}")

        elif choice == '5':
            total_tips = calculate_total_tips(morning_sales, evening_sales)
            print(f"Total Tips for the Day: ${total_tips}")

        elif choice == '6':
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
