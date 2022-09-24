from TimeSlot import TimeSlot

class WorkOrder:
    '''
    Class for a work order
    qualsreq = dictionary mapping from qualifications required to required amount of experience
    priority = 0, 1, 2 representing priority
    '''
    
    def __init__(self, work_desc, start_time, end_time, quals_req):
        self.quals_req = quals_req
        self.work_desc = work_desc
        self.time_slot = TimeSlot(start_time, end_time)

    def __str__(self):
        return "Name: " + self.name + ", Work Description: " + self.work_desc + ", Time: " + self.start_time + "-" + self.end_time + ", Qualifications" + self.quals_req
    
    def fits_availability(self, worker):
        """
        Checks if the time slot of the worker is contianed in the worker's availability.
        """
        suited = False
        for time_slot in worker.time_avail:
            if self.time_slot.is_contained_in(time_slot):
                suited = True
                break
        return suited
                    
        
        
    

