from datetime import datetime

class Student:
    def _init_(self, student_id, name, seat_no):
        self.student_id = student_id
        self.name = name
        self.seat_no = seat_no
        self.purchase_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _str_(self):
        return f"{self.student_id} | {self.name} | Seat: {self.seat_no} | Time: {self.purchase_time}"


class LibraryManagementSystem:
    def _init_(self, total_cabins):
        self.total_cabins = total_cabins
        self.students = {}
        self.filled_cabins = {}

    def book_seat(self, student_id, name):
        free_cabins = self.get_free_cabins()
        if not free_cabins:
            print("❌ No free cabins available!")
            return
        seat_no = free_cabins[0]
        student = Student(student_id, name, seat_no)
        self.students[student_id] = student
        self.filled_cabins[seat_no] = student_id
        print(f"✅ Seat {seat_no} booked successfully for {name} at {student.purchase_time}")

    def release_seat(self, student_id):
        if student_id not in self.students:
            print("❌ Student record not found.")
            return
        seat_no = self.students[student_id].seat_no
        del self.students[student_id]
        del self.filled_cabins[seat_no]
        print(f"✅ Seat {seat_no} released successfully.")

    def get_free_cabins(self):
        return [i for i in range(1, self.total_cabins + 1) if i not in self.filled_cabins]

    def get_filled_cabins(self):
        return list(self.filled_cabins.keys())

    def show_records(self):
        if not self.students:
            print("📭 No records available.")
            return
        print("\n📚 Current Student Records:")
        for s in self.students.values():
            print(s)


# Example usage:
if _name_ == "_main_":
    system = LibraryManagementSystem(total_cabins=10)

    while True:
        print("\n--- Library Management Menu ---")
        print("1. Book a Seat")
        print("2. Release a Seat")
        print("3. Show All Records")
        print("4. Show Free Cabins")
        print("5. Show Filled Cabins")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter student ID: ")
            name = input("Enter student name: ")
            system.book_seat(sid, name)
        elif choice == "2":
            sid = input("Enter student ID to release: ")
            system.release_seat(sid)
        elif choice == "3":
            system.show_records()
        elif choice == "4":
            print("🟩 Free Cabins:", system.get_free_cabins())
        elif choice == "5":
            print("🟥 Filled Cabins:", system.get_filled_cabins())
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")