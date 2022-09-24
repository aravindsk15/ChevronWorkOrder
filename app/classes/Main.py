from WorkOrder import WorkOrder
from TimeSlot import TimeSlot
from Worker import Worker
from collections import defaultdict
import random

# work_orders_to_worker = defaultdict(lambda: [])
# For each worker, assign possible work orders
workers_to_work_order = defaultdict(lambda: [])

work_orders = []
workers = []
incompatible_jobs = set()
assigned_jobs = set()
unassigned_jobs = set()
work_order_to_worker = defaultdict(int)

work_order1 = WorkOrder("Job 1", 900, 1000, {'BSCS': 3})
work_order2 = WorkOrder("Job 2", 1030, 1100, {'BACS': 2})
work_order3 = WorkOrder("Job 3", 1000, 1030, {'BSCS': 2})
work_order4 = WorkOrder("Job 4", 1000, 1100, {'Architecture': 1})
work_order5 = WorkOrder("Job 5", 1500, 1600, {'Michael is cool': 50})
work_order6 = WorkOrder("Job 6", 900, 1000, {'BSCS': 3})

work_orders.append(work_order1)
work_orders.append(work_order2)
work_orders.append(work_order3)
work_orders.append(work_order4)
work_orders.append(work_order5)
work_orders.append(work_order6)

worker1 = Worker("Bob", 45050040, {'BSCS': 4}, [TimeSlot(900, 1500)])
worker2 = Worker("Joe", 45050041, {'BACS': 2}, [TimeSlot(1030, 1100)])
worker3 = Worker("Billy", 123123, {'Architecture': 2}, [TimeSlot(900, 1200), TimeSlot(1300, 1700)])


workers.append(worker1)
workers.append(worker2)
workers.append(worker3)

for work_order in work_orders:
    #print("work order", work_order)
    work_order_assigned = False
    for worker in workers:
        #determines if workers are compatible to job with regards to qualifications and time
        #availability
        if worker.is_qual(work_order) and work_order.fits_availability(worker):
            workers_to_work_order[worker].append(work_order)
            # make more efficient?
            assigned_jobs.add(work_order)
            work_order_assigned = True
    if work_order_assigned == False:
        incompatible_jobs.add(work_order)
        # print("INCOMPATIBLE JOBS", incompatible_jobs)

# print(workers_to_work_order)

#sort workers by flexibility
work_flex_sort = sorted(workers_to_work_order.items(), key=lambda x: len(x[1]))

# print(work_flex_sort)

#flex_sort maps workers to list of possible work orders
#assign workers to work orders
for worker_and_workorder in work_flex_sort:
    # print("worker and work order", worker_and_workorder)
    current_worker = worker_and_workorder[0]
    current_work_orders = worker_and_workorder[1]
    sorted_work_order_list = sorted(workers_to_work_order[current_worker], key = lambda x: x.time_slot.end_time)
    for least_work_order in sorted_work_order_list:
        # print("assigned jobs set:", assigned_jobs)
        if least_work_order.fits_availability(current_worker) and least_work_order in assigned_jobs:

            # print("this should be assigned", least_work_order)
            #assigns work order -> worker
            work_order_to_worker[least_work_order] = current_worker

            #updates availability of worker
            current_worker.update_availability(least_work_order)

            #schedules job
            assigned_jobs.remove(least_work_order)

for an_unassigned_job in assigned_jobs:
    unassigned_jobs.add(an_unassigned_job)

#print("unassigned jobs", unassigned_jobs)
#print("incompatible jobs", incompatible_jobs)

print("final assignments", work_order_to_worker)