
# The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Retrieves all restaurants matching specific price tag (e.g. '$') from 'price' argument
    names_matching_price = price_to_names[price]

    # Get restaurant names (from above price tag) that also belong to cuisine in cuisines_list 
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Retrieve ratings from restaurants in names_final and return sorted output by ratings
    result = build_rating_list(name_to_rating, names_final)

    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    # For each restaurant in names_final, append corresponding rating (sorted) first to result
    result = list()
    for restaurant in names_final:
        result.append([name_to_rating[restaurant],restaurant])
    return sorted(result,reverse=True)



def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    # For each cuisine we want, check if the names within price range belong to that cuisine
    result = list()
    # For each name that is in cuisines_list, we check if restaurant name is in there and return it
    for cuisine in cuisines_list:
        for name in names_matching_price:
            if name in cuisine_to_names[cuisine] and name not in result:
                result.append(name)
    return result

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}
    with open(file) as f:
        i = 0
        # Store all lines (without \n) to lines in a list of words
        lines = f.read().splitlines()
        while i < len(lines):
            # we know the following:
            # line[i] = restaurant name, line[i+1] = rating
            # line[i+2] = price, line[i+3] = cuisine
            name_to_rating[lines[i]] = lines[i+1]
            # match price to name
            if lines[i+2] not in price_to_names.keys():
                price_to_names[lines[i+2]] = [lines[i]]
            else:
                price_to_names[lines[i+2]].append(lines[i])
            # add list of restaurants per cuisine
            cuisines = lines[i+3].split(',')
            for cuisine in cuisines:
                if cuisine not in cuisine_to_names.keys():
                    cuisine_to_names[cuisine] = [lines[i]]
                else:
                    cuisine_to_names[cuisine].append(lines[i])
            # while loop is incremented by 5 as name is in position 0, rating 1, price 2, cuisine 3, blank line 4 
            i += 5
    return name_to_rating, price_to_names, cuisine_to_names