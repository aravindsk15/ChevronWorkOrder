from WorkOrder import WorkOrder

import copy

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

    def __repr__(self):
        #return "Name: " + self.name + ", Worker ID: " + str(self.worker_id) + ", Qualifications" + str(self.quals) + ", Time Availability" + str(self.time_avail)
        return "Name: " + self.name + ", Available:" + str(self.time_avail)
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
            # check the time
            elif job.quals_req[req_qual] > self.quals[req_qual]:
                return False
        return True
    
    def update_availability(self, job):
        for time_slot in self.time_avail:
            if job.time_slot.is_contained_in(time_slot): 
                #the list of new slots after spilt
                new_time_slots = time_slot.remove_time_slot(job.time_slot)
                print("split time slots", new_time_slots)
                copy_slots = copy.copy(self.time_avail)
                copy_slots.remove(time_slot)
                print("time slot removed", job.time_slot)
                print("curr slots", self.time_avail)
                print("copy slots", copy_slots)
                index1 = self.time_avail.index(time_slot)
                for new_slot in new_time_slots:
                    copy_slots.insert(index1, new_slot)
                    index1 += 1
                print("new slots", copy_slots)
                self.time_avail = copy_slots
                break




