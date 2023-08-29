'''
Version 1

Takes a list of Cookbooks and return a dictionary

Unfortunately, while this tells me what collections to expect, it doesn't tell me
how to use the collection at all.
'''
def create_author_count_mapping(cookbooks: list) -> dict:
    counter = defaultdict(lambda: 0)

    for book in cookbooks:
        counter[book.author] += 1

    return counter


'''
Version 2

Takes a list of Cookbooks and return a dictionary

The cookbooks list contains Cookbook objects, and the return value of the function
is returning a dictionary mapping strings (keys) to integers (values).
'''

AuthorToCountMapping = dict[str, int]
def create_author_count_mapping(cookbooks: list[Cookbook]) -> AuthorToCountMapping:
    counter = defaultdict(lambda: 0)

    for book in cookbooks:
        counter[book.author] += 1

    return counter