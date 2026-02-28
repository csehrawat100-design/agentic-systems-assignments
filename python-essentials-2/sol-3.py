class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            if len(self.scores) == 0:
                raise ValueError('No scores available to calculate difference')
            else:
                difference = abs(self.scores[0] - self.scores[-1])
                print(f'Difference between first and last scores is: {difference}')
        except ValueError:
            print('No scores available to calculate difference')

scores_input = input("Enter scores separated by space: ")

scores_list = list(map(int, scores_input.split()))

s = StudentPerformance(scores_list)

s.score_difference()
            
