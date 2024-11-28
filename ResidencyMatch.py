'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

Jesse Melanson, Makenna Worley
We didn't finish in class together so our code will have a similar structure but not the same functions line per line

'''

import sys
import csv

class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

            # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 
    
            
    # print out the stable match
    def reportMatches(self):
        print(self.matches)
            
    # follow the chart described in the lab to find the stable match
    def runMatch(self):
        '''
        It is suggested you use the debugger or similar output statements
        to determine what the contents of the data structures are
        '''

        matchedPairs = {}

        while None in self.matches.values():
            r = self.unmatchedResidents[0]
            r_choice = (self.residentsMappings[r])[0] #not being incremented if not successful

            if r_choice in self.unmatchedHospitals:
                self.unmatchedResidents.remove(r)
                self.unmatchedHospitals.remove(r_choice)
                self.matches.update({ r : r_choice })
                matchedPairs.update({ r_choice : r })
            else:
                r2 = matchedPairs.get(r_choice)
                rankings = self.hospitalsMappings.get(r_choice)

                if rankings.index(r) < rankings.index(r2):
                    self.unmatchedResidents.remove(r)
                    self.unmatchedResidents.append(r2)
                    self.matches.update({ r : r_choice })
                    matchedPairs.update({ r_choice : r })
                    self.matches.update({ r2 : None })
                    self.residentsMappings[r2].pop(0)
                else:
                    self.residentsMappings[r].pop(0) #remove that hospital from that resident's ranking




if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()



