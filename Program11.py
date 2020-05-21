#***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program 11
#
#  File Name:         Program11.py
# 
#  Description:       This program contains a list of the World Series’ winning teams
#                     from 1903 through 2019 and lets the user select a year
#
#***************************************************************


#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************


def main():
    developerInfo()
    year_dict, teams = Teams()
    showResults(year_dict,teams)

    # End of main


#***************************************************************
#
#  Function:     Teams
# 
#  Description:  Opens and reads a file of team names and then
#                converts the information.
#
#  Parameters:   None
#
#  Returns:      year_dict, TeamT 
#
#***************************************************************   
    
    
def Teams():
    TeamFile = open('Program11.txt', 'r')
    
    YearList = []
    TeamList = []
    year_dict = {}
    count_dict = {} 
    
    Winners = TeamFile.readline()
    while Winners != '':
        Winners = Winners.rstrip('\n')
        TeamList.append(Winners)
        Winners = TeamFile.readline()
    TeamFile.close()
    
    TeamT = tuple(TeamList)
    for num in range(1903, 2020):
        YearList.append(num)
    del YearList[1]
    del YearList[90]
    YearT = tuple(YearList)

    
    for index, value in enumerate(YearList):
        year_dict[value] = TeamT[index]

    return year_dict, TeamT

    # End of Teams
    

#***************************************************************
#
#  Function:     showResults
# 
#  Description:  Shows the results based on what year the user
#                chooses from the choices of years.
#
#  Parameters:   year_dict, teams
#
#  Returns:      Nothing 
#
#***************************************************************  
    
        
def showResults(year_dict,teams):
    count_dict = {}
    print('Welcome back to your World Series Program')
    print()
    year = int(input('Enter a year in the range 1903-2019 to see who won: '))
    print()
    while year != 0:
        if year == 1904 or year == 1994:
            print("The world series wasn't played in the year", year)
        elif year < 1903 or year > 2019:
            print('The data for the year', year, \
                  'is not included in our database.')
        else:
            total = 0
            winner = year_dict[year]
            for win in range(len(teams)):
                if teams[win] == winner:
                    total += 1
        count_dict = {winner : total}
        wins = count_dict[winner]
        print()
        print('The team that won the world series in ', \
              year, ' is the ', winner, '.', sep='')
        print('They have won the world series', wins, 'times.')
        print()
        print('Would you like to enter another year?') 
        print('Enter another year or enter 0 to exit the program')
        print()
        year = int(input('Enter a year in the range 1903-2019 to see who won: '))
        if year == 0:
            print('Goodbye, thank you for using the program!')
                   
    # End of showResults
    

#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Program:  Eleven')
    print()
    # End of the developerInfo function

# Call the main function.
main()

