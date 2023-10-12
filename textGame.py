from colorama import init
from colorama import Fore
from time import sleep

import Strings
import Utils
import Inventory

# I don't want colors to be remembered in case they are not assigned
init(autoreset=True)


# Introduce the player to the atmosphere
def do_welcome():
    # presenting the text
    print(Fore.GREEN+Strings.get("Welcome"))
    
    input("Apasă 'Enter' pentru a continua...\n") 
    # presenting the next text
    print(Fore.GREEN+Strings.get("Welcome2"))
    
    input("Apasă 'Enter' pentru a continua...\n")   
    # presenting the next text
    print(Fore.GREEN+Strings.get("Welcome3"))

    # requesting a specific answer from the player
    raspuns = Utils.inputYesNo(Fore.BLUE+"Accepți misiunea?")
    if raspuns:
        # The player has chosen to join the mission
        # You can continue the story or introduce the next stage of the game here
        print(Fore.GREEN+Strings.get("Welcome4"))
        input("Apasă 'Enter' pentru a continua...\n")
        do_start()
    else:
        # The player chose not to join the mission
        # The game closes after 10 secunde
        print(Fore.RED+"Ai decis să nu accepți misiunea. Lumea dinozaurilor este acum în pericol.")
        sleep(10)
        exit()    


def do_intro():
    # Presents available missions to the player
    print(Fore.GREEN+Strings.get("Start"))
    input("\nApasă 'Enter' pentru a continua...\n")  
    do_start()


def do_start():
    # Presents available missions to the player
    print(Fore.YELLOW+Strings.get("Start2"))

    choice = Utils.inputNumber(Fore.BLUE+"Te rog să alegi cu care misiune vrei să începi introducând numărul "
                                         "corespunzător și apoi să apeși 'Enter': ")

    if choice == 1:
        # Specific logic for the Leakage Mission
        do_mission1()
    elif choice == 2:
        # Specific logic for the Barricade Mission
        do_mission2()
    elif choice == 3:
        # Specific logic for the Guard Mission
        do_mission3()


def do_mission1():
    if Inventory.check_mission_status_for_job(1, 1):
        print(Fore.BLUE+"Ai oprit deja scurgerea vulcanului! Te rog să alegi o altă misiune.")
        input("\nApasă 'Enter' pentru a continua...\n")
        do_start()
    else:
        print(Fore.GREEN+Strings.get("Mission1Title"))
        sleep(1)  # Wait for 2 seconds
        print(Fore.GREEN+Strings.get("Mission1Text1"))
        input("\nApasă 'Enter' pentru a continua...\n")
        print(Fore.GREEN+Strings.get("Mission1Text2"))
        input("\nApasă 'Enter' pentru a continua...\n")

        do_mission1_choice()


