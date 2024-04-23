import psutil as pt

class CpuBar():
    """ Read CPU and RAM usage"""

    def __init__(self):
        """The number of phisical and logical CPU cores. """
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    def cpu_percent_return(self):
        """Reads the load tye CPU cores."""

        return pt.cpu_percent(percpu=True)

    def cpu_one_return(self):
        """Read the total CPU usage."""
        return pt.cpu_percent()

    def ram_usage(self):
        """Reads the load of RAM"""
        return pt.virtual_memory()

    def count_temperatures(self):
        """temperatures"""
        return pt.sensors_temperatures()