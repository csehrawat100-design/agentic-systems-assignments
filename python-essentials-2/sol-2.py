class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise ValueError
        
            else:
                last_two = self.scores[-2:]
                highest = max(last_two)
                print(f'Highest score among last two is: {highest}')
        except ValueError:   
            print('Not enough scores to find highest value')    

scores_input = input("Enter scores separated by space: ")

scores_list = list(map(int, scores_input.split()))

s = StudentScores(scores_list)

s.highest_last_two()