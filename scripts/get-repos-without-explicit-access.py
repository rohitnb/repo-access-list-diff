fields = "repositoryToBeAdded"

def read_csv(csvFilePath,the_list):
    csvHandle = open(csvFilePath,"r")
    count=1
    for line in csvHandle:
        if count > 1:
            temp = line.split(",")[0]
            name = temp.replace('"','')
            the_list.append(name)
        count=count+1
    return the_list

the_cli_list = []
the_cli_set = set(read_csv("all-repos.csv", the_cli_list))

the_api_list = []
the_api_set = set(read_csv("explicit-access-repos.csv", the_api_list))

the_diff = the_cli_set - the_api_set

filename = "to-be-added-manually.csv"
with open(filename, 'w') as csvfile:
    csvfile.write(fields+"\n")
    for line in the_diff:
        csvfile.write(line+"\n")
