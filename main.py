import os
import json
import re
import getpass
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

DATA_FILE = "hobby_club_data.json"

# ==========================================
# 1. DATABASE & PERSISTENCE MANAGER
# ==========================================
class DatabaseManager:
    """Handles persistent storage of club data using a local JSON file."""
    
    @staticmethod
    def initialize_db() -> Dict[str, List[Dict[str, Any]]]:
        if not os.path.exists(DATA_FILE):
            default_data = {
                "members": [
                    {"name": "Alice Smith", "age": 22, "level": "Beginner", "passcode": "pass123"},
                    {"name": "Bob Jones", "age": 28, "level": "Pro", "passcode": "pass123"},
                    {"name": "Charlie Brown", "age": 35, "level": "Expert", "passcode": "pass123"}
                ],
                "mentors": [
                    {"name": "David Miller", "age": 40, "level": "Junior", "coaching_duration": "2 years", "passcode": "mentor123"},
                    {"name": "Emma Wilson", "age": 45, "level": "Senior", "coaching_duration": "5 years", "passcode": "mentor123"},
                    {"name": "Frank Castle", "age": 50, "level": "Senior", "coaching_duration": "7 years", "passcode": "mentor123"}
                ],
                "admins": [
                    {"name": "Grace Hopper", "age": 55, "level": "Senior", "coaching_duration": "10 years", "passcode": "admin123"},
                    {"name": "Alan Turing", "age": 48, "level": "Senior", "coaching_duration": "8 years", "passcode": "admin123"},
                    {"name": "Ada Lovelace", "age": 52, "level": "Senior", "coaching_duration": "12 years", "passcode": "admin123"}
                ],
                "audit_logs": [
                    {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "action": "SYSTEM_INIT",
                        "details": "Database initialized with default seeded records."
                    }
                ]
            }
            DatabaseManager.save_data(default_data)
            return default_data
        
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("[Warning] Corrupted database file detected. Reinitializing...")
            return DatabaseManager.initialize_db()

    @staticmethod
    def save_data(data: Dict[str, List[Dict[str, Any]]]) -> None:
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"[Critical Error] Failed to write to database: {e}")

    @staticmethod
    def log_action(action: str, details: str) -> None:
        data = DatabaseManager.initialize_db()
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details
        }
        data["audit_logs"].append(log_entry)
        DatabaseManager.save_data(data)


# ==========================================
# 2. ABSTRACT BASE CLASS & INHERITANCE HIERARCHY
# ==========================================
class Person(ABC):
    """Abstract base class representing a human entity within the club."""
    
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer.")
        self._age = value

    @abstractmethod
    def show_info(self) -> None:
        """Display basic profile information."""
        pass

    @abstractmethod
    def portfolio(self) -> None:
        """Display detailed portfolio view."""
        pass


class Member(Person):
    """Member entity inheriting from Person."""
    
    VALID_LEVELS = {"Beginner", "Pro", "Expert", "Trained"}

    def __init__(self, name: str, age: int, level: str, passcode: str):
        super().__init__(name, age)
        self.level = level
        self.__passcode = passcode

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, value: str) -> None:
        if value not in self.VALID_LEVELS:
            raise ValueError(f"Invalid member level. Choose from: {', '.join(self.VALID_LEVELS)}")
        self._level = value

    def verify_passcode(self, passcode: str) -> bool:
        return self.__passcode == passcode

    def set_passcode(self, new_passcode: str) -> None:
        if len(new_passcode) < 4:
            raise ValueError("Passcode must be at least 4 characters long.")
        self.__passcode = new_passcode

    def show_info(self) -> None:
        print(f"--- Member Profile ---")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Level: {self.level}")

    def portfolio(self) -> None:
        print(f"==============================")
        print(f"   MEMBER PORTFOLIO CARD     ")
        print(f"==============================")
        print(f"Full Name       : {self.name}")
        print(f"Age             : {self.age}")
        print(f"Membership Tier : {self.level}")
        print(f"Role            : General Member")
        print(f"==============================")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "age": self.age,
            "level": self.level,
            "passcode": self.__passcode
        }


