from WorkOrder import WorkOrder

class Worker:
    '''
    Class representing a worker's data
    '''
    def __init__(self, name, worker_id, quals, time_avail):
        
        '''
        worker's name -> str
        worker's id -> int
        qualifications -> dictionary mapping from strings to years of experience
        time_avail -> list of TimeSlots
        '''
        self.name = name
        self.worker_id = worker_id
        self.quals = quals
        self.time_avail = time_avail

    def __str__(self):
        return "Name: " + self.name + "Worker ID" + str(self.worker_id) + "Qualifications" + str(self.quals) + "Time Availability" + str(self.time_avail)
    
    def get_time_avail(self):
        return str(self.time_avail)

    def get_quals(self):
        return self.get_quals

    def is_qual(self, job):
        '''
        Job is a WorkOrder 

        Returns boolean value describing 
        '''
        # print("here?")
        for req_qual in job.quals_req:
            if req_qual not in self.quals.keys():
                return False
            elif job.quals_req[req_qual] >= self.quals[req_qual]:
                return False
        return True

