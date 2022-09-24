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

    def __repr__(self):
        return "Job Name: " + self.work_desc + ", Time: " + str(self.time_slot.start_time) + "-" + str(self.time_slot.end_time)
        #return "Work Description: " + self.work_desc + ", Time: " + str(self.time_slot.start_time) + "-" + str(self.time_slot.end_time) + ", Qualifications" + str(self.quals_req)
    
    def fits_availability(self, worker):
        """
        Checks if the time slot of the worker is contained in the worker's availability.
        """
        suited = False
        for time_slot in worker.time_avail:
            if self.time_slot.is_contained_in(time_slot):
                suited = True
                break
        return suited
                    
        
        
    