class Mentor(Person):
    """Mentor entity inheriting from Person."""
    
    VALID_LEVELS = {"Junior", "Senior"}

    def __init__(self, name: str, age: int, level: str, coaching_duration: str, passcode: str):
        super().__init__(name, age)
        self.level = level
        self.coaching_duration = coaching_duration
        self.__passcode = passcode

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, value: str) -> None:
        if value not in self.VALID_LEVELS:
            raise ValueError(f"Invalid mentor level. Choose from: {', '.join(self.VALID_LEVELS)}")
        self._level = value

    def verify_passcode(self, passcode: str) -> bool:
        return self.__passcode == passcode

    def set_passcode(self, new_passcode: str) -> None:
        if len(new_passcode) < 4:
            raise ValueError("Passcode must be at least 4 characters long.")
        self.__passcode = new_passcode

    def show_info(self) -> None:
        print(f"--- Mentor Profile ---")
        print(f"Name              : {self.name}")
        print(f"Age               : {self.age}")
        print(f"Level             : {self.level}")
        print(f"Coaching Duration : {self.coaching_duration}")

    def portfolio(self) -> None:
        print(f"==============================")
        print(f"   MENTOR PORTFOLIO CARD     ")
        print(f"==============================")
        print(f"Full Name         : {self.name}")
        print(f"Age               : {self.age}")
        print(f"Mentor Level      : {self.level}")
        print(f"Coaching Experience: {self.coaching_duration}")
        print(f"Role              : Club Mentor")
        print(f"==============================")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "age": self.age,
            "level": self.level,
            "coaching_duration": self.coaching_duration,
            "passcode": self.__passcode
        }


class Admin(Mentor):
    """Admin entity inheriting from Mentor (Multilevel: Person -> Mentor -> Admin)."""
    
    def __init__(self, name: str, age: int, level: str, coaching_duration: str, passcode: str):
        super().__init__(name, age, level, coaching_duration, passcode)

    def show_info(self) -> None:
        print(f"--- Administrator Profile ---")
        print(f"Name              : {self.name}")
        print(f"Age               : {self.age}")
        print(f"Level             : {self.level}")
        print(f"Coaching Duration : {self.coaching_duration}")
        print(f"Privilege Level   : Full System Access")

    def portfolio(self) -> None:
        print(f"==============================")
        print(f"    ADMIN PORTFOLIO CARD     ")
        print(f"==============================")
        print(f"Full Name         : {self.name}")
        print(f"Age               : {self.age}")
        print(f"Level             : {self.level}")
        print(f"Experience        : {self.coaching_duration}")
        print(f"Role              : Club Administrator")
        print(f"==============================")

    def to_dict(self) -> Dict[str, Any]:
        return super().to_dict()


