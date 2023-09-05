# Collections
# Version 1
def create_author_count_mapping(cookbooks: list[Cookbook]):
    counter = {}
    for cookbook in cookbooks:
    if cookbook.author not in counter:
                counter[cookbook.author] = 0
            counter[cookbook.author] += 1
    return counter

# defaultdict
# Version 2
from collections import defaultdict
def create_author_count_mapping(cookbooks: List[Cookbook]):
    counter = defaultdict(lambda: 0)
    for cookbook in cookbooks:
        counter[cookbook.author] += 1
    return counter


# Counter
# Version 3
from collections import Counter
def create_author_count_mapping(cookbooks: List[Cookbook]):
    return Counter(book.author for book in cookbooks)