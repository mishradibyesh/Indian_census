"""
@author: Dibyesh Mishra
@date: 22-12-2021 00:32
"""
class IndianCensusException(Exception) :
    """
    custom exception
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