def do_mission1_choice():
    print(Fore.YELLOW+Strings.get("Mission1Text3"))
    choice = Utils.inputNumber(Fore.BLUE+"Te rog să alegi cu care misiune vrei să începi "
                               "introducând numărul corespunzător și apoi să apeși 'Enter': ")
    if choice == 1:
        # If the user previously completed mission 1, we send them back to mission selection
        if Inventory.check_mission_status_for_job(1, 1):
            print(Fore.BLUE+"Ai mers deja in Valea Aburilor! Te rog să alegi o altă misiune.")
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission1_choice()
        else:
            print(Fore.YELLOW+Strings.get("Mission1Job1Choices"))
            choice = Utils.inputNumber("Alege un tip și apoi să apasă 'Enter': ")
            if choice == 1:
                Inventory.set_sub_mission_status(1, 1, 1)
                print(Fore.GREEN+Strings.get("Mission1Job1Choice1"))
            elif choice == 2:
                Inventory.set_sub_mission_status(1, 1, 2)
                print(Fore.GREEN+Strings.get("Mission1Job1Choice2"))
            elif choice == 3:
                Inventory.set_sub_mission_status(1, 1, 3)
                print(Fore.GREEN+Strings.get("Mission1Job1Choice3"))
            input("\nApasă 'Enter' pentru a continua...\n")
            print(Fore.GREEN+Strings.get("Mission1Job1Conclusion"))
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission1_choice()
    elif choice == 2:
        # If the user previously completed mission 2, we send them back to mission selection
        if Inventory.check_mission_status_for_job(1, 2):
            print(Fore.BLUE+"Ai fost deja prin labirint! Te rog să alegi o altă misiune.")
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission1_choice()
        else:
            print(Fore.YELLOW+Strings.get("Mission1Job2Choices"))
            choice = Utils.inputNumber("Alege un tip și apoi să apasă 'Enter': ")
            if choice == 1:
                Inventory.set_sub_mission_status(1, 2, 1)
                print(Fore.GREEN+Strings.get("Mission1Job2Choice1"))
            elif choice == 2:
                Inventory.set_sub_mission_status(1, 2, 2)
                print(Fore.GREEN+Strings.get("Mission1Job2Choice2"))
            elif choice == 3:
                Inventory.set_sub_mission_status(1, 2, 3)
                print(Fore.GREEN+Strings.get("Mission1Job2Choice3"))
            input("\nApasă 'Enter' pentru a continua...\n")
            print(Fore.GREEN+Strings.get("Mission1Job2Conclusion"))
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission1_choice()
    elif choice == 3:
        if Inventory.check_mission_status_for_job(1, 1) and Inventory.check_mission_status_for_job(1, 2):
            # Presents the optimal scenario where the user completed sub-missions 1 and 2
            print(Fore.GREEN+Strings.get("Mission1Job3Start1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Continui cu lupta?")
            if raspuns:
                # The player chose to continue the fight with all preparations done
                print(Fore.GREEN+Strings.get("Mission1Job3Start2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.GREEN+Strings.get("Mission1Job3Start3"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.GREEN+Strings.get("Mission1Job3Start4"))
                Inventory.set_mission_status(1)
                # If the user completed all 3 missions, they are sent to the final message
                if (Inventory.check_mission_status(1) and Inventory.check_mission_status(2)
                        and Inventory.check_mission_status(3)):
                    print(Fore.GREEN+Strings.get("FinalMessage"))
                else:
                    input("\nApasă 'Enter' pentru a te întoarce la începutul jocului...\n")
                    do_start()
            else:
                # The player chose not to continue the fight
                print(Fore.BLUE+Strings.get("Mission1Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission1_choice()
        elif Inventory.check_mission_status_for_job(1, 1) and not Inventory.check_mission_status_for_job(1, 2):
            # Presents the scenario where mission 1 is completed but mission 2 is not
            print(Fore.GREEN+Strings.get("Mission1Job3ErrorOnJob1_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"\nContinui cu lupta?")
            if raspuns:
                # The player chose to continue mission 3 but only completed mission 1
                print(Fore.RED+Strings.get("Mission1Job3ErrorOnJob1_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission1Job3ErrorOnJob1_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission1_choice()
            else:
                # After the failure message, the user is returned to mission selection
                print(Fore.BLUE+Strings.get("Mission1Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission1_choice()
        elif not Inventory.check_mission_status_for_job(1, 1) and Inventory.check_mission_status_for_job(1, 2):
            # Prezintă scenariul în care este terminata dubmisiunea 2, dar submisiunea 1 nu
            print(Fore.GREEN+Strings.get("Mission1Job3ErrorOnJob2_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Continui cu lupta?")
            if raspuns:
                print(Fore.RED+Strings.get("Mission1Job3ErrorOnJob2_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission1Job3ErrorOnJob2_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission1_choice()
            else:
                print(Fore.BLUE+Strings.get("Mission1Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission1_choice()
        else:
            # Specific logic for the case where the user did not complete any of the first 2 sub-missions
            print(Fore.GREEN+Strings.get("Mission1Job3ErrorOnAnyJob_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Accepți misiunea?")
            if raspuns:
                # The player has chosen to join the mission
                # You can continue the story or introduce the next stage of the game here
                print(Fore.RED+Strings.get("Mission1Job3ErrorOnAnyJob_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission1Job3ErrorOnAnyJob_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission1_choice()
            else:
                # The player chose not to join the mission
                print(Fore.BLUE+Strings.get("Mission1Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission1_choice()


def do_mission2():
    if Inventory.check_mission_status_for_job(2, 1):
        print(Fore.BLUE+"Ai pus deja baricadele! Te rog să alegi o altă misiune.")
        input("\nApasă 'Enter' pentru a continua...\n")
        do_start()
    else:
        print(Fore.GREEN+Strings.get("Mission2Title"))
        sleep(1)  # Wait for 2 seconds
        print(Fore.GREEN+Strings.get("Mission2Text1"))
        input("\nApasă 'Enter' pentru a continua...\n")
        print(Fore.GREEN+Strings.get("Mission2Text2"))
        input("\nApasă 'Enter' pentru a continua...\n")

        do_mission2_choice()


def do_mission2_choice():
    print(Fore.YELLOW+Strings.get("Mission2Text3"))
    choice = Utils.inputNumber(Fore.BLUE+"Te rog să alegi cu care misiune vrei să începi "
                               "introducând numărul corespunzător și apoi să apeși 'Enter': ")
    if choice == 1:
        # If the user previously completed mission 1, we send them back to mission selection
        if Inventory.check_mission_status_for_job(2, 1):
            print(Fore.BLUE+"Ai vizitat deja Câmpul Pietrelor! Te rog să alegi o altă misiune.")
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission2_choice()
        else:
            print(Fore.YELLOW+Strings.get("Mission2Job1Choices"))
            choice = Utils.inputNumber("Alege un tip și apoi să apasă 'Enter': ")
            if choice == 1:
                Inventory.set_sub_mission_status(2, 1, 1)
                print(Fore.GREEN+Strings.get("Mission2Job1Choice1"))
            elif choice == 2:
                Inventory.set_sub_mission_status(2, 1, 2)
                print(Fore.GREEN+Strings.get("Mission2Job1Choice2"))
            elif choice == 3:
                Inventory.set_sub_mission_status(2, 1, 3)
                print(Fore.GREEN+Strings.get("Mission2Job1Choice3"))
            input("\nApasă 'Enter' pentru a continua...\n")
            print(Fore.GREEN+Strings.get("Mission2Job1Conclusion"))
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission2_choice()
    elif choice == 2:
        # If the user previously completed mission 2, we send them back to mission selection
        if Inventory.check_mission_status_for_job(2, 2):
            print(Fore.BLUE+"Ai vizitat deja Pădurea Fumurilor! Te rog să alegi o altă misiune.")
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission2_choice()
        else:
            print(Fore.YELLOW+Strings.get("Mission2Job2Choices"))
            choice = Utils.inputNumber("Alege un tip și apoi să apasă 'Enter': ")
            if choice == 1:
                Inventory.set_sub_mission_status(2, 2, 1)
                print(Fore.GREEN+Strings.get("Mission2Job2Choice1"))
            elif choice == 2:
                Inventory.set_sub_mission_status(2, 2, 2)
                print(Fore.GREEN+Strings.get("Mission2Job2Choice2"))
            elif choice == 3:
                Inventory.set_sub_mission_status(2, 2, 3)
                print(Fore.GREEN+Strings.get("Mission2Job2Choice3"))
            input("\nApasă 'Enter' pentru a continua...\n")
            print(Fore.GREEN+Strings.get("Mission2Job2Conclusion"))
            input("\nApasă 'Enter' pentru a continua...\n")
            do_mission2_choice()
    elif choice == 3:
        if Inventory.check_mission_status_for_job(2, 1) and Inventory.check_mission_status_for_job(2, 2):
            # Presents the optimal scenario where the user completed sub-missions 1 and 2
            print(Fore.GREEN+Strings.get("Mission2Job3Start1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Continui cu lupta?")
            if raspuns:
                # The player chose to continue the fight with all preparations done
                print(Fore.GREEN+Strings.get("Mission2Job3Start2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.GREEN+Strings.get("Mission2Job3Start3"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.GREEN+Strings.get("Mission2Job3Start4"))
                Inventory.set_mission_status(2)
                # If the user completed all 3 missions, they are sent to the final message
                if (Inventory.check_mission_status(1) and Inventory.check_mission_status(2)
                        and Inventory.check_mission_status(3)):
                    print(Fore.GREEN+Strings.get("FinalMessage"))
                else:
                    input("\nApasă 'Enter' pentru a te întoarce la începutul jocului...\n")
                    do_start()
            else:
                # The player chose not to continue the fight
                print(Fore.GREEN+Strings.get("Mission2Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission2_choice()
        elif Inventory.check_mission_status_for_job(2, 1) and not Inventory.check_mission_status_for_job(2, 2):
            # Presents the scenario where mission 1 is completed but mission 2 is not
            print(Fore.GREEN+Strings.get("Mission2Job3ErrorOnJob1_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"\nContinui cu lupta?")
            if raspuns:
                # The player chose to continue mission 3 but only completed mission 1
                print(Fore.RED+Strings.get("Mission2Job3ErrorOnJob1_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission2Job3ErrorOnJob1_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission2_choice()
            else:
                # After the failure message, the user is returned to mission selection
                print(Fore.GREEN+Strings.get("Mission2Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission2_choice()
        elif not Inventory.check_mission_status_for_job(2, 1) and Inventory.check_mission_status_for_job(2, 2):
            # Presents the scenario where mission 2 is completed but mission 1 is not
            print(Fore.GREEN+Strings.get("Mission2Job3ErrorOnJob2_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Continui cu lupta?")
            if raspuns:
                print(Fore.RED+Strings.get("Mission2Job3ErrorOnJob2_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission2Job3ErrorOnJob2_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission2_choice()
            else:
                print(Fore.GREEN+Strings.get("Mission2Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission2_choice()
        else:
            # Specific logic for the case where the user did not complete any of the first 2 sub-missions
            print(Fore.GREEN+Strings.get("Mission2Job3ErrorOnAnyJob_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Accepți misiunea?")
            if raspuns:
                # The player has chosen to join the mission
                print(Fore.RED+Strings.get("Mission2Job3ErrorOnAnyJob_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission2Job3ErrorOnAnyJob_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission2_choice()
            else:
                # The player chose not to join the mission
                print(Fore.GREEN+Strings.get("Mission2Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission2_choice()


def do_mission3():
    if Inventory.check_mission_status_for_job(3, 1):
        print("Ai aparat deja cetatea! Te rog să alegi o altă misiune.")
        input("\nApasă 'Enter' pentru a continua...\n")  
        do_start()
    else:
        print(Fore.GREEN+Strings.get("Mission3Title"))
        sleep(2)  # Wait for 2 seconds
        print(Fore.GREEN+Strings.get("Mission3Text1"))
        input("\nApasă 'Enter' pentru a continua...\n")  
        print(Fore.GREEN+Strings.get("Mission3Text2"))
        input("\nApasă 'Enter' pentru a continua...\n")  

        do_mission3_choice()


def do_mission3_choice():
    print(Fore.YELLOW+Strings.get("Mission3Text3"))
    choice = Utils.inputNumber(Fore.BLUE+"Te rog să alegi cu care misiune vrei să începi "
                               "introducând numărul corespunzător și apoi să apeși 'Enter': ")
    if choice == 1:
        # If the user previously completed mission 1, we send them back to mission selection
        if Inventory.check_mission_status_for_job(3, 1):
            print(Fore.BLUE+"Ai consolidat deja intrarea! Te rog să alegi o altă misiune.")
            input("\nApasă 'Enter' pentru a continua...\n")  
            do_mission3_choice()
        else:
            print(Fore.YELLOW+Strings.get("Mission3Job1Choices"))
            choice = Utils.inputNumber("Alege un tip și apoi să apasă 'Enter': ")
            if choice == 1:
                Inventory.set_sub_mission_status(3, 1, 1)
                print(Fore.GREEN+Strings.get("Mission3Job1Choice1"))
            elif choice == 2:
                Inventory.set_sub_mission_status(3, 1, 2)
                print(Fore.GREEN+Strings.get("Mission3Job1Choice2"))
            elif choice == 3:
                Inventory.set_sub_mission_status(3, 1, 3)
                print(Fore.GREEN+Strings.get("Mission3Job1Choice3"))
            input("\nApasă 'Enter' pentru a continua...\n")  
            print(Fore.GREEN+Strings.get("Mission3Job1Conclusion"))
            input("\nApasă 'Enter' pentru a continua...\n")  
            do_mission3_choice()
    elif choice == 2:
        # If the user previously completed mission 2, we send them back to mission selection
        if Inventory.check_mission_status_for_job(3, 2):
            print(Fore.BLUE+"Ai setat deja capcanele! Te rog să alegi o altă misiune.")
            input("\nApasă 'Enter' pentru a continua...\n")  
            do_mission3_choice()
        else:
            print(Fore.YELLOW+Strings.get("Mission3Job2Choices"))
            choice = Utils.inputNumber("Alege un tip și apoi să apasă 'Enter': ")
            if choice == 1:
                Inventory.set_sub_mission_status(3, 2, 1)
                print(Fore.GREEN+Strings.get("Mission3Job2Choice1"))
            elif choice == 2:
                Inventory.set_sub_mission_status(3, 2, 2)
                print(Fore.GREEN+Strings.get("Mission3Job2Choice2"))
            elif choice == 3:
                Inventory.set_sub_mission_status(3, 2, 3)
                print(Fore.GREEN+Strings.get("Mission3Job2Choice3"))
            input("\nApasă 'Enter' pentru a continua...\n")  
            print(Fore.GREEN+Strings.get("Mission3Job2Conclusion"))
            input("\nApasă 'Enter' pentru a continua...\n")  
            do_mission3_choice()
    elif choice == 3:
        if Inventory.check_mission_status_for_job(3, 1) and Inventory.check_mission_status_for_job(3, 2):
            # Presents the optimal scenario where the user completed sub-missions 1 and 2
            print(Fore.GREEN+Strings.get("Mission3Job3Start1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Continui cu lupta?")
            if raspuns:
                # The player chose to continue the fight with all preparations done
                print(Fore.GREEN+Strings.get("Mission3Job3Start2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.GREEN+Strings.get("Mission3Job3Start3"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.GREEN+Strings.get("Mission3Job3Start4"))
                Inventory.set_mission_status(3)
                if (Inventory.check_mission_status(1) and Inventory.check_mission_status(2)
                        and Inventory.check_mission_status(3)):
                    print(Fore.GREEN+Strings.get("FinalMessage"))
                else:
                    input("\nApasă 'Enter' pentru a te întoarce la începutul jocului...\n")
                    do_start()
            else:
                # The player chose not to continue the fight
                print(Fore.GREEN+Strings.get("Mission3Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission3_choice()
        elif Inventory.check_mission_status_for_job(3, 1) and not Inventory.check_mission_status_for_job(3, 2):
            # Presents the scenario where mission 1 is completed but mission 2 is not
            print(Fore.GREEN+Strings.get("Mission3Job3ErrorOnJob1_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"\nContinui cu lupta?")
            if raspuns:
                # The player chose to continue mission 3 but only completed mission 1
                print(Fore.RED+Strings.get("Mission3Job3ErrorOnJob1_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission3Job3ErrorOnJob1_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission3_choice()
            else:
                # The player chose not to continue the fight
                print(Fore.GREEN+Strings.get("Mission3Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission3_choice()
        elif not Inventory.check_mission_status_for_job(3, 1) and Inventory.check_mission_status_for_job(3, 2):
            # Presents the scenario where mission 2 is completed but mission 1 is not
            print(Fore.GREEN+Strings.get("Mission3Job3ErrorOnJob2_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Continui cu lupta?")
            if raspuns:
                print(Fore.RED+Strings.get("Mission3Job3ErrorOnJob2_2"))
                input("\nApasă 'Enter' pentru a continua...\n")
                print(Fore.RED+Strings.get("Mission3Job3ErrorOnJob2_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")
                do_mission3_choice()
            else:
                print(Fore.GREEN+Strings.get("Mission3Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")
                do_mission3_choice()
        else:
            # Specific logic for the case where the user did not complete any of the first 2 sub-missions
            print(Fore.GREEN+Strings.get("Mission3Job3ErrorOnAnyJob_1"))
            raspuns = Utils.inputYesNo(Fore.BLUE+"Accepți misiunea?")
            if raspuns:
                # The player has chosen to join the mission
                print(Fore.RED+Strings.get("Mission3Job3ErrorOnAnyJob_2"))
                input("\nApasă 'Enter' pentru a continua...\n")  
                print(Fore.RED+Strings.get("Mission3Job3ErrorOnAnyJob_3"))
                input("\nApasă 'Enter' pentru a încerca o strategie diferită\n")  
                do_mission3_choice()
            else:
                # The player chose not to join the mission 
                print(Fore.GREEN+Strings.get("Mission3Job3Return"))
                input("\nApasă 'Enter' pentru a continua...\n")  
                do_mission3_choice()


do_welcome()
