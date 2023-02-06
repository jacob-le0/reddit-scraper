def population():
    d = {}
    populate = ""
    while populate != "/":
        populate = input("Type a keyword you would like to search in the subreddit.\nType '/' when done, 'clear' to empty list, 'list' to view contents: ")
        if populate == "clear":
            d.clear()
        elif populate == "list":
            print(d)
        else:
            d[populate] = 0
    d.popitem()
    return d

print(population())