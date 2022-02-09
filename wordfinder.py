"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
   """a class that will find random words in a document when an instance of the class is created
   >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'"""

    def __init__(self, path):
        """Reads through the document with the random words and states the total number of words read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parses the document into a list of words we can see and work with in Python, using strip() to take the new line markers out"""
        return [w.strip() for w in dict_file]

    def random(self):
        """returns a random word from the document"""
        return random.choice(self.words)


# /Desktop/springboard/python-oo-practice/words.txt

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
