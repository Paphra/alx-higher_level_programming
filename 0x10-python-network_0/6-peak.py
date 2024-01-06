"""6-peak module

For fnding the peak of the list of integers
"""

def find_peak(list_of_integers):
    """find_peak function

    For finding the peak
    """

    if len(list_of_integers) == 0:
        return None
    s_list = sorted(list_of_integers)
    return s_list[-1]
