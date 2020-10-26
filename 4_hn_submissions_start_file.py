from operator import itemgetter

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.



    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    
    
    # Build a dictionary for each article.
    submission_dict = {
        
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        
    }
    
    


