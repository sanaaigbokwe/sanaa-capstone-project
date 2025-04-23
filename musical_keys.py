"""
Nested Collections
Instruction Practice: Nested Collections
Musical Keys
"""

#### ---- SETUP ---- ####

## -- Library -- ##

import random
import ts_sampler

## -- Musical sequence data -- ##

follow_notes = {
  "A": ["F#", "C#", "D", "E"],
  "B": ["C#", "G#", "A", "D"],
  "C#": ["D", "E", "B", "F#"],
  "D": ["E", "C#", "B", "F#"],
  "E": ["D", "F#", "A", "C#"],
  "F#": ["G#", "E", "A", "C#"],
  "G#": ["B", "A", "E", "F#"]
}
note = "A"

#### ---- NOTES ---- ####

## -- Random notes -- ##





## -- Final note -- ##

ts_sampler.add_note("A")
ts_sampler.rest()

## -- Run -- ##

ts_sampler.run()
