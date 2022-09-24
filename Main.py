from WorkOrder import WorkOrder
from TimeSlot import TimeSlot
from Worker import Worker
from collections import defaultdict

# Assigns a WorkOrder to a Worker
work_dict = defaultdict(lambda: [])
work_orders = []
workers = []

work_order1 = WorkOrder("Job 1", 900, 1000)
work_order2 = WorkOrder("Job 2", 1030, 1100)
work_orders.append(work_order1)
work_orders.append(work_order2)
worker1 = Worker("Bob", 45050040, {'BSCS': 4}, [TimeSlot(900, 1000)], 'Houston')
worker2 = Worker("Joe", 45050041, {'BACS': 4}, [TimeSlot(1030, 1100)], 'New York')
workers.append(worker1)
workers.append(worker2)

for work_order in work_orders:
    for worker in workers:
        if work_order.is_suited_worker(worker):
            work_dict[work_order].append(worker)

print(work_dict)