import emoji
print('''               ***********                  ***********
            *****************            *****************
         *********************        *********************
        ***********************      ***********************
        ************************    ************************
        *************************  *************************
        **************************************************
          ************************************************
            ********************************************
              ****************************************
                 **********************************
                   ******************************
                      ************************
                        ********************
                           **************
                             **********
                               ******
                                **                      LOVE ISLAND''')

print('--------------------------------------------------------------------------------------------------------')
print("WELCOME TO LOVE ISLAND!\nOr better said, a version of Love Island by someone who has never watched the show....")

option = input(emoji.emojize('ANYWAY, ready to meet your soulmate? :two_hearts: (YES/NO)\n')).lower()
if option == 'yes':
    print(emoji.emojize('You must be quite desperate, aren\'t you? It\'s ok hun, we can help you.\nThere are two :sparkles:FABULOUS:sparkles: bachelors ready to make your heart swoon OH YES THEY ARE.\nBut the twist is... YOU\'LL HAVE TO CHOOSE BEFORE GETTING TO SEE THEM. We are so evil YES WE ARE :smiling_face_with_horns:.'))
    print('')
    bachelor = int(input('Ok, enough blah blah and more pew pew, who are you choosing? Option 1 or Option 2? (1/2)\n'))
    if bachelor == 1:
        print('Get ready to meet TROY MCCLURE!\nYou may remember him from The Simpsons and a bunch of other stuff\nthat he will make sure to let you know if you go on a date with him *wink wink*.')
        date1 = input('So what do you say, date yes, date no (YES/NO)\n').lower()
        if date1 == 'yes':
            print('Oops, turns out TROY MCCLURE had some scheduling conflict and couldn\'t come.\nDON\'T LOOK AT US THAT WAY, it\'s not our fault (but our camera guy is single and ready to mingle if you are interested *wink wink*).')
            quit
        else:
            print('Nah, it\'s ok, even better, because we didn\'t have the budget for Troy McClure either way... so bye bye.')
            quit
    elif bachelor == 2:
        print(emoji.emojize('Get ready to meet GORGONZOLA! Gorgonzola is the goat :goat: no cap :billed_cap:. Period.\nI don\'t even know what that means but my 13-year old cousin sure says it a lot and it seemed fitting.'))
        date2 = input('Ready to give Gorgonzola a chance? (YES/NO)\n').lower()
        if date2 == 'yes':
            print('\x1B[3mGorgonzola takes you foraging.\x1B[0m')
            final = input('Ok enough foraging, we all know how these things end... one thing leads to another and...\nANYWAY. What\'s your final decision? (YES/NO)\n').lower()
            if final == 'yes':
                final1 = input('Are you sure you want to date a goat? (YES/NO)\n').lower()
                if final1 == 'yes':
                    final2 = input('Like 100% sure? (YES/NO)\n').lower()
                    if final2 == 'yes':
                        print('Now that I remember, my cousin is also married to a goat and he\'s happy, so congratulations I guess?')
                        print('')
                        print(emoji.emojize("THE END :two_hearts:"))
                        quit
                    else:
                        print('Phew, thank Goodness.\nWell, that\'s all for today, thank you for watching LOVE ISLAND!')
                else:
                    print('I know foraging can be pretty intense, but let\'ts face it, Gorgonzola is a goat.\nWell, that\'s all for today, thank you for watching LOVE ISLAND!')
            else:
                print('It wasn\'t meant to be, I wonder why.\nWell, that\'s all for today, thank you for watching LOVE ISLAND!')
        else:
            print('Yes, I know you are angry we brought a goat, BUT TRY TO HIRE CONTESTANTS ON A $8.30 BUDGET.')
else:
    print('C\'mon, don\'t you wanna meet your future chikibaby?')
    print('It\'s ok. Enjoy being SINGLE and LONELY and SAD and MISERABLE.')



