# Auditory Oddball Experiment in python

This script runs a basic auditory oddball experiment in Python, using [Pygame](https://www.pygame.org/news).

## Contents:

* *AuditoryOddball_Generic.py*: the main experiment script.
* *MakeSounds_Oddball.py*: script that prepares the auditory stimuli.
* *AuditoryOddball_QualityCheck.py*: a [Jupyter notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) for a quality check, after running the experiment.

## AuditoryOddball_Generic.py

A series of parameters can be modified:
* ITI: inter-trial interval in miliseconds (from sound onset to sound onset)
* nu_sounds: total number of stimuli to be presented in each block
* duration: duration of each stimulus, in miliseconds
* nu_blocks: totaly number of experimental blocks (preferably even number)
* frequency1: main frequency of one auditory stimulus sounds in Hz
* frequency2: main frequency of the second auditory stimulus
* ratio_deviant: ration of deviant sounds in each block

## AuditoryOddball_QualityCheck.py

This notebook allows you to do some quality checks after running the experiment. 
* Cell 1: Information about the auditory stimuli of each block (frequency of deviant stimuli and their order). Because this is a roving paradigm, the deviant frequency changes in each block.
* Cell 2: Inter-stimulus interval. Plots of the interval from the onset of one sound to the onset of the next, in miliseconds.
For low-level auditory experiment it is crucial to keep a constant ITI, as the more predictable the onset of the next stimulus is, the larger the surprise response from the deviant ones. Please keep in mind that this is the *theoretical* ITI of the experiment, as recorded in python. In practice there might be further variations, which should be checked with an oscilloscope.
* Cell 3: Another quality check, that displays the two auditory stimuli.
