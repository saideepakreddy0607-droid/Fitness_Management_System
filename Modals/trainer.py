class Trainer :
    # variables
    def __init__ (self, trainer_id, trainer_name, trainer_phno) :
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        self.trainer_phno = trainer_phno
    # methods
    # update workout
    def add_exercise(self, workout, exercise, duration) :
        workout.exercise.append(exercise)
        workout.duration.append(duration)
    def delete_exercise(self, workout, exercise) :
        index = -1
        for i in range (0, len(workout.exercise)) :
            if workout.exercise[i] == exercise:
                del workout.exercise[i]
                index = i
                break
        if index!= -1 : del workout.duration[index]
    def update_exercise(self, workout, exercise, duration) :
        index = -1
        for i in range (0, len(workout.exercise)) :
            if workout.exercise[i] == exercise:
                index = i
                break
        if index!= -1 : workout.duration[index] = duration