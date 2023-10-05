#Text based adventure game I sometimes work on between projects.
#It's not done and I'm not a writer so don't expect anything ground breaking.


#constants
STARTING_CASH = 200


class player:
    def __init__(self):
        self.self_status = "okay"
        self.wife_status = "okay"
        self.daughter_status = "okay"
        self.son_status = "okay"
        self.wolf_status = "absent"
        self.wolf_name = "none"
        self.oxen = 1
        self.wife_respect = 5
        self.son_respect = 5
        self.daughter_respect = 5
        self.food = 0
        self.ammo = 0
        self.materials = 0
        self.inventory = []
        self.wagon_status = "good"
        self.money = STARTING_CASH
        self.location = "beginnning"
        self.day = 0
        self.hungryman_helped = False
        self.trait = 0
        self.knowledge = []
    
    def gain(self, item):
        self.inventory.append(item)
    
    def lose(self, item):
        self.inventory.remove(item)
    
    def check(self, item):
        for z in self.inventory:
            if z == item:
                return True
        return False

    def kgain(self, idea):
        self.knowledge.append(idea)
    
    def knowledgeCheck(self, idea):
        for x in self.knowledge:
            if x == idea:
                return True
        return False


#FILE ORDER is SAME as CLASS ORDER
def save(p):
    with open("D:\\Desktop\\Projects\\Code\\Python\\save1.txt", 'w') as file:
        file.write(p.self_status)
        file.write("\n")
        file.write(p.wife_status)
        file.write("\n")
        file.write(p.daughter_status)
        file.write("\n")
        file.write(p.son_status)
        file.write("\n")
        file.write(p.wolf_status)
        file.write("\n")
        file.write(p.wolf_name)
        file.write("\n")
        file.write(str(p.oxen))
        file.write("\n")
        file.write(str(p.wife_respect))
        file.write("\n")
        file.write(str(p.son_respect))
        file.write("\n")
        file.write(str(p.daughter_respect))
        file.write("\n")
        file.write(str(p.food))
        file.write("\n")
        file.write(str(p.ammo))
        file.write("\n")
        file.write(str(p.materials))
        file.write("\n")
        file.write(p.wagon_status)
        file.write("\n")
        file.write(str(p.money))
        file.write("\n")
        file.write(p.location)
        file.write("\n")
        file.write(str(p.day))
        file.write("\n")
        file.write(str(p.hungryman_helped))
        file.write("\n")
        file.write(p.trait)
        file.write("\n")

        #KNOWLEDGE MUST BE IN THIS POSITION
        for i in p.knowledge:
            file.write(i)
            file.write("\n")
        
        file.write("END KNOWLEDGE\n")
        
        #INVTENTORY MUST BE LAST
        for i in p.inventory:
            file.write(i)
            file.write("\n")
        
        file.close()


def savegame(p):
    print("Press 1 to save the game now.")
    print("Press 2 to continue.")
    x = 0
    while x != 1 and x != 2:
        x = choice()
    if x == 1:
        save(p)

def enterE():
    print("Press enter to continue.")
    numb = input()
    print("\n\n")


def choice():
    done = False
    while done == False:
        x = input("Choice: ")
        if x != "":
            z = eval(x)
            done = True
    return z
   

def dead():
    print("Game over.")
    exit()     

def noFood():
    print("You have run out of food.")
    print("You and your family starved to death.")
    dead()


def ask():
    z = 'a'
    while z != 'y' and z != 'n':
        z = input("(y/n): ")
    
    if z == 'y':
        return True
    else:
        return False



def hud(p):
    print("\n-------------------")
    print("Money: $", p.money, sep='')
    print(p.food, " days of food and water", sep='')
    print("Inventory: ", p.inventory, sep='')
    print("Ammo: ", p.ammo, " | Spare Materials: ", p.materials, sep='')
    print("Wagon Condition: ", p.wagon_status, sep='')
    print("-------------------\n")


def foodCheck(p):
    if p.food < 10:
        print("Are you sure you want to leave town with less than 10 days of food and water?")
        z = 'a'
        while z != 'y' and z != 'n':
            z = input("(y/n): ")
        if z[0] == 'y':
            return True
        if z[0] == 'n':
            return False
    else:
        return True


def sellItems(p):
    print("Select an item to sell.")
    sold = 0
    x = 0
    listNum = 2
    while x != listNum:
        print("\nMoney: $", p.money, " + ", sold, sep='')
        print('')
        listNum = 2
        sellList = {}
        for i in p.inventory:
            if i == "tools" or i == "firearm" or i == "map" or i == "bear_corpse" or (i == "necklace" and p.location != "corfield"):
                sellList[listNum] = i
                listNum += 1


        counter = 2
        print("1. Sell Food")
        while counter != listNum:
            print(counter, ". ", sellList[counter], sep='')
            counter += 1
        print(listNum, ". Stop selling", sep='')
        
        x = 0
        while x < 1 or x > listNum:
            x = choice()
        
        if x == 1:
            print("How much food are you willing to sell? ($2/day of food): ")
            y = choice()
            if y <= p.food:
                p.food -= y
                sold += 2 * y
                print("Sold ", y, " days of food for $", (2 * y), ".", sep='')
                enterE()
        
        if x != listNum and x > 1 and x < listNum:
            if sellList[x] == "tools":
                print("Sell tools for $25?")
            elif sellList[x] == "firearm":
                print("Sell firearm for $50?")
            elif sellList[x] == "map":
                print("Sell map for $10?")
            elif sellList[x] == "bear_corpse":
                print("Sell bear corpse for $100?")
            elif sellList[x] == "necklace" and p.location != "corfield":
                print("Sell necklace for $150?")
            elif sellList[x] == "wolf_corpse_01":
                print("Sell Wolf Corpse for $120?")
            y = 'a'
            while y != 'n' and y != 'y':
                y = input("(y/n):")
            if y == 'n':
                x = 0
            elif y == 'y':
                if sellList[x] == "tools":
                    sold += 25
                    p.lose("tools")
                    print("Tools sold.")
                    enterE()
                elif sellList[x] == "firearm":
                    sold += 50
                    p.lose("firearm")
                    print("Firearm sold.")
                    enterE()
                elif sellList[x] == "map":
                    sold += 10
                    p.lose("map")
                    print("Map sold.")
                    enterE()
                elif sellList[x] == "bear_corpse":
                    sold += 100
                    p.lose("bear_corpse")
                    print("Bear corpse sold.")
                    enterE()
                elif sellList[x] == "necklace":
                    sold += 150
                    p.lose("necklace")
                    print("Necklace sold.")
                    enterE()
                elif sellList[x] == "wolf_corpse_01":
                    sold += 120
                    p.lose("wolf_corpse_01")
                    print("Wolf corpse sold.")
                    enterE()
    
    if p.trait == "silver":
        print("[Silver] Gained an extra $" + str(sold*0.3) + ".")
        enterE()
        return sold * 1.3
    else:
        return sold


def checkFamily(p):
    print('')
    if p.wife_status == "dead":
        print("Wife is dead.")
    elif p.wife_respect < 2:
        print("Your wife is shaken up.")
    elif p.wife_status == "okay":
        print("Wife is okay.")
    
    if p.son_status == "dead":
        print("Son is dead.")
    elif p.son_respect < 2:
        print("Your son won't look at you.")
    elif p.son_status == "okay" or "unnoticeably_sick":
        print("Son is okay.")
    
    if p.daughter_status == "dead":
        print("Daughter is dead.")
    elif p.daughter_respect < 2:
        print("Your daughter is shaking.")
    elif p.daughter_status == "okay":
        print("Daughter is okay.")  
    
    enterE() 


def doctors(p):
    print("You walk into the doctor's office.\n")
    print("\t1. Get you and your family checked $30")
    print("\t2. Leave doctor's")
    y = 0
    while y != 1 and y != 2:
        y = choice()
    
    if y == 1:
        print("Doctor is checking...")
        enterE()
        if p.self_status == "okay":
            print("You are healthy.")
            
        if p.wife_status == "okay":
            print("Wife is healthy.")
        
        if p.son_status == "okay":
            print("Son is healthy.")
        elif p.son_status == "unnoticeably_sick":
            print("\nThe doctor has detected an incubating cold in your son.")
            print("He gives your son some cough medicine. It should make him feel better.\n")
            p.son_status = "okay"
        
        if p.daughter_status == "okay":
            print("Daughter is healthy.")
        
        print("\nYou paid the doctor $30.")
        enterE()
    

def travel(p, d):
    print("Traveling...")
    for x in range(d):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()





#initalizing
p = player()
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")





def coldpine_to_wissu():
    print("You set out towards Wissu.")
    enterE()


def fortd_to_neslei():
    print("You set out towards Neslei.")
    enterE()


def fortd_to_venseas():
    print("You set out towards Venseas.")
    enterE()


def westsaltor():
    print("Welcome to West Saltor")
    p.location = "westsaltor"
    enterE()
    
    savegame(p)


def fortd_to_westsaltor():
    print("You set out towards West Saltor.")
    enterE()
    
    travel(p, 2)
    print("You travel for 2 days and arrive at a farmstead.")
    print("The owner is a family man like yourself. Says he needs help fixing his plow.")
    enterE()
    if p.trait == "handy":
        print("[Handyman] You tell him you can fix the plow no problem.")
        if p.check("tools") == True:
            print("You use your tools to repair his plow.")
        else:
            print("You use his tools to repair the plow.")
        enterE()
        print("The man is greatful. He pays you $70 and give you some delicious home cooked food.\t(+8 food)")
        p.money += 70
        p.food += 8
        enterE()
    else:
        print("You tell the man you are no repairman.")
        enterE()
        print("He tells he can fix it if you helped him.")
        print("Help the man?\n")
        if ask() == True:
            print("You spend the day helping the man fix his plow. He is greatful you stopped by.")
            print("He pays you $25 for the trouble.")
            p.money += 25
            enterE()
        else:
            print("You decline easy work and be on your way.")
            enterE()
    
    travel(p, 4)
    print("You travel for 4 days and come across an honest looking man gathering materials.")
    print("\n\t1. Greet the man.")
    print("\t2. Ignore the man and keep moving.")
    x = 0
    while x != 1 and x != 2:
        x = choice()
        
    if x == 1:
        print("You give the man a friendly greeting. He greets you back matching your friendliness.\n")
        y = 0
        while y != 3:
            print("\t1. Ask what he's doing")
            print("\t2. Ask about West Saltor\n")
            print("\t3. Say goodbye and continue.")
            y = 0
            while y < 1 or y > 3:
                y = choice()
            
            if y == 1:
                print("You ask what his purpose is here.")
                enterE()
                print("He tells you that he works closely with the general store owner in West Saltor. He is gathering resources to sell there.")
                enterE()
                if p.trait == "silver":
                    print("[Silver] You conversate with the man for awhile. He begins to respect you.")
                    print("He tells you a phrase you can mention to the store owner in West Saltor to get a discount.")
                    p.kgain("ws_store_discount")
                    enterE()
            
            elif y == 2:
                print("You ask about West Saltor.")
                print("The man tells you it's located in a central part of Acirema's Great Forest. Because of this it's a hub for trade.")
                enterE()
            
            elif y == 3:
                print("You say goodbye to the man and continue travel.")
    
    elif x == 2:
        print("You ignore the man and continue your journey.")
        enterE()
    
    
    travel(p, 1)
    print("You travel for a day and stop for the night.")
    if p.check("map") == True:
        print("[Map] Glancing at your map, you see there is a homestead nearby.")
        print("You could rob them after your family falls asleep.\n")
        print("\t1. Scope out the homestead")
        print("\t2. Go to sleep")
        x = 0
        while x != 1 and x != 2:
            x = choice()
        
        if x == 1:
            print("You decide to check out the homestead.")
            enterE()
            print("You stalk through the moonlight until you find the homestead. It is a quaint building in a small clearing in the forest.")
            print("It is likely a one-room building. You shouldn't enter if you aren't light on your feet.")
            print("\nRob homestead?")
            if ask() == True:
                print("You decide to go through with the robbery.")
                enterE()
                print("You open the door to the home and enter.")
                if p.trait == "survivor" or p.trait == "instinct":
                    print("[" + p.trait + "] Your footsteps glide across the floor.")
                    enterE()
                    print("You find some money laying out.\t(+$60)")
                    p.money += 60
                    print("You walk by a portrait of someone you presume built the homestead long ago.")
                    if p.trait == "instinct":
                        print("[Instinct] Something feels off about the portrait. You remove it from the wall and find a hidden stash of money.\t(+$110)")
                        p.money += 110
                    print("You find a hand drawn map on a table with an x marked on it.")
                    if p.trait == "survivor":
                        print("[Survivor] You examine the map and compare it to your own. The x is marked near the road to Neslei from West Saltor.")
                        p.kgain("x_near_neslei")
                        enterE()
                    else:
                        print("You are unable to determine where that x is supposed to be.")
                    
                    print("You cannot find anything more. You decide to leave.")
                    enterE()
                    print("You return to bed and sleep. You set off in the morning.")
                else:
                    print("You place your foot on a creaky floorboard. The sound contrasts so sharply with the quiet it hurts your ears.")
                    enterE()
                    print("The owner of the homestead snaps awake. He sees your shadow in the doorway.")
                    print("Make your move.\n")
                    print("\t1. Run like hell")
                    if p.check("firearm") == True:
                        print("\t2. Shoot the man")
                    print('')
                    x = 0
                    while x != 1 and not (x == 2 and p.check("firearm") == False):
                        x = choice()
                    
                    if x == 1:
                        print("You aren't stupid. You take off running as soon as you see the guy move.")
                        enterE()
                        print("The man chases you out of his home but loses you in the night.")
                        print("You head back to where you've camped and go to sleep.")
                    
                    elif x == 2:
                        print("You shoot the man.")
                        enterE()
                        print("Blood springs from his chest where the bullet entered. The wound is fatal.")
                        print("The man dies quickly. He's old. You use his advanced age to justify your murder.")
        
        elif x == 2:
            print("You decide to go to bed and continue travel in the morning.")
            enterE()



