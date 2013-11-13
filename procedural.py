# Print out all the state names from the csv
# Coded in the "procedural" style
def get_country_name_from(line):
    columns = line.split(",")
    return columns[1]
def get_obama_vote(line):
    columns = line.split(",")
    return columns[3]
def get_romney_vote(line):
    columns = line.split(",")
    return columns[5]
f = open('2012_US_election_state.csv', 'r')
print "Opened file:"
all_lines = f.readlines()
obamatotal =0
romneytotal =0
for line in all_lines[1:]:
    print "  "+get_country_name_from(line)
    obamatotal +=int(get_obama_vote(line))
    romneytotal +=int(get_romney_vote(line))
print "Totals"
print "obama:" +str(obamatotal)
print "romney:" +str(romneytotal)
