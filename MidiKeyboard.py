#Pi Pico MIDI keyboard
#Cribbed mostly from https://blog.4dcu.be/diy/2021/05/20/MIDIpad.html


import board, digitalio, time, usb_midi, adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

config_Channel = 0
config_Velocity = 100


midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=config_Channel)

print("PicoKey MIDI Keyboard")
                #GPIO for 25x keys
key_pins = [board.GP12,
            board.GP16,
            board.GP14,
            board.GP6, 
            board.GP5,

            board.GP10,
            board.GP11,
            board.GP13,
            board.GP9,
            board.GP15,
            board.GP8,
            board.GP4, 

            board.GP17, 
            board.GP7,
            board.GP18, 
            board.GP3,
            board.GP19,

            board.GP20, 
            board.GP2,
            board.GP21, 
            board.GP1,  
            board.GP22, 
            board.GP0, 
            board.GP26, 

            board.GP27] 

modifier_pin = board.GP28 

key_notes = range(48,73) #C2 to C4
key_notes_mod = range(36, 61) #-1 Oct to use func keys
        
#Setups
keys = [digitalio.DigitalInOut(kpin) for kpin in key_pins]

for k in keys:
    k.direction = digitalio.Direction.INPUT
    k.pull = digitalio.Pull.UP

modifier = digitalio.DigitalInOut(modifier_pin)
modifier.direction = digitalio.Direction.INPUT
modifier.pull = digitalio.Pull.UP

pressed_keys = [False for _ in key_pins]
triggered_keys =  [False for _ in key_pins]

current_notes = key_notes

#Loop
while True:
    #Key presses
    for index, key in enumerate(keys):
        pressed_keys[index] = not key.value

    #Mod pressed
    if not modifier.value:     
        current_notes = key_notes_mod
       # print("Mod")
    else:
        current_notes = key_notes


    for index, (pressed, triggered) in enumerate(zip(pressed_keys, triggered_keys)):
        if pressed and not triggered: #On
            #print("note %d started" % index)
            #print("pin %s on" % key_pins[index])
            midi.send(NoteOn(current_notes[index], config_Velocity))
            triggered_keys[index] = True
        elif not pressed and triggered: #Off
            #print("note %d ended" % index)
            midi.send(NoteOff(current_notes[index], config_Velocity))
            triggered_keys[index] = False




    time.sleep(0.01)

#todo; debounce