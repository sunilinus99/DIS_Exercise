# Import the classes from classhierarchy.py
from  import School, MiddleSchool, HighSchool

def main():
    # Create an instance of School
    school = School("Greenwood School", "Mr. Brown", 300)
    print("Generic School Details:")
    school.show_details()

    # Create an instance of MiddleSchool
    middle_school = MiddleSchool("Springfield Middle", "Ms. Watson", 450, 6, 8)
    print("\nMiddle School Details:")
    middle_school.show_details()

    # Create an instance of HighSchool
    high_school = HighSchool("Lincoln High", "Mr. Johnson", 700, "Falcon Stadium")
    print("\nHigh School Details:")
    high_school.show_details()

if __name__ == "__main__":
    main()
