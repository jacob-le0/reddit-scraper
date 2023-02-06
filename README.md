The goal for this project:
    Search through the first 100 hot posts in the subreddit r/worldcup, and count how many times a post mentions a player or country.

The requests library was used to extract the specific data source from the subreddit. This subreddit is very active due to the World Cup taking place,
so the information extracted from this subreddit is relevant to current events today.

The JSON file that came with the link for this subreddit provided the textual information of the titles (line 26) and body (line 28) of each post. These two elements were required to obtain my goal.
I created a dictionary of a list of names (line 22) that I would search for (the most popular player of each semifinalist team in the world cup), and value of 0 for each to initiate a counter.
The for loop (line 25) iterates through the title and body text of each post, numbered 0-99 in JSON. The name_counter function is called.
The name_counter function (line 38) looks for any of the keys from the dictionary in each post. If a key is found, the value of that key is incremented by 1.
To avoid capitalization/matching issues, I converted all the text to lowercase, and matched the text with the dictionary, also lowercased.

After iteration of the first 100 posts, the dictionary with its updated values is returned and inputted into the load_reddit function (line 48).
The load_reddit function takes in the dictionary and populates a csv file with the contents, formatting the keys and its corresponding values per line.

While this project was specifically for r/worldcup, any subreddit can be inputted in line 62 and searched through, but the same keys on line 22 will be searched.

Extract, Transform and Load functions are all called in lines 62, 63, and 64 respectively.
The extract function is called with the name of the subreddit (as it would be in the url) as a parameter.
The transform function is called with the extracted raw data as its parameter, equated to a variable.
The load function is called with two parameters: the variable equated to the transform function, and the name for the csv file.