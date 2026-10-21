#Final Project - Hobby club
#Pillers: Hybrid Inheritance, Private encapsulation, Polymorphism

# ===== Base Class =====
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"👤 Name: {self.name} \n🎂 Age: {self.age}")

# ===== Member Class ===========================
class Member(Person):
    def __init__(self, name, age, level, passcode):
        super().__init__(name, age)
        self.level = level
        self.__passcode = passcode  # private encapsulation
    
    def show_info(self, name, age, level):
        super().__init__(name, age)
        print(f"Member name: {self.name} \nAge: {self.age} \nCurrent Level: {self.level}")
        print("")
        print("---------")

    def check_passcode(self, code):
        return self.__passcode == code

    def portfolio(self):   # Polymorphism
        print("\n📂 Member Portfolio")
        print(f"👤 Name: {self.name}")
        print(f"🎂 Age: {self.age}")
        print(f"📈 Level: {self.level}")
        print(f"🔑 Passcode: {self.__passcode}")

# ===== Mentor Class =====
class Mentor(Person):
    def __init__(self, name, age, level, passcode, duration=None):
        super().__init__(name, age)
        self.level = level
        self.passcode = passcode
        self.duration = duration

    def show_info(self):
        print(f"Mentor name: {self.name} \nAge: {self.age} \nCurrent Level: {self.level}")
        print("")

    def portfolio(self):   # Polymorphism
        print("\n📂 Mentor Portfolio")
        print(f"👤 Name: {self.name}")
        print(f"🎂 Age: {self.age}")
        print(f"📈 Level: {self.level}")
        print(f"⏳ Duration: {self.duration}")
        print(f"🔑 Passcode: {self.passcode}")


# ===== Admin Class (Hybrid Inheritance) =====
class Admin(Mentor):
    def __init__(self, name, age, level, passcode, duration):
        super().__init__(name, age, level, passcode, duration)

    def portfolio(self):   # Polymorphism
        print("\n📂 Admin Portfolio")
        print(f"👤 Name: {self.name}")
        print(f"🎂 Age: {self.age}")
        print(f"📈 Level: {self.level}")
        print(f"⏳ Duration: {self.duration}")
        print(f"🔑 Passcode: {self.passcode}")
    
    def show_info(self):
        print(f"Admin name: {self.name} \nAge: {self.age} \nLevel: {self.level}")
        print("-------")
        print("")

    # Admin powers
    def add_member(self, member_list, member_obj):
        member_list.append(member_obj)
        print(f"✅ Member {member_obj.name} has been added successfully!")

    def add_mentor(self, mentor_list, mentor_obj):
        mentor_list.append(mentor_obj)
        print(f"✅ Mentor {mentor_obj.name} has been added successfully!")

    def remove_member(self, member_list, name):
        for m in member_list:
            if m.name.lower().lstrip() == name.lower().lstrip():
                member_list.remove(m)
                print(f"❌ Member {m.name} has been removed.")
                return
        print("⚠️ No member found with that name.")

    def remove_mentor(self, mentor_list, name):
        for mt in mentor_list:
            if mt.name.lower().lstrip() == name.lower().lstrip():
                mentor_list.remove(mt)
                print(f"❌ Mentor {mt.name} has been removed.")
                return
        print("⚠️ No mentor found with that name.")


# ===== Declared Data =====
members = [
    Member("Rahim", 18, "Beginner", "m1"),
    Member("Karim", 19, "Pro", "m2"),
    Member("Sajid", 20, "Expert", "m3"),
    Member("Nadia", 21, "Educated", "m4"),
    Member("Rafi", 22, "Trained", "m5"),
    Member("Hasan", 23, "Beginner", "m6"),
    Member("Mitu", 24, "Pro", "m7"),
    Member("Shila", 25, "Expert", "m8"),
    Member("Babul", 26, "Educated", "m9"),
    Member("Tania", 27, "Trained", "m10")
]

mentors = [
    Mentor("Mr. Smith", 35, "Junior", "mt1", "2 years"),
    Mentor("Mr. Harper", 36, "Senior", "mt2", "3 years"),
    Mentor("Mr. Mohsin", 37, "Junior", "mt3", "4 years"),
    Mentor("Mr. Rayhan", 38, "Senior", "mt4", "5 years"),
    Mentor("Mr. Jamal", 39, "Junior", "mt5", "6 years")
]

admins = [
    Admin("Mr. Aleem", 45, "Junior", "ad1", "2 years"),
    Admin("Mr. Mufti", 46, "Senior", "ad2", "3 years"),
    Admin("Mr. Hafez", 47, "Junior", "ad3", "4 years"),
    Admin("Mr. Kaari", 48, "Senior", "ad4", "5 years"),
    Admin("Mr. Hujur", 49, "Junior", "ad5", "6 years")
]

# ===== Menus =====
def member_menu(member):
    while True:
        print("\n--- 👤 Member Menu ---")
        print("1. 👥 See other members")
        print("2. 👨‍🏫 See mentors")
        print("3. 🛡️ See admins")
        print("4. 📂 See your portfolio")
        print("5. 🚪 Exit")
        choice = input("Choice: ")

        if choice == "1":
            for m in members:
                if m != member: 
                    m.show_info(m.name, m.age, m.level) 
                    print("----------------")

        elif choice == "2":
            for mt in mentors: 
                mt.show_info()

        elif choice == "3":
            for ad in admins: 
                ad.show_info()

        elif choice == "4":
            member.portfolio()

        elif choice == "5":
            print("👋 Exiting Member Menu...")
            break

        else:
            print("⚠️ Invalid choice, try again.")

