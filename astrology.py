epic_programmer_dict = {
    'aquarius' : ['jan20 - feb18', 111],
    'pisces' : ['feb19 - march20', 222],
    'aries' : ['march21 - april19', 333],
    'taurus' : ['april20 - may20', 444],
    'gemini' : ['may21 - june20', 555],
    'cancer' : ['june21 - july22', 666],
    'leo' : ['july23 - aug22', 777],
    'virgo' : ['aug23 - sept22', 888],
    'libra' : ['sept23 - oct22', 999],
    'scorpio' : ['oct23 - nov21', 1000],
    'saggitarius' : ['nov22 - dec21', 1100],
    'capricorn' : ['dec22 - jan19', 1200]
                        }
def searchAstro(peopleAstro):
    try:
        astroInfo = epic_programmer_dict[peopleAstro]
        print 'astrology sign: ' + astroInfo[0]
    except:
        print "no info found"
    
userWantsMore = True
while userWantsMore == True:
    peopleAstro = raw_input('Please enter a sign: ').lower()
    searchAstro(peopleAstro)
    userWantsMore = False
    searchAgain = raw_input('search again? y/n')
    if searchAgain == 'y':
        userWantsMore = True
    elif searchAgain == 'n':
        userWantsMore = False
    else:
        print "uh"
