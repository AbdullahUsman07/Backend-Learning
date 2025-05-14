

from db import connect_db, close_db

def show_rooms():
    conn = connect_db()
    if not conn:
        print("Failed to connect to the database")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms")
    rows = cursor.fetchall()
    print("\n--- Available Rooms ---")
    for row in rows:
        print(f"RoomID: {row[0]}, Type: {row[1]}, Total Seats: {row[2]}, Available Seats: {row[3]}, Rent: {row[4]}")
    close_db(conn)

def show_students():
    conn = connect_db()
    if not conn:
        print("Failed to connect to the database")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student List ---")
    for row in rows:
        print(f"StudentID: {row[0]}, RoomID: {row[1]}, Name: {row[2]}, University: {row[3]}, DOB: {row[4]}")
    close_db(conn)

def add_room():
    conn = connect_db()
    if not conn:
        print("Failed to connect to the database")
        return

    roomType = input("\nEnter Room Type (Single/Shared): ")
    totalSeats = int(input("Enter Total Seats: "))
    availableSeats = totalSeats  # Initially, all seats are available
    rent = float(input("Enter Rent Amount: "))

    cursor = conn.cursor()
    sql = "INSERT INTO rooms (roomType, totalSeats, availableSeats, rent) VALUES (%s, %s, %s, %s)"
    values = (roomType, totalSeats, availableSeats, rent)
    cursor.execute(sql, values)
    conn.commit()

    print("Room added successfully!")
    close_db(conn)

def add_student():
    conn = connect_db()
    if not conn:
        print("Failed to connect to the database")
        return

    # Show available rooms
    cursor = conn.cursor()
    cursor.execute("SELECT roomID, roomType, availableSeats FROM rooms WHERE availableSeats > 0")
    rooms = cursor.fetchall()

    if not rooms:
        print("\nNo available rooms found. Please add rooms first.")
        close_db(conn)
        return

    print("\n--- Available Rooms ---")
    for room in rooms:
        print(f"RoomID: {room[0]}, Type: {room[1]}, Available Seats: {room[2]}")

    # Select room ID
    roomID = int(input("\nEnter Room ID: "))

    # Check if the selected room is valid
    valid_room_ids = [room[0] for room in rooms]
    if roomID not in valid_room_ids:
        print("Invalid Room ID! Please select a valid room from the list above.")
        close_db(conn)
        return

    
    
    studentID = input("Enter Student ID: ")

    cursor.execute("SELECT 1 FROM students WHERE studentID = %s", (studentID,))
    if cursor.fetchone():
        print("Student ID already exists! Please use a unique Student ID.")
        close_db(conn)
        return
    name = input("Enter Student Name: ")
    universityName = input("Enter University Name: ")
    DOB = input("Enter Date of Birth (YYYY-MM-DD): ")

    # Add student to the database
    sql = "INSERT INTO students (studentID, roomID, name, universityName, DOB) VALUES (%s, %s, %s, %s, %s)"
    values = (studentID, roomID, name, universityName, DOB)
    cursor.execute(sql, values)

    # Update available seats in the room
    cursor.execute("UPDATE rooms SET availableSeats = availableSeats - 1 WHERE roomID = %s", (roomID,))
    conn.commit()

    print("Student added successfully!")
    close_db(conn)


