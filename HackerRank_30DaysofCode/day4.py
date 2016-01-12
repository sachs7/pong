class Person:
        def __init__(self,initial_Age):
       		# Add some more code to run some checks on initial_Age
            if initial_Age < 0:
                initial_Age = 0
                print("This person is not valid, setting age to 0.")
            #initial_Age = age
        def amIOld(self):
            # Do some computations in here and print out the correct statement to the console
            if age < 13:
                print("You are young.")
            elif 13 <= age and age < 18:
                print("You are a teenager.")
            else:
                print("You are old.")
        def yearPasses(self):
            # Increment the age of the person in here     
            global age
            age += 1
