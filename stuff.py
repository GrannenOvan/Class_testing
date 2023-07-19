"""Hello"""

class StuffClass:
    """Class for showing how classes works"""

    def  __init__(self, value:int=0) -> None:
        print(f"Init of stuff. Count set to {value}")
        self._count = value

    def update(self):
        """Update counter value"""
        self._count += 1
        self.show_count()

    def show_count(self):
        """Print count value"""
        print(f'count is {self._count}')

    @property
    def count(self):
        """Get count value"""
        return self._count
    
    @count.setter
    def count(self, value) -> None:
        """Set count value"""
        self._count = value