def update_student():
    conn = connect_db()
    if not conn:
        print("Failed to connect to the database")
        return

    studentID = input("\nEnter Student ID to update: ")
    
    # Check if student exists
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE studentID = %s", (studentID,))
    student = cursor.fetchone()
    
    if not student:
        print("Student not found!")
        close_db(conn)
        return

    # Show update menu
    while True:
        print("\nChoose the attribute you want to update:")
        print("1. Room ID")
        print("2. Name")
        print("3. University Name")
        print("4. Date of Birth")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            cursor.execute("SELECT roomID, roomType, availableSeats FROM rooms WHERE availableSeats > 0")
            rooms = cursor.fetchall()
            if not rooms:
                print("\nNo available rooms found. Please add rooms first.")
                continue

            print("\n--- Available Rooms ---")
            for room in rooms:
                print(f"RoomID: {room[0]}, Type: {room[1]}, Available Seats: {room[2]}")
            
            new_roomID = int(input("\nEnter new Room ID: "))
            if new_roomID == student[1]:
                print("Student is already in this room!")
                continue

            # Check if the selected room is valid
            valid_room_ids = [room[0] for room in rooms]
            if new_roomID not in valid_room_ids:
                print("Invalid Room ID! Please select a valid room from the list above.")
                continue

            # Update the room and adjust available seats
            cursor.execute("UPDATE rooms SET availableSeats = availableSeats + 1 WHERE roomID = %s", (student[1],))
            cursor.execute("UPDATE rooms SET availableSeats = availableSeats - 1 WHERE roomID = %s", (new_roomID,))
            cursor.execute("UPDATE students SET roomID = %s WHERE studentID = %s", (new_roomID, studentID))
            conn.commit()
            print("Room ID updated successfully!")
        
        elif choice == '2':
            new_name = input("Enter new Name: ")
            cursor.execute("UPDATE students SET name = %s WHERE studentID = %s", (new_name, studentID))
            conn.commit()
            print("Name updated successfully!")
        
        elif choice == '3':
            new_university = input("Enter new University Name: ")
            cursor.execute("UPDATE students SET universityName = %s WHERE studentID = %s", (new_university, studentID))
            conn.commit()
            print("University Name updated successfully!")
        
        elif choice == '4':
            new_dob = input("Enter new Date of Birth (YYYY-MM-DD): ")
            cursor.execute("UPDATE students SET DOB = %s WHERE studentID = %s", (new_dob, studentID))
            conn.commit()
            print("Date of Birth updated successfully!")
        
        elif choice == '5':
            print("Exiting student update...")
            break
        
        else:
            print("Invalid choice! Please try again.")

    close_db(conn)



def update_room():
    conn = connect_db()
    if not conn:
        print("Failed to connect to the database")
        return

    roomID = int(input("\nEnter Room ID to update: "))
    
    # Check if room exists
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms WHERE roomID = %s", (roomID,))
    room = cursor.fetchone()
    
    if not room:
        print("Room not found!")
        close_db(conn)
        return

    # Show update menu
    while True:
        print("\nChoose the attribute you want to update:")
        print("1. Room Type")
        print("2. Total Seats")
        print("3. Available Seats")
        print("4. Rent")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            new_roomType = input("Enter new Room Type (Single/Shared): ")
            cursor.execute("UPDATE rooms SET roomType = %s WHERE roomID = %s", (new_roomType, roomID))
            conn.commit()
            print("Room Type updated successfully!")
        
        elif choice == '2':
            new_totalSeats = int(input("Enter new Total Seats: "))
            cursor.execute("UPDATE rooms SET totalSeats = %s WHERE roomID = %s", (new_totalSeats, roomID))
            conn.commit()
            print("Total Seats updated successfully!")
        
        elif choice == '3':
            new_availableSeats = int(input("Enter new Available Seats: "))
            cursor.execute("UPDATE rooms SET availableSeats = %s WHERE roomID = %s", (new_availableSeats, roomID))
            conn.commit()
            print("Available Seats updated successfully!")
        
        elif choice == '4':
            new_rent = float(input("Enter new Rent Amount: "))
            cursor.execute("UPDATE rooms SET rent = %s WHERE roomID = %s", (new_rent, roomID))
            conn.commit()
            print("Rent updated successfully!")
        
        elif choice == '5':
            print("Exiting room update...")
            break
        
        else:
            print("Invalid choice! Please try again.")

    close_db(conn)


def main():
    while True:
        print("\nHostel Management CLI")
        print("1. Show Rooms")
        print("2. Show Students")
        print("3. Add Room")
        print("4. Add Student")
        print("5. Update Student")
        print("6. Update Room")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            show_rooms()
        elif choice == '2':
            show_students()
        elif choice == '3':
            add_room()
        elif choice == '4':
            add_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            update_room()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