# ==========================================
# 3. SYSTEM CONTROLLER & INTERFACE
# ==========================================
class HobbyClubSystem:
    """Main Application Controller for the Hobby Club Management System."""

    def __init__(self):
        self.db_data = DatabaseManager.initialize_db()

    def reload_db(self) -> None:
        self.db_data = DatabaseManager.initialize_db()

    def run(self) -> None:
        while True:
            print("\n========================================")
            print("   HOBBY CLUB MANAGEMENT SYSTEM (HCMS)  ")
            print("========================================")
            print("1. Enter as Guest")
            print("2. Login as Member")
            print("3. Login as Mentor")
            print("4. Login as Administrator")
            print("5. Exit Application")
            
            choice = input("Select an option (1-5): ").strip()
            
            if choice == "1":
                self.guest_menu()
            elif choice == "2":
                self.member_login()
            elif choice == "3":
                self.mentor_login()
            elif choice == "4":
                self.admin_login()
            elif choice == "5":
                print("\nThank you for using the Hobby Club Management System. Goodbye!")
                break
            else:
                print("[Error] Invalid selection. Please choose between 1 and 5.")

    # ------------------------------------------
    # GUEST MODULE
    # ------------------------------------------
    def guest_menu(self) -> None:
        while True:
            print("\n--- GUEST PORTAL ---")
            print("1. Browse Public Rosters")
            print("2. Register as a New Member")
            print("3. Return to Main Menu")
            
            choice = input("Select an option (1-3): ").strip()
            
            if choice == "1":
                self.display_public_rosters()
            elif choice == "2":
                self.register_member()
            elif choice == "3":
                break
            else:
                print("[Error] Invalid option. Try again.")

    def display_public_rosters(self) -> None:
        self.reload_db()
        print("\n--- PUBLIC CLUB ROSTERS ---")
        
        print("\n[Members]")
        for m in self.db_data["members"]:
            print(f" - {m['name']} (Age: {m['age']}, Level: {m['level']})")
            
        print("\n[Mentors]")
        for men in self.db_data["mentors"]:
            print(f" - {men['name']} (Age: {men['age']}, Level: {men['level']}, Experience: {men['coaching_duration']})")
            
        print("\n[Administrators]")
        for adm in self.db_data["admins"]:
            print(f" - {adm['name']} (Age: {adm['age']}, Experience: {adm['coaching_duration']})")

    def register_member(self) -> None:
        print("\n--- MEMBER REGISTRATION ---")
        name = input("Enter your full name: ").strip()
        if not name:
            print("[Error] Name cannot be blank.")
            return

        try:
            age = int(input("Enter your age: ").strip())
        except ValueError:
            print("[Error] Age must be a valid integer number.")
            return

        print("Select Level: 1. Beginner  2. Pro  3. Expert  4. Trained")
        lvl_choice = input("Select level (1-4): ").strip()
        level_map = {"1": "Beginner", "2": "Pro", "3": "Expert", "4": "Trained"}
        level = level_map.get(lvl_choice)
        
        if not level:
            print("[Error] Invalid level selection.")
            return

        passcode = getpass.getpass("Create a secret passcode (min 4 chars): ").strip()
        if len(passcode) < 4:
            print("[Error] Passcode must be at least 4 characters.")
            return

        try:
            new_member = Member(name, age, level, passcode)
            self.reload_db()
            self.db_data["members"].append(new_member.to_dict())
            DatabaseManager.save_data(self.db_data)
            DatabaseManager.log_action("MEMBER_REGISTER", f"New member registered: {name}")
            print(f"[Success] Welcome aboard, {name}! You are now registered as a Member.")
        except ValueError as e:
            print(f"[Validation Error]: {e}")

    # ------------------------------------------
    # MEMBER MODULE
    # ------------------------------------------
    def member_login(self) -> None:
        self.reload_db()
        name = input("Enter your registered Member name: ").strip()
        member_data = next((m for m in self.db_data["members"] if m["name"].lower() == name.lower()), None)
        
        if not member_data:
            print("[Error] Member account not found.")
            return

        passcode = getpass.getpass("Enter your passcode: ").strip()
        if member_data["passcode"] != passcode:
            print("[Error] Incorrect passcode.")
            return

        member_obj = Member(member_data["name"], member_data["age"], member_data["level"], member_data["passcode"])
        print(f"\n[Success] Logged in successfully as Member: {member_obj.name}")
        self.member_session(member_obj)

    def member_session(self, member: Member) -> None:
        while True:
            print(f"\n--- MEMBER DASHBOARD: {member.name} ---")
            print("1. View Personal Portfolio Card")
            print("2. View Other Club Members")
            print("3. Search Mentors & Admins")
            print("4. Logout")
            
            choice = input("Select an option (1-4): ").strip()
            
            if choice == "1":
                member.portfolio()
            elif choice == "2":
                self.reload_db()
                print("\n--- Other Club Members ---")
                for m in self.db_data["members"]:
                    if m["name"].lower() != member.name.lower():
                        print(f" - {m['name']} (Level: {m['level']}, Age: {m['age']})")
            elif choice == "3":
                self.search_directory()
            elif choice == "4":
                print("[Info] Logging out from Member session.")
                break
            else:
                print("[Error] Invalid selection.")

    # ------------------------------------------
    # MENTOR MODULE
    # ------------------------------------------
    def mentor_login(self) -> None:
        self.reload_db()
        name = input("Enter your registered Mentor name: ").strip()
        mentor_data = next((m for m in self.db_data["mentors"] if m["name"].lower() == name.lower()), None)
        
        if not mentor_data:
            print("[Error] Mentor account not found.")
            return

        passcode = getpass.getpass("Enter your passcode: ").strip()
        if mentor_data["passcode"] != passcode:
            print("[Error] Incorrect passcode.")
            return

        mentor_obj = Mentor(mentor_data["name"], mentor_data["age"], mentor_data["level"], mentor_data["coaching_duration"], mentor_data["passcode"])
        print(f"\n[Success] Logged in successfully as Mentor: {mentor_obj.name}")
        self.mentor_session(mentor_obj)

    def mentor_session(self, mentor: Mentor) -> None:
        while True:
            print(f"\n--- MENTOR DASHBOARD: {mentor.name} ---")
            print("1. View Personal Portfolio Card")
            print("2. View Complete Club Rosters")
            print("3. Search Club Directory")
            print("4. Logout")
            
            choice = input("Select an option (1-4): ").strip()
            
            if choice == "1":
                mentor.portfolio()
            elif choice == "2":
                self.display_public_rosters()
            elif choice == "3":
                self.search_directory()
            elif choice == "4":
                print("[Info] Logging out from Mentor session.")
                break
            else:
                print("[Error] Invalid selection.")

    # ------------------------------------------
    # ADMIN MODULE
    # ------------------------------------------
    def admin_login(self) -> None:
        self.reload_db()
        name = input("Enter your Administrator name: ").strip()
        admin_data = next((a for a in self.db_data["admins"] if a["name"].lower() == name.lower()), None)
        
        if not admin_data:
            print("[Error] Administrator account not found.")
            return

        passcode = getpass.getpass("Enter your passcode: ").strip()
        if admin_data["passcode"] != passcode:
            print("[Error] Incorrect passcode.")
            return

        admin_obj = Admin(admin_data["name"], admin_data["age"], admin_data["level"], admin_data["coaching_duration"], admin_data["passcode"])
        print(f"\n[Success] Logged in successfully as Administrator: {admin_obj.name}")
        self.admin_session(admin_obj)

    def admin_session(self, admin: Admin) -> None:
        while True:
            print(f"\n--- ADMIN DASHBOARD: {admin.name} ---")
            print("1. View Personal Portfolio Card")
            print("2. Create New User (Member/Mentor/Admin)")
            print("3. Modify User Tier / Level")
            print("4. Delete User Account by Name")
            print("5. View System Audit Logs")
            print("6. Logout")
            
            choice = input("Select an option (1-6): ").strip()
            
            if choice == "1":
                admin.portfolio()
            elif choice == "2":
                self.admin_create_user(admin.name)
            elif choice == "3":
                self.admin_modify_tier(admin.name)
            elif choice == "4":
                self.admin_delete_user(admin.name)
            elif choice == "5":
                self.admin_view_logs()
            elif choice == "6":
                print("[Info] Logging out from Admin session.")
                break
            else:
                print("[Error] Invalid option.")

    def admin_create_user(self, admin_name: str) -> None:
        print("\n--- CREATE NEW USER ACCOUNT ---")
        print("Select Role to Create: 1. Member  2. Mentor  3. Admin")
        role_choice = input("Enter choice (1-3): ").strip()
        
        if role_choice not in {"1", "2", "3"}:
            print("[Error] Invalid role selection.")
            return

        name = input("Enter full name: ").strip()
        if not name:
            print("[Error] Name cannot be empty.")
            return

        try:
            age = int(input("Enter age: ").strip())
        except ValueError:
            print("[Error] Age must be an integer.")
            return

        passcode = getpass.getpass("Set passcode (min 4 chars): ").strip()
        if len(passcode) < 4:
            print("[Error] Passcode must be at least 4 characters long.")
            return

        self.reload_db()

        if role_choice == "1":
            print("Select Level: 1. Beginner  2. Pro  3. Expert  4. Trained")
            lvl_c = input("Choice (1-4): ").strip()
            level_map = {"1": "Beginner", "2": "Pro", "3": "Expert", "4": "Trained"}
            level = level_map.get(lvl_c, "Beginner")
            
            new_member = Member(name, age, level, passcode)
            self.db_data["members"].append(new_member.to_dict())
            DatabaseManager.save_data(self.db_data)
            DatabaseManager.log_action("ADMIN_CREATE_MEMBER", f"Admin {admin_name} created Member: {name}")
            print(f"[Success] Member '{name}' created successfully.")

        elif role_choice in {"2", "3"}:
            print("Select Mentor Level: 1. Junior  2. Senior")
            lvl_c = input("Choice (1-2): ").strip()
            level = "Senior" if lvl_c == "2" else "Junior"
            duration = input("Enter coaching duration (e.g., '3 years'): ").strip()
            
            if role_choice == "2":
                new_mentor = Mentor(name, age, level, duration, passcode)
                self.db_data["mentors"].append(new_mentor.to_dict())
                DatabaseManager.save_data(self.db_data)
                DatabaseManager.log_action("ADMIN_CREATE_MENTOR", f"Admin {admin_name} created Mentor: {name}")
                print(f"[Success] Mentor '{name}' created successfully.")
            else:
                new_admin = Admin(name, age, level, duration, passcode)
                self.db_data["admins"].append(new_admin.to_dict())
                DatabaseManager.save_data(self.db_data)
                DatabaseManager.log_action("ADMIN_CREATE_ADMIN", f"Admin {admin_name} created Admin: {name}")
                print(f"[Success] Administrator '{name}' created successfully.")

    def admin_modify_tier(self, admin_name: str) -> None:
        self.reload_db()
        print("\n--- MODIFY USER TIER / LEVEL ---")
        print("Select Target Category: 1. Member  2. Mentor")
        cat = input("Choice (1-2): ").strip()
        
        if cat == "1":
            target_list = self.db_data["members"]
            category_key = "members"
        elif cat == "2":
            target_list = self.db_data["mentors"]
            category_key = "mentors"
        else:
            print("[Error] Invalid category selection.")
            return

        name_query = input("Enter exact or partial name of user to modify: ").strip()
        matches = [u for u in target_list if name_query.lower() in u["name"].lower()]
        
        if not matches:
            print("[Error] No matching user found.")
            return

        print("\nMatching Users:")
        for idx, u in enumerate(matches):
            print(f"{idx + 1}. {u['name']} (Current Level: {u['level']})")

        try:
            sel = int(input("Select user number to modify: ").strip()) - 1
            selected_user = matches[sel]
        except (ValueError, IndexError):
            print("[Error] Invalid selection.")
            return

        if category_key == "members":
            print("New Level: 1. Beginner  2. Pro  3. Expert  4. Trained")
            lm = {"1": "Beginner", "2": "Pro", "3": "Expert", "4": "Trained"}
            new_lvl = lm.get(input("Choice (1-4): ").strip())
        else:
            print("New Level: 1. Junior  2. Senior")
            lm = {"1": "Junior", "2": "Senior"}
            new_lvl = lm.get(input("Choice (1-2): ").strip())

        if not new_lvl:
            print("[Error] Invalid level choice.")
            return

        # Update record in main storage
        for u in self.db_data[category_key]:
            if u["name"] == selected_user["name"]:
                u["level"] = new_lvl
                break

        DatabaseManager.save_data(self.db_data)
        DatabaseManager.log_action("ADMIN_MODIFY_TIER", f"Admin {admin_name} changed tier of {selected_user['name']} to {new_lvl}")
        print(f"[Success] User {selected_user['name']}'s tier updated to '{new_lvl}' successfully.")

    def admin_delete_user(self, admin_name: str) -> None:
        self.reload_db()
        print("\n--- DELETE USER ACCOUNT ---")
        name_query = input("Enter exact name of user to delete: ").strip()
        
        deleted = False
        for cat in ["members", "mentors"]:
            initial_len = len(self.db_data[cat])
            self.db_data[cat] = [u for u in self.db_data[cat] if u["name"].lower() != name_query.lower()]
            if len(self.db_data[cat]) < initial_len:
                deleted = True
                break

        if deleted:
            DatabaseManager.save_data(self.db_data)
            DatabaseManager.log_action("ADMIN_DELETE_USER", f"Admin {admin_name} deleted user: {name_query}")
            print(f"[Success] Account '{name_query}' deleted successfully.")
        else:
            print("[Error] User account not found in Members or Mentors database.")

    def admin_view_logs(self) -> None:
        self.reload_db()
        print("\n========================================")
        print("          SYSTEM AUDIT LOGS             ")
        print("========================================")
        for log in self.db_data["audit_logs"]:
            print(f"[{log['timestamp']}] ({log['action']}) -> {log['details']}")
        print("========================================")

    # ------------------------------------------
    # SHARED SEARCH CAPABILITY (REGEX / PARTIAL)
    # ------------------------------------------
    def search_directory(self) -> None:
        self.reload_db()
        print("\n--- DIRECTORY SEARCH (Mentors & Admins) ---")
        query = input("Enter name or keyword to search: ").strip()
        
        if not query:
            print("[Error] Search query cannot be empty.")
            return

        pattern = re.compile(re.escape(query), re.IGNORECASE)
        results = []

        for m in self.db_data["mentors"]:
            if pattern.search(m["name"]) or pattern.search(m["level"]):
                results.append(("Mentor", m))

        for a in self.db_data["admins"]:
            if pattern.search(a["name"]) or pattern.search(a["level"]):
                results.append(("Administrator", a))

        if not results:
            print("[Info] No matching mentors or administrators found.")
            return

        print(f"\nFound {len(results)} matching result(s):")
        for role, entity in results:
            print(f" - [{role}] {entity['name']} | Age: {entity['age']} | Level: {entity['level']} | Experience: {entity['coaching_duration']}")


# ==========================================
# 4. ENTRY POINT
# ==========================================
if __name__ == "__main__":
    app = HobbyClubSystem()
    app.run()
