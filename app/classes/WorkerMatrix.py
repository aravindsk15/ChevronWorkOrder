from app.app import app

class WorkerMatrix:
    '''
    Matrix consisting of rows representing workers' name, ID, qualifications, and 
    '''
    def __init__(self, matrix):
        self.matrix = matrix

    def add_worker(self, worker_data):
        self.matrix.append()