#FORT DENCEPERS
def fortd():
    print("Welcome to Fort Dencepers.")
    p.location = "fortd"
    enterE()
    
    savegame(p)
        
    print("Fort Dencepers is the largest settlement you've seen. It exists in a large clearing in the forest.")
    print("There are a few dozen buildings surrounding a large stone fort. Men armed better than most guard it.")
    enterE()
    
    x = 0
    while x != 8:
        print("\nYou are in Fort Dencepers.")
        hud(p)
        print("Day: ", p.day)
        print('')
        print("ACTIONS: ")
        print("\t1. Read road signs")
        print("\t2. Visit Store")
        print("\t3. Sell items")
        print("\t4. Visit doctor")
        print("\t5. Check on family")
        print("\t6. Converse at local inn.")
        print("\t7. Approach fort seeking a job.")
        print("\t8. Leave Fort Dencepers")
        
        x = 0
        while x > 8 or x < 1:
            x = choice()
        
        if x == 1:
            print("The road to the northeast leads to West Saltor. It is a 17 day journey.")
            print("This road is travelled often and poses little risk.\n")
            print("The road east leads to Neslei. It is a 31 day journey.")
            print("The locals mention this road is generally safe but not completely outside of savage territory.\n")
            print("The road southeast leads to Venseas. It is a 12 day journey.")
            print("This path leads into dense forest. The locals say nobody has come from Venseas in many days.")
            enterE()
        
        elif x == 2:
            y = 0
            while y != 10:
                print("SHOP:")
                print("1. Tools: $70")
                print("2. 1 day of food and water: $7")
                print("3. Firearm: $130")
                print("4. Ammo: $15")
                print("5. Map of the Region: $25")
                print("6. Spare Materials: $40")
                print("7. Extra Ox $140")
                print("8. Fishing Pole $25")
                print("9. Almanac $115")
                #print("10. Warm clothes $120")
                print("10. Leave Store")
                hud(p)
                y = choice()
            
                if y == 1:
                    if p.check("tools") == False:
                        if p.money >= 70:
                            p.money -= 70
                            p.gain("tools")
                            print("Tools bought successfully.")
                            enterE()
                    else:
                        print("You already have tools.")
                        enterE()
                elif y == 2:
                    z = eval(input("How many days of food would you like to buy?: "))
                    if (z * 7) > p.money:
                        print("You don't have enough money for that much food.")
                        enterE()
                    else:
                        p.money -= (z * 7)
                        p.food += z
                        print("Bought ", z, " days of food.", sep='')
                        enterE()
                elif y == 3:
                    if p.check("firearm") == False:
                        if p.money >= 130:
                            p.money -= 130
                            p.gain("firearm")
                            print("Firearm bought successfully.")
                            enterE()
                        else:
                            print("Not enought money.")
                            enterE()
                    else:
                        print("You already own a firearm.")
                        enterE()
                elif y == 4:
                    y = eval(input("How much ammo would you like? (1-3 recommended): "))
                    if y * 15 > p.money:
                        print("Not enough money.")
                        enterE()
                    else:
                        p.money -= y * 15
                        p.ammo += y
                        print("Bought ammo successfully.")
                        enterE()
                elif y == 5:
                    if p.check("map") == False:
                        if p.money >= 25:
                            p.money -= 25
                            p.gain("map")
                            print("Map bought.")
                            enterE()
                        else:
                            print("Not enough money")
                            enterE()
                    else:
                        print("You already own the map.")
                        enterE()
                elif y == 6:
                    if p.money >= 40:
                        p.money -= 40
                        p.materials += 1
                        print("Bought spare materials.")
                        enterE()
                    else:
                        print("Not enough money.")
                        enterE()
                elif y == 7:
                    if p.oxen == 3:
                        print("Max oxen achieved already.")
                        enterE()
                    else:
                        if p.money >= 140:
                            p.money -= 140
                            p.oxen += 1
                            print("Ox bought.")
                            enterE()
                        else:
                            print("Not enough money")
                            enterE()
                elif y == 8:
                    if p.check("pole") == False and p.money > 25:
                        print("Bought fishing pole.")
                        p.money -= 25
                        p.gain("pole")
                        enterE()
                    else:
                        print("Can't buy because you either don't have enough money or you own one already.")
                        enterE()
                elif y == 9:
                    if p.check("almanac") == False and p.money > 115:
                        print("Almanac bought.")
                        p.money -= 115
                        p.gain("almanac")
                        enterE()
                    else:
                        print("Not enough money or already own this item.")
                        
        elif x == 3:
            p.money += sellItems(p)
        
        elif x == 4:
            doctors(p)

        elif x == 5:
            checkFamily(p)
        
        elif x == 6:
            print("You decide to talk to some of the locals are the inn.")
            enterE()
            print("While conversing, you strike up conversation with an individual who seems better informed than most.")
            print("He has clearly travelled. You should ask him some things.")
            enterE()
            y = 0
            spoken = False
            while y != 5:
                print("ACTIONS:")
                print("\t1) Ask about the surrounding towns.")
                print("\t2) Ask about the Fort.")
                print("\t3) Ask about savages.")
                print("\t4) Ask about the towns far east.")
                print("\t5) Ask about the dense forest to the south.")
                print("\t6. Ask about travels.")
                print("\t7) Leave the inn.")
                y = choice()
                
                if y == 1:
                    print("You ask about the surrounding towns.")
                    print("'West Saltor to the north is near the top edge of the Great Forest.")
                    print("If you're heading east it's your last chance to head north into the mountains, although I don't know why")
                    print("you'd want to go there.'")
                    enterE()
                    print("'Neslei to the east is civilized, however there are no roads from Neslei to Lake Culmiaar so if that's")
                    print("your desitination I wouldn't head there.'")
                    print("\n\t1) Ask about Lake Culmiaar.")
                    print("\t2) Let him continue.")
                    z = 0
                    while z != 1 and z != 2:
                        z = choice()
                    
                    if z == 1:
                        print("You ask more about Lake Culimiaar.")
                        print("'It's a pretty important place for not being the largest town ever.")
                        print("The town relies on fishing, and there's a good living there for you if you're good at fishing.")
                        print("There's also the researcher there who everyone thinks is all that.' *The man rolls his eyes*")
                        print("'Guy is nothing but a moron. Don't listen to him.'")
                        print("It seems personal. You decide to change the subject and ask about Venseas.")
                        p.knowledge.append("moron_in_lc")
                        enterE()
                    
                    print("'Venseas is a pretty worthless town - if you can call it that.")
                    print("It's just a few buildings, nobody there even sells anything. And the locals are not friendly in the slightest.")
                    print("Everyone is talking about how nobody has came into town from there in quite a while.")
                    print("I hope something bad happened to them.'")
                    enterE()
                
                elif y == 2:
                    print("You ask about the Fort.")
                    print("'The fort in town is Fort Dencepers, same name as the town.")
                    print("It was built by a group of settlers who banded together in response to the growing savage threat.")
                    print("I've heard they pay well enough for a man to feed his entire family, but they don't take any old shmuck off the street.")
                    print("Probably why the town is so safe from savage attacks.'")
                    enterE()
                
                elif y == 3:
                    print("You ask about the savages.")
                    print("'They weren't here when this land was first settled. Land was void of human life far as we knew.")
                    print("It was only after we began settling east of West Saltor that they began to move into our territory.")
                    print("Did you know they used to cause trouble in Bordertown? I'm glad I wasn't around when things were that bad.'")
                    enterE()
                    print("'Anyway, I know they look human, but you can't give them the benefit of the doubt.")
                    print("Do not hesitate to kill them. They want you dead.'")
                    if p.check("firearm") == False:
                        print("The man looks you up and down.")
                        print("'I don't see a firearm on you, friend. I would suggest changing that if you plan to travel out of the Fort.'")
                    enterE()
                    
                elif y == 4:
                    print("You ask about the towns far to the east.")
                    print("'The only place I've heard about east of Nesli is New Saint. I've never been but I hear they've got work for just about anyone")
                    print("I'll bet just about anyone could settle down there.'")
                    print("\n\t1) Ask for directions to New Saint.")
                    print("\t2)Change the subject.")
                    z = 0
                    while z != 1 and z != 2:
                        z = choice()
                    
                    if z == 1:
                        print("New Saint? You shouldn't worry about missing it. Head east far enough and all roads will lead you to it.")
                        enterE()
                
                elif y == 5:
                    print("You ask about the dense forest to the southeast.")
                    print("'You'd do best to avoid that area. That place has savages all over it - and they know the land better than you.")
                    print("Not to mention the settlers in Venseas, the town down there, are almost as mean as the savages.'")
                    print("\n\t1) State your intention to travel to Venseas.")
                    print("\t2) Change the subject.")
                    z = 0
                    while z != 1 and z != 2:
                        z = choice()
                    
                    if z == 1:
                        print("You tell him you intend to head to Venseas.")
                        print("The man examines you closely.")
                        if p.trait == "instinct":
                            print("[Instinct] The man notices your quick eye.")
                            if p.check("firearm") == True:
                                print("'You'll do fine. Just keep that pistol handy and plenty of ammo. More than 5 shots at all times.'")
                                enterE()
                            else:
                                print("'If you buy yourself a gun and lots of ammo you'll be okay.'")
                                enterE()
                        elif p.trait == "handy":
                            print("[Handy] The man notes your resourceful nature.")
                            print("'You seem a handy sort. Perhaps if you travelled that way you could devise a way to protect yourself, as long as you had the materials for it.'")
                            enterE()
                        else:
                            print("The man notices no quaility which sticks out to him.")
                            print("'I'm not sure that path would end well for someone like you.'")
                            enterE()
                
                elif y == 6:
                    print("You ask the man about his travels.")
                    if p.trait == "silver":
                        print("[Silver] The man hesitates, then a look of approval comes across his face.")
                        print("'You don't want to hear my story, friend. But if you head to Neslei, you should stop and see a friend of mine.")
                        print("He usually hangs out along the road. He isn't friendly but if you tell him that you know where the red grows he'll open up to you.")
                        print("He's more interesting than I and can give you some useful things, provided you got money.'")
                        p.knowledge.append("neslei_road_phrase")
                        enterE()
                
                if y != 7:
                    spoken = True
                
                if y == 7:
                    if spoken == True:
                        print("You thank the man for the information and leave.")
                        enterE()
                    else:
                        print("You leave before asking the man anything.")
                        enterE()
                        
                        
        elif x == 7:
            print("You approach Fort Dencepers. It's stone walls stand much taller than you.")
            enterE()
            print("The guard at the gate appears impatient. You ask him if they need any help.")
            enterE()
            print("He tells you they are not looking for anyone who hasn't proven themselves. If you want to join you have to kill a few savages first.")
            print("You cannot impress this man enough to get him to let you in. Perhaps if you travel the roads to the southeast you'll find some savages.")
            enterE()
        
        elif x == 8:
            if foodCheck(p) == True:
                z = 0
                print("Which path are you taking out of Fort Dencepers?\n")
                print("\t1. Travel northwest to West Saltor")
                print("\t2. Travel west to Neslei")
                print("\t3. Travel southwest to Venseas")
                while z != 1 and z != 2 and z != 3:
                    z = choice()
                
                if z == 1:
                    fortd_to_westsaltor()
                
                elif z == 2:
                    fortd_to_neslei()
                
                elif z == 3:
                    fortd_to_venseas()
                
            else:
                x = 0
                    
                    
        
        




