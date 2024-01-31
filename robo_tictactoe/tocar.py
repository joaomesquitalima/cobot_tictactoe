import pygame
import time

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Aguarde o término da reprodução
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Substitua "caminho/do/arquivo/audio.mp3" pelo caminho real do seu arquivo de áudio
audio_file_path = "ola.mp3"
play_audio(audio_file_path)
