import os
from time import sleep

from selenium import webdriver
from gtts import gTTS
from playsound import playsound

#tts = gTTS(text="This is a visa appointment!", lang='en')
#tts.save("C:/Windows/Media/TerminVoice.mp3")
driver = webdriver.Chrome()
# url = 'https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/9ae8be97-4136-44ba-8375-c2c9f70ede01?dswid=5171&dsrid=545&st=2&v=1637910291707'
# url of the appointment booking
#url = 'https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/c95efa99-9843-4d16-841c-bffd946bcd86?dswid=8986&dsrid=226&st=2&v=1639396828588'
url = 'https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/5f91f201-93fe-4dd4-b341-deb90875f306?dswid=3109&dsrid=255&st=2&v=1676554012339'

driver.get(url)




# to start the file from python

item = 1
retries = 0
sleep(1)
while True:
    btn_next = driver.find_element_by_id('applicationForm:managedForm:proceed').click()

    while item != None:
        try:
            item = driver.find_element_by_id('j_idt440_modal')
        except Exception as e:
            item = None
            sleep(9)
    item = 1
    try:
        date = driver.find_element_by_class_name('ui-datepicker')
    except Exception as e:
        date = None
    if date:
        i = 0
        while i < 10000:
            # play sound

            playsound('C:/Windows/Media/Alarm02.wav')
            #os.system("start C:/Windows/Media/Alarm01.wav")
            #os.system("start C:/Windows/Media/TerminVoice.mp3")
            #os.system('say "There is a visa termin!"')
        break
    retries += 1
    if retries % 100 == 0:
        # play sound
        #os.system('afplay /System/Library/Sounds/funk.aiff')
        print(retries)
       
