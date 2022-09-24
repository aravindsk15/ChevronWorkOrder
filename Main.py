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

work_order1 = WorkOrder("Job 1", 900, 1000, {'BSCS': 3})
work_order2 = WorkOrder("Job 2", 1030, 1100, {'BACS': 2})
work_orders.append(work_order1)
work_orders.append(work_order2)
worker1 = Worker("Bob", 45050040, {'BSCS': 4}, [TimeSlot(900, 1000)])
worker2 = Worker("Joe", 45050041, {'BACS': 2}, [TimeSlot(1030, 1100)])
workers.append(worker1)
workers.append(worker2)

for work_order in work_orders:
    work_order_assigned = False
    random_worker_idx = list(range(len(workers)))
    for rand_worker_idx in random_worker_idx:
        worker = workers[rand_worker_idx]
        #determines if workers are compatible to job with regards to qualifications and time
        #availability
        if worker.is_qual(work_order) and work_order.fits_availability(worker):
            workers_to_work_order[worker].append(work_order)
            # make more efficient?
            assigned_jobs.add(work_order)
            work_order_assigned = True
    if work_order_assigned == False:
        incompatible_jobs.add(work_order)

#sort workers by flexibility
work_flex_sort = sorted(workers_to_work_order.items(), key=lambda x: len(x[1]))

#assign workers to work orders
for worker_and_workorder in work_flex_sort:
    worker = worker_and_workorder[0]
    work_order = worker_and_workorder[1]

    #worker.assign(jobs)

    print(worker)
    print(work_order)