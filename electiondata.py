class ElectionResults:
  
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    self.file = open(self.filename, 'r')
    self.all_lines = self.file.readlines()

  def states(self):
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      all_names.append(columns[1])
    return all_names

  def state_count(self):
    return len(self.all_lines)

  def get_obama_votes(self):
    all_obama_votes = []
    for line in self.all_lines:
        columns = line.split(",")
        all_obama_votes.append(columns[3])
    return all_obama_votes

  def get_romney_votes(self):
    all_romney_votes = []
    for line in self.all_lines:
        columns = line.split(",")
        all_romney_votes.append(columns[5])
    return all_romney_votes
