class Worker:
    '''
    Class representing a worker's data
    '''
    def __init__(self, name, worker_id, quals, time_avail, office_loc):
        '''
        worker's name -> str
        worker's id -> int
        qualifications -> dict that maps skills (str) to years (exp)
        time_avail -> list of TimeSlots
        office-location -> coordinates (might be a class, idk)
        '''
        self.name = name
        self.id = worker_id
        self.quals = quals
        self.time_avail = time_avail
        self.office_loc = office_loc
    
    def get_time_avail(self):
        return self.time_avail

    def get_quals(self):
        return self.get_quals
