# Simple Secret Santa

Ho Ho Ho!!! T'is the season of holidays, so here's a holiday themed script! 
This is a simple secret santa randomizer that generates pairs from a given set of names for the purpose of deciding the secret santa.
The set of names is passed through a text file. See names.txt for example.

On running the SSanta.py file, at prompt, insert the file name which has the names separated by a new line.
As an example, insert names.txt.

This script will read all the names inside the text file, run it through a randomizer and generate a pair such that:
  1. Everyone gets only one gift
  2. The giver can't gift himself
  3. The giver won't receive a gift from the person he gifted.

