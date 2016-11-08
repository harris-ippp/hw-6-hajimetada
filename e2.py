import requests

# Repeat each line in ELECTION_ID.
for line in open("ELECTION_ID"):
    # Disconnect id and year.
    id = str(line.split(" ")[1].replace("\n",""))
    year = str(line.split(" ")[0])
    # Put separated id in URL.
    addr = "http://"+"historical.elections.virginia.gov/elections/download/"+\
    id+"/precincts_include:0/"
    # Retrieve csv.
    resp = requests.get(addr)
    # Create appropriate file name.
    file_name = year +".csv"
    # Write out csv file.
    with open(file_name, "w") as out:
        out.write(resp.text)
