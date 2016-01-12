class Grade(Student):

    def __init__(self, firstName, lastName, phone, score):
        super().__init__(firstName, lastName, phone)
        self.score = score
        
    def calculate(self):
        if score < 40:
            return "D"
        elif 40 <= score < 60:
            return "B"
        elif 60 <= score < 75:
            return "A"
        elif 75 <= score < 90:
            return "E"
        else:
            return "O"
