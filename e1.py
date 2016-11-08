# Import necessary stuff.
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

addr = "http://historical.elections.virginia.gov/elections/search/year_from:\
1924/year_to:2015/office_id:1/stage:General"
resp = requests.get(addr)
soup = bs(resp.content, "html.parser")

# Extract the years of presidential election from HTML and create a list of them.
year = []
for election in soup.find_all("td", "year first"):
    year.append(int(election.contents[0]))

# Extract the id of presidential elections from HTML and create a list of them.
id = []
for election in soup.find_all("tr", "election_item"):
    id.append(int(election.get("id").split("-")[2]))

# Merge each row of these two lists, print them,
# and make an output titled "ELECTION_ID".
with open("ELECTION_ID", "w") as output:
    for i in range(len(year)):
        s = str(year[i]) + " " + str(id[i]) + "\n"
        print(s)
        output.write(s)
    output.close()
