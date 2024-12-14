import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My Name is Virtual Assistant")
        return "My Name is Virtual Assistant"

    elif "hello" in user_data:
        text_to_speech.text_to_speech("Hi sir, How can I help you")
        return "Hi sir, How can I help you"
        
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning, sir")
        return "Good Morning, sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay, sir")
        return "Okay, sir"

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Spotify is now ready for you")
        return "Spotify is now ready for you"
        
    elif "youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Youtube is now ready for you")
        return "Youtube is now ready for you"
        
    elif "open google" in user_data:
        webbrowser.open("https://www.google.co.in/")
        text_to_speech.text_to_speech("Google is now ready for you")
        return "Google is now ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
        

    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"


    
    