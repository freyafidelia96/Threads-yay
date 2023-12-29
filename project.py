# Function to calculate worker's salary
def calculateWorkerSalary(hourlyRate, hoursWorked):
    return hourlyRate * hoursWorked

# Function to calculate profit or loss
def calculateProfit(totalSales, totalCost):
    return totalSales - totalCost

# Function to calculate tips for a shift
def calculateShiftTips(shiftSales):
    return sum(shiftSales) * 0.02

# Function to calculate total tips for the day
def calculateTotalTips(morningSales, eveningSales):
    return calculateShiftTips(morningSales) + calculateShiftTips(eveningSales)

# Function for user interface displaying menu
def display_menu():
    print("*=*=*=*=*=* Accounting Automation System *=*=*=*=*=*")
    print("0. Input Total Sales for the Day")
    print("1. Calculate Total Sales for the Day")
    print("2. Calculate Worker's Salary")
    print("3. Calculate Profit/Loss")
    print("4. Calculate Tips for a Shift")
    print("5. Calculate Total Tips for the Day")
    print("6. Exit")

#Function to get sales data
def get_sales_data():
    try:
        morningSales = [] # instantiation of morning sales data
        morningSales_cost_prices = [] # instantiation of morning sales cost data
        eveningSales = [] # instantiation of evening sales data
        eveningSales_cost_prices = [] # instantiation of evening sales cost data


        
        while True:
            costPrice = float(input("Enter morning sales data/ Cost price of item: "))
            salesPrice = float(input("Enter morning sales data/ Sales price of item: "))

            morningSales.append(salesPrice)
            morningSales_cost_prices.append(costPrice)

            end = input("Enter zero (0) to end input: ")

            if end == '0':
                break

        
    
 

        while True:
            costPrice = float(input("Enter evening sales data/ Cost price of item: "))
            salesPrice = float(input("Enter evening sales data/ Sales price of item: "))

            eveningSales.append(salesPrice)
            eveningSales_cost_prices.append(costPrice)


            end = input("Enter zero to end input: ")

            if end == '0':
                break

    
    except Exception:
        print(f"Invalid input! Start all over.")
        get_sales_data()

    return morningSales, eveningSales, morningSales_cost_prices, eveningSales_cost_prices

# Main function
def main():

    while True:
        display_menu()

        try:
            choice = input("Enter your choice (0-6), 0 FIRST TO ENTER SALES DATA: ")
        

            if choice == '0':
                morningSales, eveningSales, morningSales_cost_prices, eveningSales_cost_prices = get_sales_data()
                total_cost = sum(morningSales_cost_prices) + sum(eveningSales_cost_prices)
                total_sales = sum(morningSales) + sum(eveningSales)
                
            elif choice == '1':
                print(f"Morning sales: {morningSales}\nEvening sales: {eveningSales}\nTotal sales: ${total_sales}")

            elif choice == '2':
                hourly_rate = float(input("Enter worker's hourly rate: "))
                hours_worked = float(input("Enter hours worked by the worker: "))
                worker_salary = calculateWorkerSalary(hourly_rate, hours_worked)
                print(f"Worker's Salary: ${worker_salary}")

            elif choice == '3':
                profit = calculateProfit(total_sales, total_cost)
                print(f"Profit/Loss: ${profit}")

            elif choice == '4':
                which_shift = input("Enter the shift (morning or evening): ").lower()
                if which_shift == "morning":
                    shift_tips = calculateShiftTips(morningSales)
                elif which_shift == "evening":
                    shift_tips = calculateShiftTips(eveningSales)
                else:
                    print("Invalid input!")
                print(f"Tips for the Shift: ${shift_tips}")

            elif choice == '5':
                total_tips = calculateTotalTips(morningSales, eveningSales)
                print(f"Total Tips for the Day: ${total_tips}")

            elif choice == '6':
                print("Exiting the program. Thank you!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except UnboundLocalError:
            print("You have to input sales data first.")


if __name__ == "__main__":
    main()
