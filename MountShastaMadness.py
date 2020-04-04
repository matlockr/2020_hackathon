# file: MountShastaMadness.py
# Robert Matlock
# 4/4/2020
# Hackathon 2020 Theme: Mt. Shasta

# Project Description: I decided to make a text adventure game
# that has a player explore the mountain and learn about the some
# of the places around the mountain and some of the strange 
# activities that are occuring around the mountain.


# Get imports
import time
import os

current_event = 0


# This section is used when comparing the user input to what is possible
# in each event.
actions = ["look", "go"]
help_list = "The two commands are \"look\" and \"go\""
not_good_action = "I do not understand... Type help for list of actions or quit to exit program"
not_good_go = "I do not know where that is"
trailhead_actions = ["trail", "car"]
horse_camp_actions = ["trail"]
helen_lake_actions = ["trail"]
misery_hill_actions = ["cave"]
cave_enterance_actions = ["cave"]
cave_system_actions = ["door", "back"]


# This section contains all the text for the text adventure
intro = """

Mount Shasta Madness

My name is David Marquee, I’m a journalist working remotely as an employee of 
the San Francisco local paper named The Good Times. I’ve wrote stories ranging 
from psychopathic killers to multi-generational prison gang activity. While I 
love the work I do, I have wanted some thing a bit more different these days 
and think I found it. 

While driving up north along the I-5, I stopped by the small town of Mount 
Shasta. While looking for a local coffee shop I felt strange to say the least.
While from the highway the town appeared normal, but from the inside I could 
see stores such as magic crystal stores. How a business like that stays afloat
I haven’t the slightest idea. 

I made my way into a local coffee shop and ordered my cup of joe. I have the 
tendency to eavesdrop people’s conversations by accident due to my line of 
work, but something seemed off. People spoke about strange activities on one 
of the local mountains, specifically Mt. Shasta. These strange activities 
that had been seen before according to the locals but were more active than
before.

After finishing my coffee, I decided to investigate the abnormal activities 
of Mt. Shasta. While I have done some hiking in the past, this hike would 
certainly be challenging for me, but I was excited to see what I could learn 
about the mysteries of the mountain.
"""

trailhead_intro = """
As I parked my car at the trailhead parking lot I could already tell something 
was off. Will a clear blue sky and weekend day the lot should be packed, or at 
least have anybody else by me. How could I be the only person looking to hike 
this trail?

Regardless, I gather my gear that I bought at one of the local shops. I even 
got a good deal, at least according to the owner. I had enough gear to last 
3 days, which should be more than enough to get to the summit and back with 
plenty to spare.
"""

trailhead_look = """
As I stood in the parking lot, I could see in front of me the trail head 
where… the trail began unsurprisingly. Next to the trail was an informational 
board about the trail ahead. Nearby I could see some colorful tents set up 
behind a sign that says “Hippie Camp” along with some long haired people 
wearing psychedelic clothing.
"""

ending_3 = """
I decided to leave the trailhead and head home as apparently I’m just not cut 
out to be a supernatural journalist. But that’s fine, I bet there wasn’t 
anything special about Mt. Shasta anyway.

The End?
"""

horse_camp_intro = """
Horse Camp, the first major stop along the trail, why I am not sure. The trail 
has been relatively easy so far, but I know for certain that I will be 
challenged soon as I could continuously see the mountain looming in the 
distance waiting for me to take it on. 
"""

horse_camp_look = """
While there wasn’t much but dense forest around the camp, the sits a lonely 
cabin. The cabin looked abandoned as the large wooden door was left open 
letting anyone go in and out of it. To the right was the continuation of the 
path I was currently on towards the next stop called Helen Lake.
"""

helen_lake_intro = """
While approaching the Helen Lake Campsite, the area got a fair darker as some 
clouds were starting to form of the mountain summit. However, I still was 
interested in climbing the top regardless. 
"""

helen_lake_look = """
I look around to see an empty campsite. Barren, lonely, and untounched by any
person for some time. Strangly, I hear the strange sounds coming from over the
ridge. Sounds of chants and rythmic music are just within earshot. The trail to 
Misery hill is just up ahead. I should hurry.
"""

misery_hill_intro = """
Misery Hill has lived up to its name as being the most challenging part so far 
as there is nothing but snow on the trail and a steepness even expensive 
treadmills could not even dream of replicating. Luckily, the summit I within 
reach along with an even more dense cloud formation that has blocked out my 
view of the outside world. Alone and cold, I still strive to reach my goal to 
get to the top of Mt. Shasta.
"""

misery_hill_look = """
The clouds fog up my vision, but i can make out a strangly ominus cave very 
close to me. It asks me to come closer and can't help feel compeled to make my
way towards it. Strange...
"""

cave_enterance_intro = """
I approached the wide opening to the dark and seemingly endless black rock 
cave. Every sound I made echoed through its interior as I could hear strange 
noises coming from deep within. Harrowing noises that are low in pitch but 
seem to pass though my physical body with ease as if I don’t exist.
"""

cave_enterance_look = """
If the strange noises and chanting weren't enough to sends chills down my core,
the cave I stand in front of has done enough to make me worried about what is to
come. I want to no... I need to go inside this cave.
"""