def fork_to_westsaltor():
    print("You continue travelling.")
    enterE()
    travel(p, 3)
    print("You travel for 3 days and find a lone wolf.")
    print("He looks hungry but tame. Maybe you should give him some food.\n")
    print("\t1) Offer 5 days of food and water.")
    print("\t2) Ignore the wolf.")
    if p.check("firearm") == True:
        print("\t3) [Firearm] Shoot the wolf")
    x = 0
    while x < 1 or x > 3:
        x = choice()
    
    if x == 1:
        print("You feed the wolf food.")
        enterE()
        print("The wolf's mood has improved. It wants to come with you.\n")
        print("1) Bring the wolf along.")
        print("2) Shoo the wolf away.")
        y = 0
        while y != 1 and y != 2:
            y = choice()
        if y == 1:
            print("You welcome the wolf's company.")
            p.wolf_status = "okay"
        elif y == 2:
            print("You try to shoo the wolf away but it is determined to follow you.")
            print("Your daughter catches you trying to shoo the wolf. She wants it to come along.")
            print("If not, there's only one way to get the wolf to stop following you.\n")
            print("1) Bring the wolf along.")
            print("2) Shoot the wolf.")
            z = 0
            while z != 1 and z != 2:
                z = choice()
                if z == 2 and not (p.check("firearm") == True and p.ammo > 0):
                    print("You cannot shoot the wolf as you lack either a gun or ammo.")
                    z = 0
                    enterE()
            
            if z == 1:
                print("You welcome the wolf's company.")
                p.wolf_status = "okay"
            
            if z == 2:
                if p.check("firearm") == True and p.ammo > 0:
                    print("You shoot the wolf. What a waste of food.")
                    enterE()
                    print("Your brutality scars your daughter.")
                    p.daughter_respect -= 2
                    print("You load the animal into your wagon.")
                    print("Wolf Corpse gained.")
                    p.gain("wolf_corpse_01")
                    enterE()
        
        if p.wolf_status == "okay":
            print("You should decide on a name for your wolf.")
            p.wolf_name = input("Name: ")
            print("You have named your wolf ", p.wolf_name, ".", sep='')
    
    if x == 2:
        print("You ignore the wolf and continue.")
        enterE()
    
    if x == 3:
        print("You shoot the wolf.")
        print("You load the corpse into your wagon.")
        p.gain("wolf_corpse_01")
        enterE()
    
    travel(p, 4)
    print("You travel for 4 days and come across a man meditating along the path.")
    print("He makes no awknowledgement of your arrival. Speaking to him yields no response either.")
    if p.trait != "instinct":
        print("Something about him makes you uncomfortable.")
    print("\n\t1) Ignore the man.")
    print("\t2) Punch the man.")
    x = 0
    while x != 1 and x != 2:
        x = choice()
        
    if x == 1:
        print("You leave the man be.")
        enterE()
    
    if x == 2:
        print("You sock the guy right in the jaw.")
        enterE()
        print("He collapses. He appears to be out cold.")
        print("Searching the man, you find a single vial of purple liquid. It's impossible to know what the stuff is.")
        p.gain("strange_vial")
        enterE()
    
    
    
    #BEAR ENCOUNTER
    travel(p, 3)
    print("You travel for 3 days.")
    enterE()
    print("While stopped for the night, a very large bear wanders into where you've made camp.")
    if p.wolf_status == "absent":
        print("The bear appears calm. It is raiding your food supply.")
        print("You could let it eat some of your food, maybe it will leave after.")
        print("Or you could distract the bear while your son grabs the food. He will have to have his faith in you to succeed.")
        if p.trait == "instinct" and p.son_respect < 2:
            print("[Instinct] Your son does not trust you very much. Perhaps you shouldn't count on him.")
        if p.check("firearm") == True and p.ammo > 0:
            print("You could also shoot the thing.")
        print("\n\t1) Let the bear eat your food.")
        print("\t2) Distract the bear while your son grabs the food.")
        print("\t3) [Firearm] Shoot the bear.")
        x = 0
        while x != 1 and x != 2 and (x != 3 and p.check("firearm") and p.ammo > 0):
            x = choice()
        
        if x == 1:
            print("You decide to wait out the bear.")
            enterE()
            print("The bear eats a good amount of food and leaves the camp.")
            print("You check your food supplies and find 10 days of food missing.")
            p.food -= 10
            enterE()
        
        elif x == 2:
            print("You decide to distract the bear and send your son to get the food.")
            enterE()
            print("You run out making noise. The bear immediately turns to you.")
            print("You continue to make a fool of yourself and the bear walks slowly towards you.")
            enterE()
            if p.son_respect > 2:
                print("Trusting you, your son moves for the food.")
                enterE()
                print("Your son grabs the food successfully.")
                print("You try to move away from the bear but have intimidated it too much.")
                enterE()
                print("Your son reads the situation and throws some food away to distract the bear.")
                print("The bear hears the sound of the food hitting the bushes. He turns to it and you move away from the bear.")
                print("The massive bear soon loses interest in your camp.")
                enterE()
                print("You check the food supply. Your son threw about 1 day of food out to distract the bear.")
                p.food -= 1
                print("\n\t1) Thank your son for saving you.")
                print("\t2) Scold your son for wasting food.")
                y = 0
                while y != 1 and y != 2:
                    x = choice()
                
                if y == 1:
                    print("You tell your son he did good. He understands the trust you put in him.")
                    p.son_respect += 2
                    enterE()
                elif y == 2:
                    print("You curse at your son for throwing food. He is hurt. He thought he was doing the right thing.")
                    p.son_respect -= 2
                    enterE()
            else:
                print("Your son moves towards the food, but hesitates as he nears where it's stashed.")
                print("Your actions have inspired doubt in him. He does not trust you.")
                enterE()
                print("A twig snaps under him and the bear spins around. Your son's close proximity startles the bear.")
                print("The bear attacks your son.")
                if p.check("firearm") == True:
                    print("You left your firearm where you sleep. You cannot get to it in time.")
                print("Powerless against such a massive animal, your son is mauled.")
                enterE()
                print("The bear runs off into the forest after it is finished attacking your son.")
                print("You run to your son. The bear has clawed him all over, he is already dead.")
                p.son_status == "dead"
                enterE()
                print("Your wife and daughter witness the entire event. Your wife asks how you could be so careless.")
                if p.check("firearm") == True and p.ammo > 0:
                    print("She screams asking why you risked the life of your son when you could've shot the beast.")
                print("Neither your wife or your daughter will look at you the same again. They definately don't trust you now.")
                p.daughter_respect = 0
                p.wife_respect = 0
                enterE()
        
        elif x == 3:
            print("You decide the shoot the bear.")
            enterE()
            print("The bear lets out a blood chilling rawr. Your shot did not kill it but it definately hurt it.")
            print("The bear runs from your campsite. You and your food are safe.")
            p.ammo -= 1
            enterE()
    
    elif p.wolf_status == "okay":
        print(p.wolf_name, " barks at the beast. Startled, the bear turns towards where you're sleeping.", sep='')
        print("Damn dog.")
        enterE()
        print("The bear is pissed off at you already. You have to act.\n")
        enterE()
        if p.trait == "survivor":
            print("[Survivor] You intimidate the bear by making yourself look big and screeching like a chimp.")
            print("The bear recoils in surprise. Your confidence makes it question itself.")
            print("The beast leaves your camp.")
        elif p.trait == "handy" and p.materials > 0 and p.check("tools") == True:
            print("[Handy + More] You use tools and materials to makeshift a barricade between you and the beast.")
            print("The beat scratches at the barricade but cannot enter. It soon loses interest and leaves.")
            p.materials -= 1
            enterE()
        elif p.check("firearm") and p.ammo > 0:
            print("[Firearm] You shoot the beast with your firearm.\t(-1 ammo)")
            print("It lets out a roar and leaves your camp.")
            p.ammo -= 1
            enterE()
        else:
            if p.check("firearm") == True and p.ammo == 0:
                print("[Firearm] You grab your firearm to shoot the beast.")
                enterE()
                print("Your gun clicks when you pull the trigger. You have no ammo.")
                enterE()
            else:
                print("You have nothing to defend yourself with.")
                enterE()
            print("The beast mauls you. You are dead.")
            enterE()
            print("It is unlikely your family or your wolf ", end="")
            print(p.wolf_name + " survived the attack.")
            enterE()
            dead()
            
    
    
    
    travel(p, 2)
    print("You travel for 2 days.")
    enterE()
    if p.check("wolf_corpse_01") == True:
        print("You could harvest meat from the wolf to increase your supply of food.")
        print("You currency have " + str(p.food) + " days of food and water.\n")
        print("\t1) Keep wolf.")
        print("\t2) Use wolf corpse for food.")
        x = 0
        while x != 1 and x != 2:
            x = choice()
        
        if x == 1:
            print("You keep the wolf.")
            enterE()
        
        elif x == 2:
            print("You chop up the wolf corpse.")
            enterE()
            print("You extract 15 days of food from the body.")
            p.food += 15
            if p.trait == "survivor":
                print("[Survivor] Your experience means you were able to get 3 extra days of food from the body.")
                p.food += 3
            enterE()
    
    elif p.wolf_status == "okay":
        print("While stopped for the night, ", p.wolf_name, " finds a dead body some distance from the road.", sep='')
        print("You find $30 on the body. You pet ", p.wolf_name, " for being such a good boy.", sep='')
        enterE()
    
    print("As you sleep, you hear a twig snap in the night.")
    if p.wolf_status == "okay":
        print(p.wolf_name, " growls at the dark.", sep='')
    enterE()
    #25 days
    
    travel(p, 3)
    print("You travel for 3 days and enter West Saltor.")
    enterE()
    
    westsaltor()



def coldpine_to_westsaltor():
    print("You set out towards West Saltor.")
    enterE()
    travel(p, 2)
    print("You travel for 2 days. The air begins to get warmer.")
    enterE()
    print("While travelling the path you find grass pressed down. It appears someone travelled off the path recently.")
    print("You could investigate further.\n")
    print("\t1. Follow path in the grass.")
    print("\t2. Ignore path and keep moving.")
    x = 0
    while x != 1 and x != 2:
        x = choice()
    
    if x == 1:
        print("You decide to follow the path of pushed down grass.")
        enterE()
        print("You follow the path for a few minutes and find the body of a man. He must have died in the last few days.")
        print("Would you like to search the man for anything useful?")
        if ask() == True:
            print("You search the man.")
            enterE()
            print("You find an almanac.")
            if p.check("almanac") == False:
                p.gain("almanac")
                print("You pickup the almanac. Might be useful.")
                enterE()
            else:
                print("You already own an almanac so you leave it on the corpse.")
                enterE()
            print("Searching some more you find he was carrying $35.")
            p.money += 35
            enterE()
            print("You return to where your covered wagon was waiting for you.")
    
    print("You continue traveling down the road.")
    enterE()
    
    travel(p, 3)
    print("You travel for 2 days and reach the edge of the Great Forest.")
    enterE()
    
    travel(p, 1)
    print("You travel for a day and come to where the road meets with another.")
    enterE()
    fork_to_westsaltor()





