class Task:
    def __init__(self, title, description, priority, deadline):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def to_dict(self): # Convert task to dictionary for saving
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "deadline": self.deadline
        }
    
    def __str__(self): # String representation for easy viewing
        return f"Title: {self.title}, \nDescription: {self.description}, \nPriority: {self.priority}, Deadline: {self.deadline}"