def mentor_menu(mentor):
    while (True):
        print("\n--- 👨‍🏫 Mentor Menu ---")
        print("1. 👨‍🏫 See other mentors")
        print("2. 👥 See members")
        print("3. 🛡️ See admins")
        print("4. 📂 See your portfolio")
        print("5. 🚪 Exit")
        choice = input("Choice: ")

        if choice == "1":
            for mt in mentors:
                if mt != mentor: mt.show_info()
                print("--------------")

        elif choice == "2":
            for m in members: 
                m.show_info(m.name, m.age, m.level)

        elif choice == "3":
            for ad in admins: 
                ad.show_info()

        elif choice == "4":
            mentor.portfolio()

        elif choice == "5":
            print("👋 Exiting Mentor Menu... \nGoodbye.")
            break
        else:
            print("⚠️ Invalid choice, try again.")


def admin_menu(admin):
    while True:
        print("\n--- 🛡️ Admin Menu ---")
        print("1. 👥 See members")
        print("2. 👨‍🏫 See mentors")
        print("3. 🛡️ See other admins")
        print("4. 📂 See your portfolio")
        print("5. ➕ Add member")
        print("6. ➕ Add mentor")
        print("7. ❌ Remove mentor")
        print("8. ❌ Remove member")
        print("9. 🚪 Exit")
        choice = input("Choice: ")
        choice = choice.lstrip()

        if choice == "1":
            for m in members: 
                m.show_info(m.name, m.age, m.level)

        elif choice == "2":
            for mt in mentors: 
                mt.show_info()

        elif choice == "3":
            for ad in admins:
                if ad != admin: 
                    ad.show_info()

        elif choice == "4":
            admin.portfolio()

        elif choice == "5":
            name = input("Name: ")
            age = int(input("Age: "))
            level = input("Level: ")
            passcode = input("Passcode: ")
            new_member = Member(name, age, level, passcode)
            admin.add_member(members, new_member)

        elif choice == "6":
            name = input("Name: ")
            age = int(input("Age: "))
            level = input("Level: ")
            passcode = input("Passcode: ")
            duration = input("Duration: ")
            new_mentor = Mentor(name, age, level, passcode, duration)
            admin.add_mentor(mentors, new_mentor)

        elif choice == "7":
            name = input("Enter mentor name to remove: ")
            admin.remove_mentor(mentors, name)

        elif choice == "8":
            name = input("Enter member name to remove: ")
            admin.remove_member(members, name)

        elif choice == "9":
            print("👋 Exiting Admin Menu...")
            break

        else:
            print("⚠️ Invalid choice, try again.")


# New member entering process
def new_member():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    level = input("Enter Level (Beginner, Pro, Expert, Educated, Trained): ")
    passcode = input("Enter Passcode: ")

    new_member = Member(name, age, level, passcode)
    members.append(new_member)
    print("🎉 You are now a Member! \nWe are glad that you are here.!!!")
    member_menu(new_member)


# ===== Main =====
print("=== 🎉 Welcome to Hobby Club ===")
print("1. 👤 Regular Member")
print("2. 👨‍🏫 Mentor")
print("3. 🛡️ Admin")
print("4. 👥 Guest")
role = input("Enter choice: ")

if role == "1":
    for i in range(3): 
        name = input("Enter Member Name: ")
        level = input("Enter Member Level: ")
        passcode = input("Enter Member Passcode: ")

        for m in members:
            if m.name.lower().lstrip() == name.lower().lstrip() and m.level.lower().lstrip() == level.lower().lstrip() and m.check_passcode(passcode):
                print("✅ Login successful as Member!")
                member_menu(m)
                break
     
        else:
            print("❌ Invalid Member login.")
            print(f"You have {2-i} opportunity to try again.")
            continue
        break

elif role == "2":
    for i in range(3): 
        name = input("Enter Mentor Name: ")
        level = input("Enter Mentor Level: ")
        passcode = input("Enter Mentor Passcode: ")

        for mt in mentors:
            if mt.name.lower() == name.lower() and mt.level.lower() == level.lower() and mt.passcode == passcode:
                print("✅ Login successful as Mentor!")
                mentor_menu(mt)
                break
        else:
            print("❌ Invalid Mentor login.")
            print(f"You have {2-i} opportunity to try again.")
            continue
        break  

elif role == "3":
    for i in range(3):
        name = input("Enter Admin Name: ")
        passcode = input("Enter Admin Passcode: ")
        for ad in admins:
            if ad.name.lower().lstrip() == name.lower().lstrip() and ad.passcode == passcode:
                print("✅ Login successful as Admin!")
                admin_menu(ad)
                break
        else:
            print("❌ Invalid Admin login.")
            print(f"Try again. You have {2-i} opportunity to try")
            continue
        break

elif role == "4":
    while True:
        print("\n\n--- 👥 Guest Menu ---")
        print("1. 👥 See members")
        print("2. 👨‍🏫 See mentors")
        print("3. 🛡️ See admins")
        print("4. 🤝 Join our club")
        print("5. 🚪 Exit")
        choice = input("Choice: ")
        print("")

        if choice == "1":
            for m in members: 
                m.show_info(m.name, m.age, m.level)

        elif choice == "2":
            for mt in mentors: 
                mt.show_info()

        elif choice == "3":
            for ad in admins: 
                ad.show_info()

        elif choice == "4":
            new_member()
        
        elif choice == "5":
            print("👋 Thanks for visiting as Guest!")
            print("🤝 You can join any time when you are interested.")
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

else:
    print("Invalid choice!")
    print("Try again.")