def coldpine():
    print("Welcome to Cold Pine.")
    p.location = "coldpine"
    enterE()
    
    savegame(p)
    
    print("Cold Pine is a small settlement bordering the cold lands to the northeast.")
    print("There are few buildings. A small store is the only place of particular interest.")
    enterE()
    x = 0
    while x != 9:
        print("\nYou are in Cold Pine.")
        hud(p)
        print("Day: ", p.day)
        print('')
        print("ACTIONS: ")
        print("\t1. Read road signs")
        print("\t2. Visit Store")
        print("\t3. Sell items")
        print("\t4. Check on family")
        print("\t5. Leave Cold Pine")
        
        x = 0
        while x > 5 or x < 1:
            x = choice()
        
        if x == 1:
            print("To the northeast is the town Wissu. It is a 32 day journey.")
            print("The road there is cold. The locals seem certain anyone without warm clothes will freeze to death.\n")
            print("To the southeast is the town of West Saltor. It is a 27 day journey.")
            print("It is warmer down this road. Means there's bound to be more wildlife.")
            enterE()
        
        elif x == 2:
            y = 0
            while y != 8:
                print("SHOP:")
                print("1. Tools: $50")
                print("2. 1 day of food and water: $5")
                print("3. Firearm: $100")
                print("4. Ammo: $10")
                #print("5. Map of the Region: $20")
                print("5. Spare Materials: $30")
                #print("7. Extra Ox $100")
                #print("8. Fishing Pole $20")
                print("6. Almanac $90")
                print("7. Warm clothes $120")
                print("8. Leave Store")
                hud(p)
                y = choice()
            
                if y == 1:
                    if p.check("tools") == False:
                        if p.money >= 50:
                            p.money -= 50
                            p.gain("tools")
                            print("Tools bought successfully.")
                            enterE()
                    else:
                        print("You already have tools.")
                        enterE()
                elif y == 2:
                    z = eval(input("How many days of food would you like to buy?: "))
                    if (z * 5) > p.money:
                        print("You don't have enough money for that much food.")
                        enterE()
                    else:
                        p.money -= (z * 5)
                        p.food += z
                        print("Bought ", z, " days of food.", sep='')
                        enterE()
                elif y == 3:
                    if p.check("firearm") == False:
                        if p.money >= 100:
                            p.money -= 100
                            p.gain("firearm")
                            print("Firearm bought successfully.")
                            enterE()
                        else:
                            print("Not enought money.")
                            enterE()
                    else:
                        print("You already own a firearm.")
                        enterE()
                elif y == 4:
                    y = eval(input("How much ammo would you like? (1-3 recommended): "))
                    if y * 10 > p.money:
                        print("Not enough money.")
                        enterE()
                    else:
                        p.money -= y * 10
                        p.ammo += y
                        print("Bought ammo successfully.")
                        enterE()
                elif y == 5:
                    if p.money >= 30:
                        p.money -= 30
                        p.materials += 1
                        print("Bought spare materials.")
                        enterE()
                    else:
                        print("Not enough money.")
                        enterE()
                elif y == 6:
                    if p.check("almanac") == False and p.money > 90:
                        print("almanac bought.")
                        p.money -= 90
                        p.gain("almanac")
                        enterE()
                    else:
                        print("Not enough money or already own.")
                elif y == 7:
                    if p.check("warm_clothes") == False and p.money > 120:
                        print("Warm clothes bought.")
                        p.money -= 120
                        p.gain("warm_clothes")
                    else:
                        print("Failed to purchase; You either lack the funds or already own this item.")
                        
        elif x == 3:
            p.money += sellItems(p)
        
        elif x == 4:
            checkFamily(p)
        
        elif x == 5:
            if foodCheck(p) == True:
                z = 0
                print("Which path are you taking out of Cold Pine?\n")
                print("\t1. Travel northwest to Wissu")
                print("\t2. Travel southwest to West Saltor")
                while z != 1 and z != 2:
                    z = choice()
                
                if z == 1:
                    coldpine_to_wissu()
                
                elif z == 2:
                    coldpine_to_westsaltor()
                
                
            else:
                x = 0
            
            
        

def bordertown_to_coldpine():
    print("You have chosen to head to Cold Pine.")
    p.location = "bordertown_to_coldpine"
    enterE()
    
    travel(p, 3)
    print("You travel for 3 days. You begin to enter the Northern Plains.")
    print("A vast cold grassland.")
    enterE()
    
    travel(p, 2)
    print("You travel for 2 more days. You spot an abandoned covered wagon far from the trail.")
    print("You could investigate further.\n")
    print("\t1. Investigate Wagon")
    print("\t2. Ignore Wagon")
    
    x = 0
    while x != 1 and x != 2:
        x = choice()
    
    if x == 1:
        print("You investigate the covered wagon.")
        enterE()
        print("After searching the wagon, you find nothing but $20 and a pamphlet.")
        print("On the cover there is a bright red sun with the text 'THE END IS NIGH' written on the front.")
        print("You can't read the inside but you are certain it's fill of crap.")
        p.money += 20
        p.gain("pamphlet")
        enterE()
    
    print("You continue on your way.")
    enterE()
    
    travel(p, 4)
    print("You travel for 4 days and come across a lake.")
    print("You could fish it if you had a pole.\n")
    print("\t1. Leave lake")
    if p.check("pole") == True:
        print("\t2. [Pole] Fish lake")

    x = 0
    while x != 1 and x != 2:
        x = choice()
    
    if x == 2:
        print("You fish the lake.")
        enterE()
        if p.trait == "survivor":
            print("[Survivor] Using superior fishing techniques, you fish the hell out of this pond.")
            print("You catch a good amount of food.")
            print("+8 food")
            p.food += 8
            enterE()
        
        else:
            print("You catch some fish.")
            print("This fish will feed your family for a few days.")
            print("+3 food")
            p.food += 3
            enterE()
    
    print("You continue on your way.")
    enterE()
    
    travel(p, 2)
    print("You travel for 2 days. The air has become colder.")
    if p.trait == "survivor":
        print("[Survivor] You notice a rock out of place. Underneath is a small stash of money hidden.")
        print("You find $40.")
    enterE()
    
    travel(p, 4)
    print("You travel for 4 days and come to a damaged part of the road.")
    enterE()
    if p.trait == "handy":
        print("[Handyman] You push through the damaged road. Your wagon is bruised but it's nothing you can't fix.")
        print("Your wagon is undamaged.")
        enterE()
    elif p.materials > 0:
        print("[Materials] You lay out some flat wood to allow your wagon to safely cross.")
        print("Your wagon is undamaged.")
        enterE()
    else:
        print("You push through the damaged part of the road. Your wagon gets bruised crossing but is still functional.")
        p.wagon_status == "bruised"
        enterE()
    
    travel(p, 2)
    print("You travel for 2 days and arrive at Cold Pine.")
    coldpine()
    



def bordertown_to_westsaltor():
    print("You have chosen to head to West Saltor.")
    p.location = "bordertown_to_westsaltor"
    enterE()
    
    travel(p, 2)
    print("You travel for 2 days and enter the Great Forest.")
    enterE()
    
    travel(p, 1)
    print("You travel for a day. Your daughter complains of hunger.")
    print("Food: "+p.food)
    print("\n\t1) Give her an extra days worth of food")
    print("\t2) Tell her to tough it out.")
    x = 0
    while x != 1 and x != 2:
        eval(input("Choice: "))
    
    if x == 1:
        print("You give your daughter some food.\t(-1 food)")
        print("She is happier the rest of the day.")
        p.daughter_respect += 1
        enterE()
    
    elif x == 2:
        print("You explain that the family must ration food in order to survive.")
        print("She is sad but understands.")
        enterE()
    
    travel(p, 3)
    print("You travel for 3 days.")
    print("You spend the night camping on a small cliff overlooking a lake.")
    enterE()
    
    
    
    travel(p, 1)
    print("You travel for a day and come to where another road meets with your own.")
    fork_to_westsaltor()
    



