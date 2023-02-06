import requests
from unidecode import unidecode

"""Notes/Plans: Populate an empty dictionary with user input
Populate url with subreddit of user's choice
Create a visual graph (matplotlib) representing the data pulled from reddit"""

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

# Transform 
def transform_reddit(raw_data):
    """Raw data transformed into informational data"""

    # Create a dictionary of names to search for and their counters
    d = {"messi":0, "modric":0, "mbappe":0, "hakimi":0, "argentina":0, "croatia":0, "france":0, "morocco":0}

    # Iterate through the title and body text of the first 100 posts in r/worldcup and search for the keys in dictionary
    for i in range (100):
        title = raw_data['data']['children'][i]['data']['title']

        bodytext = raw_data['data']['children'][i]['data']['selftext']
        
        key = name_counter(title, bodytext, d.keys())

        # Adds one to the counter if the corresponding key is found
        if key in d:
            d[key]+=1
    
    return d

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


status, raw_data = extract_reddit('worldcup')
name_data = transform_reddit(raw_data)
load_reddit(name_data, 'name_mentions')