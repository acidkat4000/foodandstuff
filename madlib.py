#!/usr/bin/env python3

"""
File: madlibs.py
Name:
A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

import time

def main():
    
        
    name1 = input("i need a name")
    name2 = input("i need a second name")
    name3 = input("i need a third name")
    pronoun1 = input("i need a pronoun for the first name(he/she/they)")
    pronoun2 = input("i need a pronoun for the first name(him/her/it)")
    pronoun3 = input("i need a pronoun for the second name(he/she/they)")
    pronoun4 = input("i need a pronoun for the second name(him/her/it)")
    pronoun5 = input("i need a pronoun for the third name(he/she/they)")
    pronoun6 = input("i need a pronoun for the third name(him/her/it)")
    iteam1 = input("i need a iteam(be sure to add, a or an, if nessacery)")
    verb1 = input("i need a verb")
    number1 = input("i need a number between 2 and 99")
    number2 = input("i need a number between 30 and 70")
    number3 = input("i need any number, at all")
    
    print("this is a story about " + name1 + ", lord of thieves")
    time.sleep(2)
    print(name1 + " stole " + iteam1 + ", an officer took notice notice, so " + name1 + " " + verb1 + " ran away")
    time.sleep(2)
    print("eventually loosing the angry cop " + name1 + " made it back to the safehouse")
    time.sleep(2)
    print("where his friends and fellow thieves " + name2 + " and " + name3 + " also are")
    time.sleep(2)
    print(name2 + ": hey, was the mission a succees.")
    time.sleep(2)
    print(name1 + ": of coarse, what kind of thief do ya take me for!")
    time.sleep(2)
    print(name2 + ": A BAD ONE, dont you remember prauge where we all almost went to prison!")
    time.sleep(2)
    print(name3 + ": hey, hey, hey, now, we dont need to start fighting, " + name1 + " got the job done, thats all that matters")
    time.sleep(3)
    print(name1 + ": well, what now?")
    time.sleep(2)
    print(name3 + ": i dont know, maybe we should just sleep for tonight")
    time.sleep(2)
    print("everyone agreess sleeping would be a good idea and do so")
    time.sleep(2)
    print("___________________________________THE NEXT DAY, AT THE SAFEHOUSE_________________________________________")
    time.sleep(2)
    print(name3 + ": hey, what are you doing here " + name1 + "? shouldent you be out right now, ya know? stealing?")
    time.sleep(3)
    print(name1 + ": cant, tenants are home, guess they felt like staying home today, so im stuck here")
    time.sleep(3)
    print(name2 + ": hey " + name1 + " what are you doing here?")
    time.sleep(2)
    print(name1 + ": read the text above")
    time.sleep(2)
    print(name2 + " looks at the text above")
    time.sleep(2)
    print(name2 + ": oh, darn")
    time.sleep(2)
    print(name1 + ": yea, so what do you guys wnna do today?")
    time.sleep(2)
    print(name3 + ": maybe we should buy some food so we can live?")
    time.sleep(2)
    print(name1 + ": not a bad idea, " + name2 + " go do that for us, i cant becuase im being searched for right now and " + name3 + " cant go becuase it was " + pronoun6 + " idea")
    time.sleep(4)
    print(name2 + ": im fine with going, just give me some money")
    time.sleep(2)
    print(name1 + " gives " + name2 + " money to buy food and stuff")
    time.sleep(2)
    print(name2 + ": this is " + number1 + " cents")
    time.sleep(2)
    print(name1 + ": -_-, ok fine, heres " + number2 + " bucks")
    time.sleep(2)
    print(name3 + ": ok, thanks ill probs be about " + number3 + " minutes, see ya then")
    time.sleep(2)
    print(name3 + ": bye")
    time.sleep(2)
    print(name1 + ": righty, see you then")
    time.sleep(2)
    print(name3 + " nods and leaves to get food")
    time.sleep(2)
    print()
    

if __name__ == "__main__":
    main()