def bordertown_to_fortdencepers():
    print("You have chosen to head to Fort Dencepers.")
    p.location = "bordertown_to_fortdencepers"
    enterE()
    
    travel(p, 2)
    print("You travel for 2 days and enter the Great Forest.")
    enterE()
    
    travel(p, 5)
    print("You travel for 5 days and come across another covered wagon traveling the land.")
    print("They seem a friendly bunch. Perhaps you want to travel together.\n")
    print("\t1. Suggest traveling together to Fort Dencepers")
    print("\t2. Greet them and move on")
    x = 0
    while x != 1 and x != 2:
        x = choice()
    
    if x == 2:
        print("You smile and wave as you continue your journey.")
        aid = False
        enterE()
    
    elif x == 1:
        print("You ask the traveling family if they'd like to go to Fort Dencepers with you.")
        print("The father of the family was a soldier in his past life. He says his protection is valuable.")
        print("He's wondering how you are valuable to him.")
        enterE()
        if p.trait == "instinct" and p.check("firearm") == True:
            print("[Instinct + Firearm] You show him your iron and tell him you can watch his back. He recognizes your sharp eye.")
            print("He is willing to travel with you.")
            aid = True
        elif p.trait == "silver":
            print("[Silver Tongue] You tell the man you and your wife and kids are defenseless against any savages that may attack them.")
            print("He looks at you and pities you. He will take you with them.")
            aid = True
            enterE()
        elif p.trait == "survivor" and p.check("map"):
            print("[Survivor + Map] You tell him you are an experienced cartographer. You can help him take a shortcut to Fort Dencepers.")
            print("He is willing to travel with you.")
            aid = True
            enterE()
        elif p.trait == "handy" and p.check("tools") == True:
            print("[Handyman + Tools] You tell him you're experienced fixin' things and can make sure he gets to Fort Dencepers without issue.")
            print("He is willing to travel with you.")
            aid = True
        else:
            if p.check("firearm") == True:
                print("You show him your firearm in an attempt to impress him.")
                print("He laughs. He can tell you've had no real experience with it. Not like he has.")
            else:
                print("You have no obvious use to him.")
                
            print("Pay him $30 for his company?")
            if ask() == True:
                if p.money >= 30:
                    print("You pay him $30 to travel together to Fort Dencepers.")
                    p.money -= 30
                    aid = True
                    enterE()
                else:
                    print("You offer to pay him, but when you reach for your pockets, you lack the money to pay him.")
                    print("He thinks you are stupid for even bringing it up. You continue on your journey embarassed.")
                    p.wife_respect -= 1
                    aid = False
                    enterE()
            else:
                print("You apologize for being useless and continue on your journey.")
                aid = False
                enterE()
    
    
    if aid == True:
        print("You travel with company.")
    travel(p, 4)
    print("You travel for 2 days.")
    print("You have made camp for the night. It is peak nighttime and your family is sleeping.")
    print("You lie awake watching the dim lumination of the moon under the trees.")
    if aid == False:
        print("Your daughter wakes and sees you sitting. She says she's hungry.")
        print("Give daughter some extra food (-1 day of food and water)?")
        print("You have ", p.food, " days of food.", sep='')
        print('')
        if ask() == True:
            print("Your daughter munches the food silently. You stay awake with her and watch the stars.")
            p.food -= 1
            p.daughter_respect += 1
            enterE()
        else:
            print("You shake your head sadly at her plea. You comfort her while watching the sky.")
            enterE()
    else:
        print("Your companions are carrying a lot. If you were quick, you could steal something from them they wouldn't notice.")
        print("On the other hand, the stranger has seen war. His senses are sharp.")
        print("You should only try if yours are too.\n")
        print("\t1. Try to steal from your fellower travelers")
        print("\t2. Go back to sleep")
        x = 0
        while x != 1 and x != 2:
            x = choice()
        
        if x == 2:
            print("You fall back asleep.")
            enterE()
        elif x == 1:
            print("You decide to steal from the strangers you are traveling with.")
            enterE()
            if p.trait == "instinct":
                print("[Instinct] You step lightly over to where your companions have made camp. They are sleeping soundly.")
                print("You search the camp slowly...")
                enterE()
                print("You locate a jewelry box.")
                print("You open it. There are many valuable looking pieces inside.")
                print("You take a smaller, out of the way piece you hope won't be noticed.")
                p.gain("stolen_jewelry")
                enterE()
                print("You return to where you were sleeping undetected.")
                print("Gained stolen jewelry.")
                enterE()
            else:
                print("You attempt to sneak into the camp of your companions. They are sleeping soundly.")
                print("You begin to look through their wagon.")
                enterE()
                print("As you are searching the wagon, you are struck in the back of the head with something hard.")
                print("You fall to the ground and turn to find the father of your companions.")
                print("What you have done is wrong, and there are no prisons. Only justice.")
                print("The stranger deals some when he shoots you.")
                dead()
    
    print("You set out the next morning.")
    
    travel(p, 3)
    print("You travel for 3 days.")
    enterE()
    if aid == True:
        print("You hear a snap of a twig from somewhere in the forest.")
        print("You are nervous for a few moments, but you calm after nothing happens.")
        if p.trait == "instinct":
            print("[Instinct] You have a feeling you just avoided danger although you're not sure how.")
        enterE()
    else:
        print("While you are traveling on the road two men jump out in front of your wagon with firearms.")
        print("They are demanding that you hand over your money.\n")
        print("\t1. Surrender and give over your money.")
        if p.trait == "instinct" and p.check("firearm") and p.ammo > 1:
            print("\t2. [Instinct + Firearm + Ammo] Shoot them both.")
        if p.check("necklace") == True:
            print("\t3. [Necklace] Give over valuable necklace instead.")
        if p.trait == "survivor":
            print("\t4. [Survivor] Savagely murder the men with your bare hands.")
        
        x = 0
        done = False
        while done == False:
            while x < 1 or x > 4:
                x = choice()
            
            if x == 1:
                print("You agree to give the men all of your money.")
                enterE()
                if p.money == 0:
                    print("You go to surrender your money to the men and realize you don't have any.")
                    print("The men laugh at you and walk away.")
                    done = True
                    enterE()
                else:
                    print("They take your money and leave.")
                    p.money = 0
                    done = True
                    enterE()
            
            elif x == 2 and p.trait == "instinct" and p.check("firearm") == True and p.ammo > 1:
                done2 = False
                print("You swiftly pull out your firearm and shoot both of the men before they have a chance to move.")
                print("You strike one man in the head, the other in the gut. They both fall to the ground, the one shot in the gut begins to insult you.")
                print("Blood spews from his mouth when he talks. He says horrible things about your wife and daughter.\n")
                print("\t1) Shoot him in the face.")
                print("\t2) Shoot both of his knees.")
                print("\t3) Stomp on his face.")
                print("\t4) Leave the man to die on the side of the road.")
                y = 0
                while y < 1 or y > 5:
                    y = choice()
                
                if y == 1 and p.ammo > 0:
                    print("You shoot the man in the face. Nothing remains but pieces of skin, skull, and blood.")
                    print("You wipe your boots off in the grass and continue travelling.")
                    p.ammo -= 1
                    done2 = True
                    enterE()
                
                elif y == 2 and p.ammo > 1:
                    print("You shoot the man in both his knees. The insults are replaced with screams of agony.")
                    print("Your family is disturbed by the scene.")
                    p.daughter_respect -= 1
                    p.wife_respect -= 1
                    p.son_respect -= 1
                    p.ammo -= 2
                    done2 = True
                    enterE()
                
                elif y == 3:
                    print("The bottom of your boot meets the man's face. His body slumps and he goes quiet.")
                    done2 = True
                    enterE()
                
                elif y == 4:
                    print("You let him talk as you walk away. The cries of a dying man have no effect on you.")
                    print("You deny him any gradification. Your wife is impressed.")
                    p.wife_respect += 1
                    done2 = True
                    enterE()
                
                done = True
            
            elif x == 3 and p.check("necklace") == True:
                print("You hold up a necklace you found and offer that instead. The men seem content and leave you alone.")
                p.lose("necklace")
                done = True
                enterE()
                
            elif x == 4:
                print("A sound is made behind the men and they turn around for a moment, but the moment is enough.")
                print("You grab one of the men and get behind him. The other man fires at you but only hits his friend.")
                print("You threw the dead man aside and slam the remaining man to the ground. You dig your fingers into his throat and rip out of windpipe.")
                enterE()
                print("The scene is gruesome. Your wife is disturbed.")
                p.wife_respect -= 1
                done = True
                enterE()
    
    
    if p.check("map") == True and p.trait == "survivor":
        if aid == False:
            print("You travel a bit further the same day.")
            print("You spot a shortcut on the map. It looks like it shaves off a few days to Fort Dencepers.")
            enterE()
            travel(p, 2)
            print("You travel for 2 days and arrive at Fort Dencepers.")
            enterE()
        else:
            print("You travel a bit further the same day.")
            print("You find the shortcut you mentioned to your companions and point it out . You take it with them.")
            enterE()
            travel(p, 2)
            print("You travel for 2 days and arrive at Fort Dencepers")
            enterE()
    else:
        travel(p, 5)
        print("You travel for 5 days and arrive at Fort Dencepers.")
        enterE()
    
    if aid == True:
        print("You shake hands with the family you traveled with and part ways.")
        enterE()

    fortd()
    
            




#BORDERTOWN
def borderTown():
    p.location = "bordertown"
    
    savegame(p)
        
    print("You arrive at Bordertown. It is slightly smaller than Corfield.")
    print("This city borders the wild land to the west. There are three roads leaving here.")
    
    enterE()
    print("TUTORIAL: When you come to a town, you will have the option to read road signs.")
    print("The signs will tell you which towns branch from your location and how far they are away.")
    print("The locals will also share their views on towns, but most people aren't well-travelled and their views are skewed.")
    print("When you are ready to leave town, you will decide your next destination.")
    print("Remember your ultimate goal is to find a place for you to settle permanantly. Your trait will determine the locations available to you.")
    print("Good Luck.")
    enterE()
    
    print("You decide to spend two weeks in Bordertown working.")
    if p.trait == "silver":
        print("[Silver Tongue] You work at the local tavern as a stand in for the local barkeep.")
        print("You get paid $220 for your trouble.")
        p.money += 220
    elif p.trait == "handy":
        print("[Handyman] The local government hired you to help maintain their building.")
        print("You were paid $180")
        p.money += 180
    else:
        print("You are asked to help maintain the town roads.")
        print("You are paid $150 for the work.")
        p.money+= 150
    print("Your job covered food for you and your family.")
    enterE()
    
    p.day += 14
    print("It is now two weeks later.")
    enterE()
    if p.hungryman_helped == False:
        print("A traveler passing through asks you if you saw the man who starved to death outside of Corfield.")
    print("The doctor is in here at Bordertown.")
    enterE()
    
    x = 0
    while x != 6:
        print("\nYou are in Bordertown.")
        hud(p)
        print("Day: ", p.day)
        print('')
        print("ACTIONS: ")
        print("\t1. Read road signs")
        print("\t2. Visit Store")
        print("\t3. Sell items")
        print("\t4. Visit doctor")
        print("\t5. Check on family")
        print("\t6. Leave Bordertown")
        
        x = 0
        while x > 6 or x < 1:
            x = choice()
        
        if x == 1:
            print("The road to the northwest leads to Cold Pine. It is an 18 day journey.")
            print("The locals say the land north beyond Cold Pines is cold and unforgiving, but the path to Cold Pines is temparate enough.\n")
            
            print("Straight to the west is West Saltor. It is a 31 day journey.")
            print("The locals say the forest to the west has lots of diverse wildlife.")
            print("The road is long but a skilled hunter or fisherman could make the journey easily.\n")
            
            print("To the southwest is Fort Dencepers. It is a 19 day journey.")
            print("The locals say it's a town built around the protection of the fort.")
            print("Savages own the land to the south so you may run into some traveling down there.\n")
            
            print("The locals tell you the road to Cold Pines is safer than the ones to West Saltor and Fort Dencepers.\n")
            
            enterE()
        
        elif x == 2:
            y = 0
            while y != 11:
                print("SHOP:")
                print("1. Tools: $50")
                print("2. 1 day of food and water: $5")
                print("3. Firearm: $100")
                print("4. Ammo: $10")
                print("5. Map of the Region: $20")
                print("6. Spare Materials: $30")
                print("7. Extra Ox $100")
                print("8. Fishing Pole $20")
                print("9. Almanac $90")
                print("10. Warm clothes $95")
                print("11. Leave Store")
                hud(p)
                y = choice()
            
                if y == 1:
                    if p.check("tools") == False:
                        if p.money >= 50:
                            p.money -= 50
                            p.gain("tools")
                            print("Tools bought successfully.")
                            enterE()
                    else:
                        print("You already have tools.")
                        enterE()
                elif y == 2:
                    z = eval(input("How many days of food would you like to buy?: "))
                    if (z * 5) > p.money:
                        print("You don't have enough money for that much food.")
                        enterE()
                    else:
                        p.money -= (z * 5)
                        p.food += z
                        print("Bought ", z, " days of food.", sep='')
                        enterE()
                elif y == 3:
                    if p.check("firearm") == False:
                        if p.money >= 100:
                            p.money -= 100
                            p.gain("firearm")
                            print("Firearm bought successfully.")
                            enterE()
                        else:
                            print("Not enought money.")
                            enterE()
                    else:
                        print("You already own a firearm.")
                        enterE()
                elif y == 4:
                    y = eval(input("How much ammo would you like? (1-3 recommended): "))
                    if y * 10 > p.money:
                        print("Not enough money.")
                        enterE()
                    else:
                        p.money -= y * 10
                        p.ammo += y
                        print("Bought ammo successfully.")
                        enterE()
                elif y == 5:
                    if p.check("map") == False:
                        if p.money >= 20:
                            p.money -= 20
                            p.gain("map")
                            print("Map bought.")
                            enterE()
                        else:
                            print("Not enough money")
                            enterE()
                    else:
                        print("You already own the map.")
                        enterE()
                elif y == 6:
                    if p.money >= 30:
                        p.money -= 30
                        p.materials += 1
                        print("Bought spare materials.")
                        enterE()
                    else:
                        print("Not enough money.")
                        enterE()
                elif y == 7:
                    if p.oxen == 3:
                        print("Max oxen achieved already.")
                        enterE()
                    else:
                        if p.money >= 100:
                            p.money -= 100
                            p.oxen += 1
                            print("Ox bought.")
                            enterE()
                        else:
                            print("Not enough money")
                            enterE()
                elif y == 8:
                    if p.check("pole") == False and p.money > 20:
                        print("Bought fishing pole.")
                        p.money -= 20
                        p.gain("pole")
                        enterE()
                    else:
                        print("Can't buy because you either don't have enough money or you own one already.")
                        enterE()
                elif y == 9:
                    if p.check("almanac") == False and p.money > 90:
                        print("almanac bought.")
                        p.money -= 90
                        p.gain("almanac")
                        enterE()
                    else:
                        print("Not enough money or already own.")
                elif y == 10:
                    if p.check("warm_clothes") == False and p.money > 95:
                        print("Warm clothes bought.")
                        p.money -= 95
                        p.gain("warm_clothes")
                    
                    
        elif x == 3:
            p.money += sellItems(p)
        
        elif x == 4:
            doctors(p)

        elif x == 5:
            checkFamily(p)
        
        elif x == 6:
            if foodCheck(p) == True:
                z = 0
                print("Which path are you taking out of Bordertown?\n")
                print("\t1. Travel northwest to Cold Pine")
                print("\t2. Travel west to West Saltor")
                print("\t3. Travel southwest to Fort Dencepers")
                while z != 1 and z != 2 and z != 3:
                    z = choice()
                
                if z == 1:
                    bordertown_to_coldpine()
                
                elif z == 2:
                    bordertown_to_westsaltor()
                
                elif z == 3:
                    bordertown_to_fortdencepers()
                
            else:
                x = 0


