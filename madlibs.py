#!/usr/bin/env python3

"""
File: madlibs.py
Name:

A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

def main():
    
    name1 = input("i need a name")
    name2 = input("i need a second name")
    name3 = input("i need a third name")
    pronoun1 = input("i need a pronoun for the first name(he/she/it)")
    pronoun2 = input("i need a pronoun for the first name(him/her/it)")
    pronoun3 = input("i need a pronoun for the second name(he/she/it)")
    pronoun4 = input("i need a pronoun for the second name(him/her/it)")
    pronoun5 = input("i need a pronoun for the third name(him/her/it)")
    pronoun6 = input("i need a pronoun for the third name(him/her/it)")
    iteam1 = input("i need a iteam(be sure to add, a or an, if nessacery)")
    iteam2 = input("i need another iteam(be sure to add, a or an, if nessacery)")
    verb1 = input("i need a verb")
    
    print("this is a story about " + name1 + ", lord of thieves")
    print(name1 + " stole " + iteam1 + ", an officer took notice notice, so " + name1 + " " + verb1 + " ran away")
    print("eventually loosing the angrey horde of cops and cavilians, " + name1 + " made it back to his hideout where " + name2 + " and " + name3 + " also are")
    print(name2 + ": hey, was the mission a succees.")
    print(name1 + ": of coarse, what kind of thief do ya take me for!")
    print(name2 + ": A BAD ONE, dont you remember prauge where we all almost went to prison!")
    print(name3 + ": hey, hey, hey, now, we dont need to start fighting, " + name1 + " got the job done, thats all that matters")
    print(name1 + ": well, what now?")
    print(name3 + ": i dont know, maybe we should just sleep for tonight")
    print("everyone agreess sleeping would be a good idea and do so")
    print("___________________________________________________________________THE NEXT DAY___________________________________________________________________")

if __name__ == "__main__":
    main()