cave_system_intro = """
The darkness of the black rock cave makes it very difficult to tell how far 
I have traveled, but I as turn the corner of the one the split paths inside 
the cave system I see a deep red light. I’m not sure if the light was my 
imagination making sense of the pitch black environment, but I wanted to make 
a further investigation to be sure. 

As I approached the red light, I noticed what looked like a human made 
doorway. The doorway was open to pass thru but was certainly not natural. 
"""

cave_system_look = """
Other than the deep read light and the odd looking door I can't make much of
anything. Maybe I should go back. Maybe I should go through the door. I don't
know what to do.
"""

ending_2 = """
I decide the strangeness of the situation is too much for me to handle and I 
to head back to the entrance of the cave. However, as I make my was back 
around the corner before I saw the red light, the entrance to the cave is 
gone. 

In a panic, I continue to look around to find the exit to this pitch black 
nightmare. I search high and low for any sign of freedom but fail to do so. 
I had no direction or any sense of time as the batteries in my flashlight 
start to die.

I cry out for help but hear nothing out the echoes of my own voice.

The End?
"""

lemurian_outpost_intro = """
I pass through the doorway and see A bright light. After traveling through the 
cave for an unknown amount of time my eyes werent adjusts to such a light. I 
can make out humanoid figures speaking a language I neither understand nor have
heard of in my life.

Before I have any chance to respond my vision goes dark.

Darkness...

The End
"""

# This function prints the text given to it
def PrintText(text):
    print(text)
    time.sleep(1)
    input("Press Enter to continue...")


# This function determins what if the user input is valid
def CheckEventAction(user_action, event_actions):
    for act in range(len(event_actions)):
        if event_actions[act] in user_action:
            return act
    return -1


# This is the main loop of program where depending on the current event
# the player can do certain things
def GetAction():
    global current_event
    os.system("cls")
    
    
    if current_event == 0:
        PrintText(trailhead_intro)
        user_input = input("Action: ")
        user_input = str.lower(user_input)   
        if "go" in user_input:
            action = CheckEventAction(user_input, trailhead_actions)
            if action == -1:
                PrintText(not_good_go)
            elif action == 0:
                current_event = 1
            elif action == 1:
                PrintText(ending_3)
                return False    
        elif "look" in user_input:
            PrintText(trailhead_look)
        elif "help" in user_input:
            PrintText(help_list)   
        elif "quit" in user_input:
            print("Quitting...")
            return False
        else:
            PrintText(not_good_action)
            
    elif current_event == 1:
        PrintText(horse_camp_intro)
        user_input = input("Action: ")
        user_input = str.lower(user_input)
        if "go" in user_input:
            action = CheckEventAction(user_input, horse_camp_actions)
            if action == -1:
                PrintText(not_good_go)
            elif action == 0:
                current_event = 2
        elif "look" in user_input:
            PrintText(horse_camp_look)
        elif "help" in user_input:
            PrintText(help_list)   
        elif "quit" in user_input:
            print("Quitting...")
            return False
        else:
            PrintText(not_good_action)
            
    elif current_event == 2:
        PrintText(helen_lake_intro)
        user_input = input("Action: ")
        user_input = str.lower(user_input)
        if "go" in user_input:
            action = CheckEventAction(user_input, helen_lake_actions)
            if action == -1:
                PrintText(not_good_go)
            elif action == 0:
                current_event = 3
        elif "look" in user_input:
            PrintText(helen_lake_look)
        elif "help" in user_input:
            PrintText(help_list) 
        elif "quit" in user_input:
            print("Quitting...")
            return False
        else:
            PrintText(not_good_action)
            
    elif current_event == 3:
        PrintText(misery_hill_intro)
        user_input = input("Action: ")
        user_input = str.lower(user_input)
        if "go" in user_input:
            action = CheckEventAction(user_input, misery_hill_actions)
            if action == -1:
                PrintText(not_good_go)
            elif action == 0:
                current_event = 4
        elif "look" in user_input:
            PrintText(misery_hill_look)
        elif "help" in user_input:
            PrintText(help_list)
        elif "quit" in user_input:
            print("Quitting...")
            return False
        else:
            PrintText(not_good_action)
            
    elif current_event == 4:
        PrintText(cave_enterance_intro)
        user_input = input("Action: ")
        user_input = str.lower(user_input)
        if "go" in user_input:
            action = CheckEventAction(user_input, cave_enterance_actions)
            if action == -1:
                PrintText(not_good_go)
            elif action == 0:
                current_event = 5
        elif "look" in user_input:
            PrintText(cave_enterance_look)
        elif "help" in user_input:
            PrintText(help_list) 
        elif "quit" in user_input:
            print("Quitting...")
            return False
        else:
            PrintText(not_good_action)
            
    elif current_event == 5:
        PrintText(cave_system_intro)
        user_input = input("Action: ")
        user_input = str.lower(user_input)
        if "go" in user_input:
            action = CheckEventAction(user_input, cave_system_actions)
            if action == -1:
                PrintText(not_good_go)
            elif action == 0:
                PrintText(lemurian_outpost_intro)
                return False
            elif action == 1:
                PrintText(ending_2)
                return False
        elif "look" in user_input:
            PrintText(cave_system_look)
        elif "help" in user_input:
            PrintText(help_list) 
        elif "quit" in user_input:
            print("Quitting...")
            return False
        else:
            PrintText(not_good_action)
            
    return True
            

# This section gets the program started
PrintText(intro)

game_running = True

while game_running:
    game_running = GetAction()