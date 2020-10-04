import winsound

def play_sound(frequency=250,duration=1000):
    winsound.Beep(frequency,duration)

if __name__=="__main__":
    frequency=100
    duration=1000
    play_sound(frequency,duration)
    play_sound()