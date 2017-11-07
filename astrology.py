astro_dict = {
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
    'sagittarius' : ['nov22 - dec21', 1100],
    'capricorn' : ['dec22 - jan19', 1200]
                        }
char_astro = {
    'daring' : ['aries', 1],
    'twofaced' : ['gemini', 2],
    'charming' : ['libra', 3],
    'loving' : ['scorpio', 4],
    'enthusiastic' : ['sagittarius', 5],
    'wise' : ['capricorn', 6],
    'adventurous' : ['aquarius', 7],
    'fierce' : ['virgo', 8],
    'sensitive' : ['pisces', 9],
    'protective' : ['leo', 10],
    'emotional' : ['cancer', 11],
    'strong' : ['taurus', 12]
    }

def searchAstro(peopleAstro):
    try:
        astroInfo = astro_dict[peopleAstro]
        print 'astrology sign: ' + astroInfo[0]
    except:
        print "no info found"

def searchChar(peopleChar):
    try:
        charInfo = char_astro[peopleChar]
        print 'you are most like: ' + charInfo[0]
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
        peopleChar = raw_input('which characteristic do you think suits you most: daring, twofaced, charming,    loving, wise, enthusiastic, adventurous, sensitive, fierce, protective, emotional, or strong?').lower()
        searchChar(peopleChar)
    else:
        print "uh"
