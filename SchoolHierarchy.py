class School:
    def __init__(self, name, principal, student_count):
        self.name = name
        self.principal = principal
        self.student_count = student_count

    def show_details(self):
        print(f"School Name: {self.name}")
        print(f"Principal: {self.principal}")
        print(f"Student Count: {self.student_count}")


class MiddleSchool(School):
    def __init__(self, name, principal, student_count, lowest_grade, highest_grade):
        # Call the base class constructor
        super().__init__(name, principal, student_count)
        self.lowest_grade = lowest_grade
        self.highest_grade = highest_grade

    def show_details(self):
        # Call the parent method to display general school details
        super().show_details()
        print(f"Lowest Grade: {self.lowest_grade}")
        print(f"Highest Grade: {self.highest_grade}")


class HighSchool(School):
    def __init__(self, name, principal, student_count, sports_field_name):
        # Call the base class constructor
        super().__init__(name, principal, student_count)
        self.sports_field_name = sports_field_name

    def show_details(self):
        # Call the parent method to display general school details
        super().show_details()
        print(f"Sports Field Name: {self.sports_field_name}")


if __name__ == "__main__":
    # Create an instance of the base class School
    school = School(name="Springfield Elementary", principal="Mr. Skinner", student_count=500)
    print("Details of the School:")
    school.show_details()

    print("\nDetails of the Middle School:")
    # Create an instance of the MiddleSchool subclass
    middle_school = MiddleSchool(name="Springfield Middle", principal="Ms. Krabappel", student_count=300, lowest_grade=6, highest_grade=8)
    middle_school.show_details()

    print("\nDetails of the High School:")
    # Create an instance of the HighSchool subclass
    high_school = HighSchool(name="Springfield High", principal="Ms. Hoover", student_count=400, sports_field_name="Bartman Stadium")
    high_school.show_details()
