class TimeSlot:
    def __init__(self, start_time, end_time):
        """
        start_time: an integer representing 24-hour time (e.g. 2345 for 11:45 PM)
        end_time: an integer representing 24-hour time (e.g. 745 for 7:45 AM)
        """
        self.start_time = start_time
        self.end_time = end_time
        
        
    def is_contained_in(self, timeslot):
        """
        Checks if the current time slot is contained within timeslot
        """
        return_val = (self.start_time >= timeslot.start_time) and (self.end_time <= timeslot.end_time)
        return return_val
    
    def time_slot_length(self):
        return self.end_time - self.start_time
    
    def __str__(self):
        return str(start_time) + str(end_time)
    