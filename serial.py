"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """This assigns a start value when an instance of SerialGenerator is created, and 100 is the starting point unless changed by user. It runs any time an instance is instantiated. Start and next are the same before any numbers are generated because the next number generated will be equal to start."""

        self.start = self.next = start

    def __repr__(self):
        """This defines how the output looks when printing out an instance of SerialGenerator in the Python shell"""

        return f"<SerialGenerator start = {self.start} and next = {self.next}>"

    def generate(self):
        """This generates the next serial number in the sequence, i.e. one number greater than the last serial number."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Calling this function resets the generator back to the first number and the whole process starts over."""

        self.next = self.start

