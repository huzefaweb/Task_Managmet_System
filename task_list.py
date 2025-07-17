class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self.tasks):
            task = self.tasks[self._index]
            self._index += 1
            return task
        raise StopIteration
    
    def add(self, task):
        self.tasks.append(task)
    
    def remove(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Task index out of range")
    
    def sort(self, key=None):
        self.tasks.sort(key=key)
    
    def all(self):
        return self.tasks
    
    def filter(self, condition):
        return [task for task in self.tasks if condition(task)]