def tutorial():
    #game start and trait picking
    repairman_Killed = False

    print("You are a man who has come to Acirema with your wife, son, and daughter in hopes of a better life.")
    print("Your goal is to find a town to settle in to live out your days.")
    print('')
    enterE()

    print("Choose a trait below by entering a number and pressing enter.")
    print("Your trait will determine how a number of encounters go, and which locations will be available for settling.\n")

    print("1. Good Instincts: Your senses are sharp and will rarely fail you. You also trust your gut as it warns you of danger reliably.")
    print("2. Handyman: You grew up on a farm and know your way around tools. You have the knowledge to repair most things and have an inventive nature.")
    print("3. Silver Tongue: You are a natural at moving others. Many are weary of strangers, but you make others feel comfortable. You also get more money when you sell items.")
    print("4. Survivor: You have a connection to the natural. Animals and the world they live in are like second nature to you.")
    x = choice()
    while x > 4 and x < 1:
        print("Invalid choice. Choose between 1 and 4.")
        x = choice()

    if x == 1:
        p.trait = "instinct"
    elif x == 2:
        p.trait = "handy"
    elif x == 3:
        p.trait = "silver"
    elif x == 4:
        p.trait = "survivor"

    print("You have choosen ", p.trait, ".", sep='')
    enterE()


    print("You cross the border into Acirema with a small group of settlers. The land here is a large valley coning the path forward.")
    print("Settlers you travel with inform you this area of Acirema is known as The Green Mile.")
    print("There is a straight line of settlements leading to the central part of the land. You are told your path will branch at Bordertown.")
    print("Your first goal should be to reach there.")
    enterE()





    #BAYCOAST
    print("You have just arrived in Baycoast. After purchasing your covered wagon and your ox you have $" + str(STARTING_CASH) + ".")
    print("It is a 17 day journey to Westmount. The locals say the area is relatively safe.")
    enterE()
    if p.trait == "survivor":
        print("[Survivor] You approach a man you can tell is well travelled. You ask him about the road and he tells you")
        print("there's a bridge that crosses a river that is destroyed, but if you head north a few miles you can cross")
        print("a shallow point safely.")
        enterE()

    

    print("TUTORIAL: You will now enter the shop. Here you will buy items for your journey to Westmount.")
    print("To buy items, enter the number of your selection and press enter.")
    print("Make your choices wisely. You do not know when you will earn your next dollar.")
    print("Hint: ALWAYS BUY MORE FOOD THAN YOU THINK YOU'LL NEED")
    enterE()

    while x != 9:
        print("SHOP:")
        print("1. Tools: $50")
        print("2. 1 day of food and water: $5")
        print("3. Firearm: $100")
        print("4. Ammo: $10")
        print("5. Map of the Region: $20")
        print("6. Spare Materials: $30")
        print("7. Another ox: $100")
        print("8. [Silver Tongue] Tools and Gun: $110")
        print("9. Leave to Westmount")
        print("---------------")
        hud(p)
        x = choice()
        
        if x == 1:
            if p.check("tools") == False:
                if p.money >= 50:
                    p.money -= 50
                    p.gain("tools")
                    print("Tools bought successfully.")
                    enterE()
            else:
                print("You already have tools.")
                enterE()
                
        elif x == 2:
            y = eval(input("How many days of food would you like to buy?: "))
            if (y * 5) > p.money:
                print("You don't have enough money for that much food.")
                enterE()
            else:
                p.money -= (y * 5)
                p.food += y
                print("Bought ", y, " days of food.", sep='')
                enterE()
        
        elif x == 3:
            if p.check("firearm") == False:
                if p.money >= 100:
                    p.money -= 100
                    p.gain("firearm")
                    print("Firearm bought successfully.")
                    enterE()
                else:
                    print("Not enought money.")
                    enterE()
            else:
                print("You already own a firearm.")
                enterE()
        
        elif x == 4:
            y = eval(input("How much ammo would you like? (1-3 recommended): "))
            if y * 10 > p.money:
                print("Not enough money.")
                enterE()
            else:
                p.money -= y * 10
                p.ammo += y
                print("Bought ammo successfully.")
                enterE()
        
        elif x == 5:
            if p.check("map") == False:
                if p.money >= 20:
                    p.money -= 20
                    p.gain("map")
                    print("Map bought.")
                    enterE()
                else:
                    print("Not enough money")
                    enterE()
            else:
                print("You already own the map.")
                enterE()
        
        elif x == 6:
            if p.money >= 30:
                p.money -= 30
                p.materials += 1
                print("Bought spare materials.")
                enterE()
            else:
                print("Not enough money.")
                enterE()
        
        elif x == 7:
            if p.oxen == 3:
                print("Max oxen achieved already.")
                enterE()
            else:
                if p.money >= 100:
                    p.money -= 100
                    p.oxen += 1
                    print("Ox bought.")
                    enterE()
                else:
                    print("Not enough money")
                    enterE()
        
        elif x == 8:
            if p.trait != "silver":
                print("You do not have a silver tongue.")
                enterE()
            else:
                if p.money >= 110:
                    p.money -= 110
                    p.gain("firearm")
                    p.gain("tools")
                    print("Special deal bought.")
                    enterE()
        
        elif x == 9:
            if foodCheck(p) == True:
                print("Leaving Baycoast...")
                enterE()
            else:
                x = 0
        
        else:
            print("Invalid input.")
            enterE()

    #end of Baycoast









    #ROAD TO WESTMOUNT
    print("Traveling!")
    for x in range(5):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()

    print("You travel for five days.")
    enterE()
    print("You come to a bridge that used to cross a large river, but has been recently destroyed.")
    print("The water is too deep to ford. You cannot cross here.")
    print("You will have to travel north or south along the river.")
    if p.check("map") == True:
        print("[Map] The map shows a bridge far to the south.")
    print("")
    print("\t1. Travel North")
    print("\t2. Travel South")
    x = 0
    while x != 1 and x != 2:
        x = choice()

    if x == 1:
        print("You travel north for half a day and find a shallow point in the river.")
        print("You cross it with ease and head back to the trail.")
        p.day += 1
        p.food -= 1

    elif x == 2:
        print("You travel south for a day.")
        p.day += 1
        p.food -= 1
        enterE()
        print("You find a part of the river that isn't as deep as the other parts, but still uncomfortably deep.")
        print("You can try to ford it here, or you can keep travelling south to find a better spot.")
        if p.check("map") == True:
            print("[Map] The map shows a bridge far to the south.")
        elif p.trait == "instinct":
            print("[Instinct] My gut says I should keep looking.")
        print("\t1. Keep travelling south")
        print("\t2. Attempt to ford river here")
        y = 0
        while y != 1 and y != 2:
            y = choice()
        
        if y == 1:
            print("You travel south for another day.")
            enterE()
            print("You find another bridge across the river. You cross it.")
            print("It takes you 2 days to return to your original path.")
            p.day += 3
            p.food -= 3
            enterE()
        elif y == 2:
            print("You attempt to ford the river.")
            print("You enter the river and cross the middle with relative ease.")
            if p.oxen > 1:
                print("[2+ oxen] When you approach the steep river bank, your oxen are able to pull your wagon up with ease.")
                enterE()
            elif p.trait == "handy":
                print("Your single ox struggles to pull your cart up the steep river bank.")
                print("[Handyman] You makeshift a lever with a piece of your wagon and you and your son help lift the wagon")
                print("out of the water.")
            else:
                print("Your single ox struggles to pull your cart up the steep river bank.")
                print("The wagon comes splashing back down as your ox loses it's balance trying to lift it out.")
                print("You and your family help push the wagon up the slope this time and successfully get it out of the river.")
                enterE()
                print("Your wagon has been damaged. You need someone to fix it.")
                print("A passerby on horseback who saw you ford the river says he'll get help from Westmount.")
                print("Help arrives the next day.")
                p.day -= 1
                p.food -= 1
                enterE()
                print("A man arrives to help fix your wagon. He does the job in a few hours.")
                print("He charges $40 for the service.")
                print("Money: $", p.money, sep='')
                if p.money >= 40:
                    print("\t1. Pay him $40")
                if p.check("tools") == True:
                    print("\t2. Trade tools for the service.")
                if p.check("firearm") == True:
                    print("\t3. Trade firearm for service.")
                    if p.ammo > 0:
                        print("\t4. Shoot the man and throw his body in the river.")
                        if p.trait == "instinct":
                            print("[Instinct] Your gut says shooting him is a bad idea.")
                print("\t5. Admit you can't pay him.")
                done = False
                
                while done == False:
                    z = 0
                    while z > 5 or z < 1:
                        z = choice()
                    if z == 1:
                        if p.money >= 40:
                            p.money -= 40
                            print("You pay the man and continue your journey.")
                            done = True
                    elif z == 2:
                        if p.check("tools") == True:
                            p.lose("tools")
                            print("You traded your tools for his service.")
                            done = True
                    elif p.check("firearm") == True:
                        if z == 3:
                            p.lose("firearm")
                            print("You traded your firearm for his service.")
                            done = True
                        elif z == 4:
                            if p.ammo > 0:
                                print("You shoot the man and dump his body into the river.")
                                print("Your wife panics, as she witnessed the event. She may never look at you the same again.")
                                p.wife_respect -= 3
                                print("Your children are scared by the shot of the gun. Although your wife lies to calm")
                                print("them down, your son is unconvinced that nothing happened.")
                                p.son_respect -= 2
                                repairman_Killed = True
                                done = True
                    elif z == 5:
                        print("You offer the man your food and your ox, but he does not want either one.")
                        print("He becomes angry. He is a very large man and you are unsure of what to do.")
                        print("You offer to let him sleep with your wife. He accepts and relucantly, so does she.")
                        print("After she's done. Your wife gets into the covered wagon silently. She may never look at you the same again.")
                        p.wife_respect -= 5
                        done = True
                
                print("It takes two days to return to the path.")
                p.day -= 2
                p.food -= 2
                enterE()

    print("Traveling...")
    for x in range(4):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()

    print("You travel for 4 days.")
    enterE()
    print("While exploring, your son finds a stash box hidden near the side of the road in a tree.")
    print("He gives it to you. Inside is $120.")
    print("Finders keepers.")
    p.money += 120
    enterE()


    print("Traveling...")
    for x in range(6):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()




    #WESTMOUNT
    print("You travel for 6 days and arrive at Westmount.")
    p.location = "westmount"
    enterE()
    print("You are headed to Corfield next. The journey is 20 days long.")
    print("The locals also mentioned that the wildlife on the journey are more active.")
    enterE()

    if p.trait == "silver":
        print("[Silver Tongue] You talk up a man sitting outside the post office. He claims there's a newer road")
        print("that was built recently that takes a shorter route to Corfield. He talks of a fork in the road, but")
        print("he did not know which path was the shorter one.")
        enterE()
    elif p.trait == "handy":
        print("[Handyman] A man approaches you asking if you can help him fix his house.")
        print("With some tools and spare materials you could do it.")
        enterE()
        
    x = 0
    done = False

    while x != 2:
        print("Day: ", p.day)
        hud(p)
        print("Actions: ")
        print("\t1. Visit store")
        print("\t2. Leave Westmount")
        if p.trait == "handy" and p.check("tools") == True and p.materials > 0 and done == False:
            print("\t3. [Handyman] Do house job for $90")
        
        x = 0
        y = 0
        while x > 3 or x < 1:
            x = choice()
        
        if x == 1:
            while y != 7:
                print("SHOP:")
                print("1. Tools: $50")
                print("2. 1 day of food and water: $5")
                print("3. Firearm: $100")
                print("4. Ammo: $10")
                print("5. Map of the Region: $20")
                print("6. Spare Materials: $30")
                print("7. Leave Store")
                hud(p)
                y = choice()
                
                if y == 1:
                    if p.check("tools") == False:
                        if p.money >= 50:
                            p.money -= 50
                            p.gain("tools")
                            print("Tools bought successfully.")
                            enterE()
                    else:
                        print("You already have tools.")
                        enterE()
                elif y == 2:
                    z = eval(input("How many days of food would you like to buy?: "))
                    if (z * 5) > p.money:
                        print("You don't have enough money for that much food.")
                        enterE()
                    else:
                        p.money -= (z * 5)
                        p.food += z
                        print("Bought ", z, " days of food.", sep='')
                        enterE()
                elif y == 3:
                    if p.check("firearm") == False:
                        if p.money >= 100:
                            p.money -= 100
                            p.gain("firearm")
                            print("Firearm bought successfully.")
                            enterE()
                        else:
                            print("Not enought money.")
                            enterE()
                    else:
                        print("You already own a firearm.")
                        enterE()
                elif y == 4:
                    y = eval(input("How much ammo would you like? (1-3 recommended): "))
                    if y * 10 > p.money:
                        print("Not enough money.")
                        enterE()
                    else:
                        p.money -= y * 10
                        p.ammo += y
                        print("Bought ammo successfully.")
                        enterE()
                elif y == 5:
                    if p.check("map") == False:
                        if p.money >= 20:
                            p.money -= 20
                            p.gain("map")
                            print("Map bought.")
                            enterE()
                        else:
                            print("Not enough money")
                            enterE()
                    else:
                        print("You already own the map.")
                        enterE()
                elif y == 6:
                    if p.money >= 30:
                        p.money -= 30
                        p.materials += 1
                        print("Bought spare materials.")
                        enterE()
                    else:
                        print("Not enough money.")
                        enterE()
        elif x == 3 and done == False:
            if p.trait == "handy" and p.check("tools") == True and p.materials >= 1:
                print("You've done the job for the man. It only took a couple of hours.")
                print("You've been paid $90.")
                print("You used up one spare materials.")
                p.materials -= 1
                p.money += 90
                done = True
                enterE()
            else:
                print("You lack necessary items.")
                enterE()
        
        elif x == 2:
            if foodCheck(p) == True:
                print("Leaving Westmount...")
                enterE()
            else:
                x = 0

    #end of Westmount







    #Road to Corfield
    print("Traveling...")
    for x in range(3):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()

    if p.trait == "instinct":
        enterE()
        print("You travel for three days.")
        print("[Instinct] While you are stopped to take a leak, you spot hollowed out tree.")
        print("Inside is $60.")
        p.money += 60
        print("You take the money and continue on your way.")
        enterE()
        print("Traveling...")

    for x in range(4):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()


    x = 0
    if p.trait == "instinct":
        print("You have traveled for 4 days.")
    else:
        print("You have traveled for 7 days.")
    enterE()

    print("There is a fork in the road.")
    if p.trait == "instinct":
        if p.ammo == 0 or p.check("firearm") == False:
            print("[Instinct] My gut says to take the left path.")
    if p.check("map") == True:
        print("[Map]: The map shows that the right path is shorter.")
    if p.trait == "survivor":
        print("[Survivor] Scouting the paths a bit, you can tell the right path has more animal activity.")
    print('')
    print("\t1. Take left path")
    print("\t2. Take right path")
    while x != 1 and x != 2:
        x = choice()

    if x == 1:
        print("You travel down the left path.")
        enterE()
        print("Traveling...")
        for x in range(10):
            p.day += 1
            p.food -= 1
        if p.food < 0:
            noFood()
        enterE()
        print("You travel for 7 days and come to where the path meets with the other.")

    elif x == 2:
        print("You go down the right path and travel for a day.")
        p.day += 1
        p.food -= 1
        enterE()
        print("While you are travelling you run into a bear. It gets aggressive when it sees you.\n")
        saved = False
        if p.check("firearm") == True and p.ammo > 0:
            print("\t1. [Firearm] Shoot the bear.")
            saved = True
        if p.check("tools") == True and p.trait == "survivor":
            print("\t2. [Survivor + Tools] Kill the bear using some tools.")
            saved = True
        if p.oxen > 1:
            print("\t3. [2+ oxen] Sacrfice an ox.")
            saved = True
        if p.trait == "instinct":
            print("\t4. [Instinct] Attack the bear in it's weakpoint.")
        y = 0
        done = False
        while done == False:
            while y > 3 or y < 1 and saved == True:
                y = choice()
        
            if y == 1 and p.check("firearm") == True and p.ammo > 0:
                print("You shoot the bear.")
                enterE()
                print("The bear is killed. You and your son load it into your covered wagon.")
                p.son_respect += 1
                p.ammo -= 1
                p.gain("bear_corpse")
                done = True
                enterE()
        
            elif y == 2 and p.check("tools") == True and p.trait == "survivor":
                print("You attack the bear with a hammer. You psycho.")
                enterE()
                print("You smash the bear's head in.")
                print("The bear is killed. You lift the bear up and toss it in the covered wagon.")
                print("Your entire family is impressed.")
                p.son_respect += 1
                p.daughter_respect += 1
                p.wife_respect += 1
                p.gain("bear_corpse")
                done = True
                enterE()
        
            elif y == 3 and p.oxen > 1:
                print("[2+ oxen] You let an ox loose to get away from the bear.")
                p.oxen -= 1
                print("Your son takes note of your quick thinking.")
                p.son_respect += 1
                enterE()
            
            elif y == 4:
                print("You attack the bear at it's neck and eyes. You claw out it's eyes and chase it away.")
                print("Your entire family is impressed.")
                p.son_respect += 1
                p.daughter_respect += 1
                p.wife_respect += 1
                p.gain("bear_corpse")
                done = True
                enterE()
        
            if saved == False:
                if p.check("tools") == True:
                    print("You attack the bear with your tools but to no avail. It mauls you.")
                    dead()
                if p.check("gun") == True:
                    print("Having a gun but no bullets, you whack the bear with your gun.")
                    print("It whacks you back with it's claws.")
                    dead()
                else:
                    print("Having nothing to defend yourself with, the bear mauls you with ease.")
                    dead()

        print("You come to where the road meets itself after one day of traveling.")
        p.day += 1
        p.food -= 1
        
    print("Traveling...")
    for x in range(3):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()

    print("You travel for 3 days.")
    print("You come across a grave in the ground.")
    print("It looks semi-recent. It was probably dug in the last year.")
    if p.trait == "instinct":
        print("[Instinct] I can probably get away with this.")
    print('')
    print("\t1. [Tools] Dig up the grave")
    print("\t2. Leave the grave alone.")

    x = 0
    while x != 1 and x != 2:
        x = choice()
        if x == 1 and p.check("tools") == False:
            print("You have nothing to dig up the grave with.")
            x = 0

    if x == 2:
        print("You continue on your journey.")

    elif x == 1:
        print("You begin to dig up the grave.")
        enterE()
        print("Your spade hits a wood casket. You open it.")
        print("Inside is what appears to be the remains of a young woman.")
        print("Although it's hard to tell, shes decayed quite alot.")
        print("There is a nice looking necklace around her neck.\n")
        print("\t1. Take the necklace")
        print("\t2. Leave the grave alone")
        y = 0
        while y != 1 and y != 2:
            y = choice()
        
        if y == 1:
            print("You take the necklace. Your son witnesses the act but says nothing.")
            p.son_respect -= 1
            p.gain("necklace")
        
        print("You fill in the grave and be on your way.")
        enterE()

    print("Traveling...")
    for x in range(1):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()







    #CORFIELD
    print("You travel for one more day and arrive in Corfield.")
    p.location = "corfield"
    enterE()
    if repairman_Killed == True:
        print("A man approaches you. He asks if you know anything about John Custer.")
        print("You shake your head, not knowing.")
        print("'Oh,' he says, 'because he was on his way to help fix your wagon, but nobody has seen him since.'")
        print("Damn.\n")
        enterE()
        if p.trait == "silver":
            print("[Silver Tongue] You lie and insist you don't know the man.")
            print("The man sees good nature in you and apologizes for the trouble.")
            enterE()
        else:
            print("You attempt to lie to the man, claiming you don't know what happened to him after his repair.")
            print("He doesn't believe you. He hauls you back to Westmound to be executed.")
            print("The fate of your family is unknown.")
            dead()

    print("This town is much larger than the previous visited.")
    print("You could spend a few days here looking for work.")
    if p.trait == "instinct" and p.check("necklace") == True:
        print("[Instinct] I don't think I should sell the necklace here.")

    enterE()
    x = 0
    done = False
    while x != 3:
        x = 0
        print("\nIt is an 18 day journey to Bordertown.")
        hud(p)
        print("Day: ", p.day)
        print('')
        if done == False:
            print("\t1. Spend 5 days working.")
        print ("\t2. Visit store")
        print("\t3. Leave Corfield")
        print("\t4. Sell items")
        print("\t5. Check on family")
        if p.check("necklace") == True:
            print("\t6. [Necklace] Try to pawn necklace from grave.")
        while x > 5 or x < 1:
            x = choice()
        
        if x == 1 and done == False:
            print("Working...")
            p.day += 5
            
            if p.trait == "handy":
                print("[Handyman] Some of the local ranchers could use a hand with their equipment.")
                print("They'll provide food and materials. You just have to work.")
                print("You've been paid $100.")
                p.money += 100
                enterE()
            elif p.trait == "survivor":
                print("[Survivor] You've helped the local butcher skin game.")
                print("He pays you $75.")
                p.money += 75
                enterE()
            else:
                print("You offer to help carry water.")
                print("You've been paid $50.")
                p.money += 50
                enterE()
            
            if p.son_respect >= 4:
                print("Your son approaches you with a smile on his face. He has been working for the local post office.")
                print("He hands you $15 to help pay expenses.")
                p.money += 15
                enterE()
            
            done = True
        
        elif x == 2:
            y = 0
            while y != 9:
                print("SHOP:")
                print("1. Tools: $50")
                print("2. 1 day of food and water: $5")
                print("3. Firearm: $100")
                print("4. Ammo: $10")
                print("5. Map of the Region: $20")
                print("6. Spare Materials: $30")
                print("7. Extra Ox $100")
                print("8. Fishing Pole $20")
                print("9. Leave Store")
                hud(p)
                y = choice()
                
                if y == 1:
                    if p.check("tools") == False:
                        if p.money >= 50:
                            p.money -= 50
                            p.gain("tools")
                            print("Tools bought successfully.")
                            enterE()
                    else:
                        print("You already have tools.")
                        enterE()
                elif y == 2:
                    z = eval(input("How many days of food would you like to buy?: "))
                    if (z * 5) > p.money:
                        print("You don't have enough money for that much food.")
                        enterE()
                    else:
                        p.money -= (z * 5)
                        p.food += z
                        print("Bought ", z, " days of food.", sep='')
                        enterE()
                elif y == 3:
                    if p.check("firearm") == False:
                        if p.money >= 100:
                            p.money -= 100
                            p.gain("firearm")
                            print("Firearm bought successfully.")
                            enterE()
                        else:
                            print("Not enought money.")
                            enterE()
                    else:
                        print("You already own a firearm.")
                        enterE()
                elif y == 4:
                    y = eval(input("How much ammo would you like? (1-3 recommended): "))
                    if y * 10 > p.money:
                        print("Not enough money.")
                        enterE()
                    else:
                        p.money -= y * 10
                        p.ammo += y
                        print("Bought ammo successfully.")
                        enterE()
                elif y == 5:
                    if p.check("map") == False:
                        if p.money >= 20:
                            p.money -= 20
                            p.gain("map")
                            print("Map bought.")
                            enterE()
                        else:
                            print("Not enough money")
                            enterE()
                    else:
                        print("You already own the map.")
                        enterE()
                elif y == 6:
                    if p.money >= 30:
                        p.money -= 30
                        p.materials += 1
                        print("Bought spare materials.")
                        enterE()
                    else:
                        print("Not enough money.")
                        enterE()
                elif y == 7:
                    if p.oxen == 3:
                        print("Max oxen achieved already.")
                        enterE()
                    else:
                        if p.money >= 100:
                            p.money -= 100
                            p.oxen += 1
                            print("Ox bought.")
                            enterE()
                        else:
                            print("Not enough money")
                            enterE()
                elif y == 8:
                    if p.check("pole") == False and p.money > 20:
                        print("Bought fishing pole.")
                        p.money -= 20
                        p.gain("pole")
                        enterE()
                    else:
                        print("Can't buy because you either don't have enough money or you own one already.")
                        enterE()
        
        elif x == 6 and p.check("necklace") == True:
            print("You try to pawn the necklace in town.")
            enterE()
            print("You enter the local store to pawn the necklace.")
            print("The store owner recognizes the necklace as belonging to the daughter of another townsperson who passed recently.")
            print("He knows you took it from her grave. He is disguested by your actions.")
            print("You try to flee before he sounds the alarm, but it's too late.")
            print("The town executes you for your horrible crime.")
            dead()
        
        elif x == 4:
            p.money += sellItems(p)
        
        elif x == 5:
            checkFamily(p)
        
        elif x == 3:
            if foodCheck(p) == True:
                print("Leaving Corfield...")
                enterE()
            else:
                x = 0

    #end of Corfield







    #Road to Bordertown
    print("Traveling...")
    for x in range(2):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()

    print("You travel for 2 days and come across a man on the verge of starving to death.\n")
    print("You have ", p.food, " days of food.\n", sep='')
    print("\t1. Give him 2 days worth of food")
    print("\t2. Say a prayer to him and leave him be.")
    x = 0
    while x != 1 and x != 2:
        x = choice()

    if x == 1:
        print("You give him some of your food. He thanks you with tears in his eyes.")
        print("Your family respects the gesture.")
        p.son_respect += 1
        p.wife_respect += 1
        p.daughter_respect += 1
        p.hungryman_helped = True
        enterE()

    elif x == 2:
        print("You hope for the best for the man as you continue onward.")
        enterE()

    print("Traveling...")
    for x in range(3):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()

    print("You travel for three days.")
    enterE()
    print("When you wake the next day and prepare to set out, it begins to rain heavily.")
    print("You could wait for this to blow over, but who knows how long that could take?")
    if p.trait == "survivor":
        print("[Survivor] The storm should blow over in a couple days.")
    print('')
    print("You have ", p.food, " days of food.\n", sep='')
    print("\t1. Wait for the storm to end.")
    print("\t2. Push through the storm.")
    x = 0
    while x != 1 and x != 2:
        x = choice()

    if x == 1:
        print("Waiting for storm to clear...")
        for x in range(2):
            p.day += 1
            p.food -= 1
            if p.food < 0:
                noFood()
        enterE()
        
        print("While waiting for the storm to clear a wolf approaches your covered wagon.")
        print("Your daughter whimpers when it approaches and the wolf turns it's head to look inside.")
        print("It is right outside the back of the covered wagon.\n")
        if p.check("firearm") == True and p.ammo >= 1:
            print("\t1. [Firearm] Shoot the wolf")
        print("\t2. Shoo the wolf off and kick it.")
        print("\t3. Offer the wolf some food from your supply.")
        y = 0
        done = False
        while done == False:
            y = 0
            while y > 3 or y < 1:
                y = choice()
        
            if y == 1 and p.check("firearm") == True and p.ammo >= 1:
                print("You shoot the wolf and load it into your wagon.")
                p.gain("wolf corpose")
                p.ammo -= 1
                enterE()
                done = True
            
            elif y == 2:
                print("You shoo the wolf away by kicking it's throat. It leaves you alone.")
                done = True
                enterE()
            
            elif y == 3:
                print("You offer the wolf food from your supply. It eats it and leaves.")
                enterE()
                print("The wolf returns soon after with 2 other wolves.")
                enterE()
                if p.ammo > 3 and p.check("firearm") == True:
                    print("[Firearm + Ammo] You are forced to shoot all three wolves.")
                    print("One of them bites your son in the action. He is hurt badly but you can stablize him with what you have.")
                    print("Hopefully the doctor is in at the next town.")
                    p.ammo -= 3
                    p.son_status = "bitten"
                    done = True
                    enterE()
                else:
                    if p.ammo >= 1 and p.check("firearm") == True:
                        print("You manage to shoot at the wolves but you lack the ammo to kill them all.")
                        print("You and your family are mauled in the storm.")
                        dead()
                    else:
                        print("With no protection against them, the wolves maul you and your family.")
                        dead()

    if x == 2:
        print("You decide to push through the storm")
        enterE()
        print("You approach a long downhill portion of the path.")
        if p.oxen >= 2:
            print("[2+ oxen] With multiple oxen, they bring your wagon down the slope with ease.")
            enterE()
        elif p.trait == "handy" and p.materials > 0:
            print("[Handyman + Materials] Using your inventive nature, you makeshift a brake to help slow the decent.")
            print("You've used up 1 spare materials.")
            p.materials -= 1
            enterE()
        elif p.check("map") == True:
            print("[Map] Looking at the map, you see another path back where you came.")
            print("You take the other path and continue on your way.")
            enterE()
        else:
            print("You and your son must help your single ox bring the wagon slowly downhill.")
            print("Your son complains about the cold but he helps you.")
            print("You get down the hill relatively easy. Your son is shivering when he gets back into the covered wagon.")
            p.son_status = "unnoticeably_sick"
            enterE()

    print("Traveling...")
    for x in range(6):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()

    print("You travel for 6 days. You find a man on the side of the road with a dead ox. His cart is damaged.")
    print("He desparately wants to get Bordertown and he needs an ox. He's willing to pay a handsome fee.")
    print("He also is willing to buy spare materials off of you.\n")
    print("\t1. Apologize for being unable to help.")
    if p.oxen > 1:
        print("\t2. [Spare ox] Sell him an ox for $220")
    if p.materials > 0:
        print("\t3. [Materials] Offload materials for $70")
    if p.trait == "handy":
        print("\t4. [Handyman] His wagon looks real bad. You could repair his wagon for him if you had the tools and 2 spare materials.")
    if p.oxen > 1 and p.materials > 0:
        print("\t5. Give both spare ox and materials for $300")
    x = 0
    done = False
    while done == False:
        while x != 1 and x != 2 and x != 3 and x != 4 and x != 5:
            x = choice()
        
        if x == 1:
            print("You continue on your journey.")
            done = True
            enterE()
        elif x == 2 and p.oxen > 1:
            print("You sell the man your ox and continue on your way.")
            p.oxen -= 1
            p.money += 220
            done = True
            enterE()
        elif x == 3 and p.materials > 0:
            print("You give the man some spare materials and continue on your way.\t(-1 Material, +$70)")
            p.materials -= 1
            p.money += 70
            done = True
            enterE()
        elif x == 4 and p.trait == "handy" and p.materials > 1 and p.check("tools") == True:
            print("You put your hand on his shoulder and tell him not to worry, you can fix it.")
            print("He looks at you strange but let's you fix his wagon.")
            enterE()
            print("You've fixed his wagon. He is greatful.")
            print("You've been paid $150")
            p.money += 150
            p.materials -= 2
            done = True
            enterE()
            
        elif x == 5 and p.oxen > 1 and p.materials > 0:
            print("You sell a spare ox and offload materials. The man is exetremely greatful.")
            print("You were paid $320. You continue on your way.")
            p.money += 320
            p.materials -= 1
            p.oxen -= 1
            done = True
            enterE()

    print("Traveling...")
    for x in range(4):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()

    print("You travel for 4 days and come across a homestead.")
    enterE()
    print("The people living there are friendly. As you pass, they ask if you can help them move things from their barn.")
    print("They're willing to pay you.\n")
    print("\t1. Help them move the things")
    print("\t2. Politely refuse")
    if p.trait == "silver":
        print("\t3. [Silver Tongue] Offer your help if they'll pay your son as well. Earn $40.")
    if p.trait == "instinct" and p.check("firearm") == True:
        print("\t4. [Instinct + firearm] Discretely rob them")

    x = 0
    done = False
    while done == False:
        x = 0
        while x > 4 or x < 1:
            x = choice()
        
        if x == 1:
            print("You help them move a few things from their barn. They pay you $20.")
            p.money += 20
            done = True
            enterE()
        elif x == 2:
            print("Your wife scorns you for passing up on easy money.")
            p.wife_respect -= 1
            done = True
            enterE()
        elif x == 3 and p.trait == "silver":
            print("You convince them to hire you and your son.")
            print("You help them move the things and they pay you $40.")
            p.son_respect += 1
            p.money += 40
            done = True
            enterE()
        elif x == 4 and p.trait == "instinct":
            print("You leave on your covered wagon.")
            print("You return to the homestead after your family has stopped for the night")
            print("You find $70 and an expensive looking ring.")
            p.money += 70
            done = True
            p.gain("homestead ring")
            enterE()

    print("Traveling...")
    for x in range(3):
        p.day += 1
        p.food -= 1
        if p.food < 0:
            noFood()
    enterE()
    #End of Tutorial
    print("You travel for 3 days and enter Bordertown.")
    borderTown()


