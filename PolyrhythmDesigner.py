import pygame
import math


def calculate_duration(bpm, beats_per_measure):
    return (60 / bpm) * beats_per_measure


def play_polyrhythm(time_signature):
    pygame.mixer.init()
    bpm = 70
    beats1, beats2 = map(int, time_signature.split(":"))
    lcm = beats1 * beats2 // math.gcd(beats1, beats2)  # Calculate least common multiple
    duration1 = calculate_duration(bpm, beats1)
    duration2 = calculate_duration(bpm, beats2)
    
    total_duration = min(duration1, duration2) * 4  # Play 4 measures
    interval1 = total_duration / lcm  # Interval for rhythm 1
    interval2 = total_duration / lcm  # Interval for rhythm 2
    
    beat_sound1 = pygame.mixer.Sound("beat.wav")
    beat_sound2 = pygame.mixer.Sound("beat2.wav")

    while True:
        for _ in range(lcm):
            if _ % (lcm // beats1) == 0:
                beat_sound1.play()
            if _ % (lcm // beats2) == 0:
                beat_sound2.play()
            pygame.time.wait(int((interval1 + interval2) * 100))  # Convert seconds to milliseconds


if __name__ == "__main__":
    print('Developed by A4P5')
    print()
    time_signature = input("Enter the time signature (e.g., 3:4): ")
    print('\nSound should now be playing...')

    play_polyrhythm(time_signature)
