class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:    
            if len(self.marks) < 3:
                raise ValueError
            else:
                last_three = self.marks[-3:]
                average = sum(last_three) / len(last_three)
                print(f'Average of last 3 marks is: {average}')
        
        except ValueError:
            print("Not enough marks to calculate average")

marks_input = input("Enter marks separated by space: ")

marks_list = list(map(int, marks_input.split()))

s = StudentMarks(marks_list)

s.last_three_avg()
