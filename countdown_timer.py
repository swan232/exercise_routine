import time as t
from playsound import playsound
import pyttsx3



engine = pyttsx3.init()
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female



def countdown(tme):
	for i in range(tme):
		print(str(tme-i) + " seconds remaining \n")
		##we also need the loop to wait for 1 second between each iteration
		# t.sleep(1) # speaking text alound takes time, no need to add sleep time
		engine.say(str(tme-i))
		engine.runAndWait()
	print("Time is up")
	playsound('bell ring.mp3') # play bell ring



def routine(tme,exer = 'Rest'):
	if exer != 'Rest':
		print('Start exercise: ' + exer + ' ' + str(tme) + ' seconds countdown...')

		engine.say(str(tme) + ' seconds ' + exer + '. Ready? Go!')
		engine.runAndWait()
	else: 
		print('Rest for %s seconds' %(tme))
		engine.say('Rest for ' + str(tme) + ' seconds' )
		engine.runAndWait()
	
	countdown(tme)
	engine.stop()


# routine(15, 'Pushups')
# routine(5, 'Rest')
# routine(20, 'Squats')
# routine(5, 'Rest')
# routine(20, 'Two-Arm Hang')

def main():
    routine(15, 'Pushups')
    routine(5, 'Rest')
    routine(20, 'Squats')
    routine(5, 'Rest')
    routine(20, 'Two-Arm Hang')
    routine(5, 'Rest')
    routine(20, 'Hanging Pelvic Tilt')



if __name__ == "__main__":
    main()

