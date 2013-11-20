# Verify that we can open and read the election results CSV correctly
# Showing a "test-driven" style
from electiondata import ElectionResults
import unittest
class ElectionResultsTest(unittest.TestCase):
    def setUp(self):
        self.results = ElectionResults('election_results_test_file.csv')
    def testLoad(self):
        self.results.load()
        assert self.results!=None
        assert self.results.file!=None
    def testStateCount(self):
        self.results.load()
        state_count = self.results.state_count()
        assert state_count==3
    def testStates(self):
        self.results.load()
        names = self.results.states()
        assert len(names)==3
        assert names[1]=='Alaska'
        assert names[2]=='Alabama'
    def testObama(self):
        self.results.load()
        obamavotes = self.results.get_obama_votes()
        assert len(obamavotes)==3
    def testRomney(self):
        self.results.load()
        romneyvotes = self.results.get_romney_votes()
        assert len(romneyvotes)==3
# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
