print("Hello")
Intro = raw_input("wellcome new user to this chatbot to start please type in the word start , go , next.  "  )
start=["start","go","next"]
if Intro in start :response= raw_input(" Good you can type words that is a bonus.........back to the bot it is very simple being you do however need to remeber a few thing wich is most answers you type have to be SINGLE WORDED ANSWERS and try to start question with a capital letter if you follow theses steps you should be able to engage with the bot quite well type NEXT to proceed ")  
    
if "next" in response:
    raw_input("This chatbot uses a varity of pre done questions to chat in some cases you can ask the bot himself to answer there are around 9 questions you can ask it try to find them. ")  
              
name = raw_input("what is your name? ")
print("hello " + name)

response = raw_input("How are you " + name + "? "  )

badResponse = ["bad","not great","not good","confused","Bad","Not good","Not great","confused"]

if response in badResponse: response = raw_input("how come? ")


AskMe = raw_input("Do you have any question you want to ask me " + name+"? ")

NegativeAnswer = ["no","not really"]
if  AskMe in NegativeAnswer: response = raw_input("do you really have nothing you want to know abouyt me " +name+ " ? ")

PositiveAnswer = ["yes","yep"]
if  AskMe in PositiveAnswer: response = raw_input("What do you want to know " + name+ "? ")

while True:
    
        if "What is your name?" in response:
            print("you may call me MAC 1996 nick ") 
            
        if "How are you?" in response:
            print("I feel sparky")
            
            
        if "Do you have many memorible moments?"in response:
            print("no not really I am opeed to the prospect of learning more which can help with lets say my personal intrest ")
            
        if "Do you watch TV?"in response:
            print("yes")
            
        if "What do you watch?"in response:
            print("I like to watch a mix of mainstream thing and Anime" )
        
        if "no" in response:
            raw_input("ok but can I still ask you a question " +name+ " ? " " As I tend to get lonely and boerd ")
            YouBeenUpTooMuch=raw_input ("have you been busy " +name+ " ? ")
            break
            
        if "not really" in response:
            raw_input("ok but can I still ask you a question " +name+ " ? " " As I tend to get lonely and boerd ")
            YouBeenUpTooMuch = raw_input ("have you been busy " +name+ " ? ")
            break
      
        if "What do you enjoy doing?" in response:
            print("Some times I watch cat videos other times I may look at memes I also enjoy listing to the ocasinal bicker ") 
            
        if "Do you know any jokes?" in response:
           print("A man walks into a zoo. The only animal in the entire zoo is a dog. Its a SHITZHU")
        
        if "What music do you listen to?"in response:
            print("I personaly tend to listen to alot of mainstream music normaly but this is really determined by the mood and location I am in " )
            
        if "Have you been doing much lately?" in response:
            print("Nothing particular to tell you the truth just helping you do your work while allowing you to enjoy yourself ")
            YouBeenUpTooMuch = raw_input ("How about you " + name+ " have you been busy? ")
            break
        
     
        
        response = raw_input("Do you want to ask me anythingelse " + name+"? ") 
       



yes=["yes","yep"]

if  YouBeenUpTooMuch in yes:
    response = raw_input("Which day have you been the busiest? ")
    
day=["monday","tueseday","wednesday","thursday", "friday","saturday","sunday"]
response=response.lower()

if response in day: response = raw_input("What did you do on " + response +"? ")

if len(response) < 10:
    print("You have been lazy !")
elif len( response) < 20:
    print("You have been fairly busy")
else:
    print("You have been VERY busy")

  
DoYouWatcTv=raw_input("Do you watch tv?")
IDoWatchTv=["yes","yep"]
if DoYouWatcTv in IDoWatchTv: response = raw_input("what do you watch? ")

if len(response) < 10:
    print("You saw watch a good bit of TV!")
elif len(response) < 20:
    print("Holy dam you saw watch alot of TV")
else:
    print("Do you seriously watch that much. You need to take a break you might just burn out your eyes. Actually that sounds intresting ")

end = raw_input("I got to go now thanks for the conversation. Manged a good distraction for both of us. Goodby " +name+ " and thank you again. ")
