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
    
    def remove_time_slot(self, timeslot):
        """
        Removes timeslot from the current timeslot
        """
        print("remove time slot")
        print(self)
        print(timeslot)
        if timeslot.is_contained_in(self) and self.is_contained_in(timeslot):
            return []
        elif timeslot.is_contained_in(self):
            if self.start_time != timeslot.start_time:
                left_timeslot = TimeSlot(self.start_time, timeslot.start_time)
            else:
                left_timeslot = None
            if timeslot.end_time != self.end_time:
                right_timeslot = TimeSlot(timeslot.end_time, self.end_time)
            else:
                right_timeslot = None
            if left_timeslot == None and right_timeslot != None:
                return [right_timeslot]
            elif left_timeslot != None and right_timeslot == None:
                return [left_timeslot]
            else:
                return [left_timeslot, right_timeslot]
        # what if self is contained in timeslot? shouldn't happen based on our code

    
    def __str__(self):
        return str(self.start_time) + "-" + str(self.end_time)

    def __repr__(self):
        return str(self.start_time) + "-" + str(self.end_time)
    