# Auditory Oddball Experiment in python

This script runs a basic auditory oddball experiment in Python, using [Pygame](https://www.pygame.org/news).

## Contents:

* *AuditoryOddball_Generic.py*: the main experiment script.
* *MakeSounds_Oddball.py*: script that prepares the auditory stimuli.
* *AuditoryOddball_QualityCheck.py*: a [Jupyter notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) for a quality check, after running the experiment.

## AuditoryOddball_Generic

A series of parameters can be modified:
* ITI: inter-trial interval in miliseconds (from sound onset to sound onset)
* nu_sounds: total number of stimuli to be presented in each block
* duration: duration of each stimulus, in miliseconds
* nu_blocks: totaly number of experimental blocks (preferably even number)
* frequency1: main frequency of one auditory stimulus sounds in Hz
* frequency2: main frequency of the second auditory stimulus
* ratio_deviant: ration of deviant sounds in each block

