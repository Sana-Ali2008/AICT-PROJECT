cars = [] 
def load_from_file():
    try:
        file = open("cars.txt", "r")
        for line in file:
            data = line.strip().split(",")
            car = {
                "name": data[0],
                "model": data[1],
                "mileage": int(data[2]),
                "last_oil": int(data[3]),
                "last_tire": int(data[4]),
                "last_brake": int(data[5])
            }
            cars.append(car)
        file.close()
        print("Data loaded from file.")
    except:
        print("No previous data found.")

def save_to_file():
    file = open("cars.txt", "w")
    for c in cars:
        file.write(
            c["name"] + "," +
            c["model"] + "," +
            str(c["mileage"]) + "," +
            str(c["last_oil"]) + "," +
            str(c["last_tire"]) + "," +
            str(c["last_brake"]) + "\n"
        )
    file.close()
    print("Data saved to file.")

def add_car():
    print("\n--- Add Car Information ---")
    name = input("Enter car name: ")
    model = input("Enter car model: ")
    mileage = int(input("Enter current mileage: "))
    last_oil = int(input("Enter last oil change mileage: "))
    last_tire = int(input("Enter last tire change mileage: "))
    last_brake = int(input("Enter last brake service mileage: "))

    car = {
        "name": name,
        "model": model,
        "mileage": mileage,
        "last_oil": last_oil,
        "last_tire": last_tire,
        "last_brake": last_brake
    }

    cars.append(car)
    print("Car added successfully.\n")

def view_cars():
    if len(cars) == 0:
        print("No car records found.\n")
        return

    print("\n    Car Records    ")
    for i, c in enumerate(cars):
        print(f"{i+1}. {c['name']} ({c['model']})")
        print("   Mileage:", c["mileage"])
        print("   Last Oil:", c["last_oil"])
        print("   Last Tire:", c["last_tire"])
        print("   Last Brake:", c["last_brake"])

def update_oil_change():
    view_cars()
    num = int(input("Enter record number: ")) - 1

    if 0 <= num < len(cars):
        cars[num]["last_oil"] = int(input("Enter new oil change mileage: "))
        print("Oil change updated.\n")
    else:
        print("Invalid record number.\n")

def check_maintenance():
    if len(cars) == 0:
        print("No records available.\n")
        return

    for c in cars:
        print(f"\nChecking {c['name']} ({c['model']})")

        if c["mileage"] - c["last_oil"] >= 3000:
            print(" Oil change required")
        else:
            print(" Oil is OK")

        if c["mileage"] - c["last_tire"] >= 20000:
            print(" Tire change required")
        else:
            print(" Tires are OK")

        if c["mileage"] - c["last_brake"] >= 10000:
            print(" Brake service required")
        else:
            print(" Brakes are OK")

def service_summary():
    count = 0
    for c in cars:
        if c["mileage"] - c["last_oil"] >= 3000:
            count += 1
    print("\nCars needing oil change:", count)

def reset_maintenance():
    view_cars()
    num = int(input("Enter record number: ")) - 1

    if 0 <= num < len(cars):
        cars[num]["last_oil"] = cars[num]["mileage"]
        cars[num]["last_tire"] = cars[num]["mileage"]
        cars[num]["last_brake"] = cars[num]["mileage"]
        print("Maintenance reset successfully.\n")
    else:
        print("Invalid record number.\n")

def delete_car():
    view_cars()
    num = int(input("Enter record number to delete: ")) - 1

    if 0 <= num < len(cars):
        cars.pop(num)
        print("Car deleted.\n")
    else:
        print("Invalid record number.\n")

load_from_file()

while True:
    print("\n      CAR MAINTENANCE MENU      ")
    print("1. Add Car")
    print("2. View Cars")
    print("3. Update Oil Change")
    print("4. Check Maintenance Status")
    print("5. Service Summary")
    print("6. Reset Maintenance After Service")
    print("7. Delete Car")
    print("8. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_car()
    elif choice == "2":
        view_cars()
    elif choice == "3":
        update_oil_change()
    elif choice == "4":
        check_maintenance()
    elif choice == "5":
        service_summary()
    elif choice == "6":
        reset_maintenance()
    elif choice == "7":
        delete_car()
    elif choice == "8":
        save_to_file()
        print("Program exited.")
        break
    else:
        print("Invalid choice. Try again.")