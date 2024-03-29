import math
import re

from django.utils.html import strip_tags


def count_words(html_string):
    word_string = strip_tags(html_string)
    matching_list = re.findall(r'\w+', word_string)
    count = len(matching_list)
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count / 200.0)
    return int(read_time_min)