print("ALPHA VERSION")
print("Press 1 to start a new game.")
print("Press 2 to load a save")
x = 0
while x != 1 and x != 2 and x != 5:
    x = eval(input("Choice: "))

if x == 2:
    print("Save Loaded:")
    with open("D:\\Desktop\\Projects\\Code\\Python\\save1.txt", 'r') as file:
        p.self_status = file.readline().strip()
        p.wife_status = file.readline().strip()
        p.daughter_status = file.readline().strip()
        p.son_status = file.readline().strip()
        p.wolf_status = file.readline().strip()
        p.wolf_name = file.readline().strip()
        p.oxen = int(file.readline().strip())
        p.wife_respect = int(file.readline().strip())
        p.son_respect = int(file.readline().strip())
        p.daughter_respect = int(file.readline().strip())
        p.food = int(file.readline().strip())
        p.ammo = int(file.readline().strip())
        p.materials = int(file.readline().strip())
        p.wagon_status = file.readline().strip()
        p.money = int(file.readline().strip())
        p.location = file.readline().strip()
        p.day = int(file.readline().strip())
        p.hungryman_helped = file.readline().strip()
        p.trait = file.readline().strip()
        
        #KNOWLEDGE
        thing = str()
        thing = file.readline().strip()
        while thing != "END KNOWLEDGE":
            p.knowledge.append(thing)
            thing = file.readline().strip()
        
        
        #INVTENTORY MUST BE LAST
        thing = str()
        while True:
            thing = file.readline().strip()
            if thing == '':
                break;
            else:
                p.gain(thing)
        
        print("Character Status: " + p.self_status)
        print("Trait: " + p.trait)
        print("Wife Status: " + p.wife_status)
        print("Daughter Status: " + p.daughter_status)
        print("Son Status: " + p.son_status)
        print("Oxen: " + str(p.oxen))
        print("Food: " + str(p.food))
        print("Money: " + str(p.money))
        print("Location: " + p.location)
        print("Day: " + str(p.day))
        print("Items:", p.inventory)
        
        print("\nIs this the character you wish to load?")
        if ask() == True:
            #load the save
            print("Loading " + p.location + "...")
            if p.location == "bordertown":
                borderTown()
            elif p.location == "coldpine":
                coldpine()
            elif p.location == "fortd":
                fortd()
            
        else:
            dead()
        
        file.close()
        


elif x == 5:
    print("Developer save loaded.")
    p.food = 600
    p.inventory.append("firearm")
    p.money = 1000
    p.ammo = 4
    print("Player has been given firearm, 4 bullets, 600 days of food.")
    print("Choose trait:")
    print("1) Instinct \n2) Handy\n3) Silver\n4) Survivor")
    x = 0
    while x < 1 or x > 4:
        x = choice()
    
    
    if x == 1:
        p.trait = "instinct"
    elif x == 2:
        p.trait = "handy"
    elif x == 3:
        p.trait = "silver"
    elif x == 4:
        p.trait = "survivor"
        
    print("You will now begin in Bordertown.")
    enterE()
    borderTown()




tutorial()
