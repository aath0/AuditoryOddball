# IMPORT LIBRARIES
import sys
import os
import pygame
from pygame.locals import *
import numpy as np
import scipy.io as io
import time
import string
import re
import math
import imageio
import wave
import signal
from MakeSounds_Oddball import MakeSounds_Oddball

# handle user interruptions:
def signal_handler(signal, frame):
    print("Script ended by user")
    print("...You were in block number: " + str(bl+1) + " and trial number: " + str(tr+1) + "...")

    pygame.quit()
    sys.exit(0)

experiment_path = "/Users/atzovara/Documents/Python/AuditoryOddball/"

width = 1440
height = 900

ITI = 600 # in ms
nu_sounds = 50
duration = 100 # sound duration
nu_blocks = 2
standard = 2000 # frequencies in Hz
deviant = 500
ratio_deviant = 0.2
date = (time.strftime("%m%d%Y-%I%M%S"))

p_id = input('Patient ID: ') # change to raw_input for python < 3
Block = input('Start with block: ')
# Create sounds:
Stimuli = MakeSounds_Oddball(nu_sounds, nu_blocks, duration, [standard, deviant] ,ratio_deviant, int(p_id))
Dev = np.array(Stimuli[0])
Freq_Dev = np.array(Stimuli[1])
Sounds = np.array(Stimuli[2])

np.savez(experiment_path+'/Data/Participant_' + p_id + '_time' + date + '.mat', Dev = np.array(Stimuli[0]), Freq_Dev = np.array(Stimuli[1]), Sounds = np.array(Stimuli[2]))

warmUp = 3000 # in ms

# Initialize pygame:
pygame.mixer.pre_init(44100, -16, 2, 32) # setup mixer to avoid sound lag
pygame.init()

clock = pygame.time.Clock()

# from which block do we start?
bl = int(Block)-1
SoundOn = np.zeros((nu_sounds, nu_blocks))

while bl < nu_blocks:
    tr = 1
    input('...Press any key to start with block number: ' + str(bl+1) + '...')
    # save stimuli first:
    #matOutDict = {'Dev': np.array(Stimuli[0][bl]), 'p_id': p_id, 'Block': Block, 'Freq': np.array(Stimuli[1][bl])}

    Sounds_bl = np.array(Stimuli[2][bl])
    time.sleep(5) # let vlc warm up
    last_time = time.time()
    S2pl = pygame.mixer.Sound(Sounds_bl[0,:].astype('int16')) #prepare first series of sounds

    while tr < nu_sounds-1:

        if time.time()-last_time > ITI/1000 - 0.005:
            SoundOn[tr,bl] = pygame.time.get_ticks()
            S2pl.play()

            #prepare buffer for next trial:
            tr = tr+1
            S2pl = pygame.mixer.Sound(Sounds_bl[tr,:].astype('int16')) #prepare first sound
            last_time = time.time()
        else:
            time.sleep(0.001)

        signal.signal(signal.SIGINT, signal_handler)

    np.save(experiment_path+'/Data/Participant_' + p_id + '_Block' + str(bl+1) + '_time' + date + '_TIMING', SoundOn)
    bl += 1

pygame.quit()
