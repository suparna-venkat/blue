import pygame
import time

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("blue.mp3")  # Replace with your song file
    pygame.mixer.music.play()

def print_lyrics():
    lines = [
        "Your morning eyes",#1.2
        "I could stare like watching stars",#1.3
        "I could walk you by",#1.3
        "and I'll tell without a thought ",#0.1
        "You'd be mine",#0.4
        "would you mind", #0.5
        "if I took your hand tonight? ",#0.7
        "Know you're all",# 0.4
        "that I want",#1.0
        "this life ",#3.0
        "I'll imagine we fell in love ",#0.0
        "I'll nap under moonlight skies with u", #0.0
        "I think I'll picture us u with the waves ",#0.0
        "The ocean's colors on your face ",#0.0
        "I'll leave my heart with your air ",#0.3
        "So let me fly with you ",#0.3
    
        ]        
    delays = [1.2, 1.3, 1.3, 0.1, 0.4, 0.5, 0.7, 0.4, 1.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.8]
    

    for i, line in enumerate(lines):
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.1)
        time.sleep(delays[i])
        print()

play_song()
print_lyrics()
 