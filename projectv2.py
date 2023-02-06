import requests
from unidecode import unidecode
import matplotlib.pyplot as plt
"""Notes/Plans: 
*Populate an empty dictionary with user input
*Populate url with subreddit of user's choice
*Input the generated dictionary into transform_reddit
*Create a visual graph (matplotlib) representing the data pulled from reddit
Figure out a way for the counter to continue counting other keys for more accurate data
    i.e. If a post includes more than one key, it will only count the earlier key in the dictionary, even though another key is mentioned"""

#Extract
def extract_reddit(subreddit):
    """Return data from a subreddit"""
    # Input pointer to raw data source
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    
    # Define a unique user agent value
    head = {'user-agent': 'Jacob Leo App v0.0.1'}

    r = requests.get(url, headers = head)
    raw_data = r.json()
    return r.status_code, raw_data


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

# Transform 
def transform_reddit(raw_data, user_dict):
    """Raw data transformed into informational data"""

    # Create a dictionary of names to search for and their counters
    #d = {"messi":0, "modric":0, "mbappe":0, "hakimi":0, "argentina":0, "croatia":0, "france":0, "morocco":0}

    # Iterate through the title and body text of the first 100 posts in r/worldcup and search for the keys in dictionary
    for i in range (100):
        title = raw_data['data']['children'][i]['data']['title']

        bodytext = raw_data['data']['children'][i]['data']['selftext']
        
        key = name_counter(title, bodytext, user_dict.keys())

        # Adds one to the counter if the corresponding key is found
        if key in user_dict:
            user_dict[key]+=1
    
    return user_dict

def name_counter(title, bodytext, name):
    """Returns the key found in each individual post, title and body text."""

    for i in name:
        if i in title.lower() or i in bodytext.lower():
            return i
    


#Load
def load_reddit(processed_data, filename):

    """Opens, writes and saves the dictionary keys 
    and values in proper format in a csv file"""
    
    f = open(f'{filename}.csv', 'w')
    f.write("Name, Mentions\n")

    # Prints out each key and value per new line, capitlizes key
    for i, j in processed_data.items():
        f.write(f"{i.capitalize()}, {j}\n")
    f.close()

def graph_reddit(population):
    names = list(population.keys())
    values = list(population.values())
    plt.bar(range(len(population)), values, tick_label=names)
    plt.show()

subreddit = input("Enter a subreddit you would like to scrape (omit the r/): ")
status, raw_data = extract_reddit(subreddit)
user_dict = population()
name_data = transform_reddit(raw_data, user_dict)
load_reddit(name_data, 'name_mentions')
graph_reddit(user_dict)