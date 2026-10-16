class Workout :
    # variables
    def __init__ (self, trainer_id, member_id, exercise, purpose, duration) :
        self.trainer_id = trainer_id
        self.member_id = member_id
        self.exercise = exercise
        self.purpose = purpose
        self.duration = duration
    # methods
    # calculate total duration
    def calculate_duration (self) :
        total_time = 0
        for time in self.duration :
            total_time+=time
        return total_time