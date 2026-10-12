 
class FindPercent:
    def percentage(self):
        subject1 = 98
        subject2 = 95
        subject3 = 92
        subject4 = 90
        subject5 = 88

        grand_total = 500
        total = subject1 + subject2 + subject3 + subject4 + subject5

        percentage = (total / grand_total) * 100

        print("Subject 1:", subject1)
        print("Subject 2:", subject2)
        print("Subject 3:", subject3)
        print("Subject 4:", subject4)
        print("Subject 5:", subject5)
        print("Total Marks:", total)
        print("Percentage:", percentage)

        return percentage

