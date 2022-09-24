from TimeSlot import TimeSlot

class WorkOrder:
    '''
    Class for a work order
    '''
    def __init__(self, work_desc, start_time, end_time):
        self.work_desc = work_desc
        self.time_slot = TimeSlot(start_time, end_time)

    def is_suited_worker(self, worker):
        suited = False
        for time_slot in worker.time_avail:
            if self.time_slot.is_contained_in(time_slot):
                suited = True
                break
        return suited
                    
        
        
    

