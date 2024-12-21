# PicoMidiKeyboard
A 3D Printed, 25-key keyboard using the Raspberry Pi Pico, primarily to play Rockband 3 Pro Keys in a small convenient device.

# Requirements

3D printer with decent calibration, for snap-fit tolerances.

[CircuitPython](https://circuitpython.org/)

26x Gateron KS-27 Low Profile Red switches

1x Rasbperry Pi Pico (Or other SBC with sufficient digital I/O

# Usage

Add main.py and MidiKeyboard.py to your Circuitpython-equipped Pico, adjusting the digital pin mappings inside of key_pins as necessary. 

Keys are in ascending order from C3 to C5.

MOD key currently shifts the set of keys down one octave.

