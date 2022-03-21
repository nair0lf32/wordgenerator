# wordgenerator

A python script to generate wordlist (another one)!

## About:

The script use a simple menu to take use input and generate combinations from that.
It then writes the generated data to a file in the output folder. 
The program runs two main modes:

- Random mode: generates a list of words with random meaning from a combination of common characters
- Custom mode: Takes some specific information (comma separated) in a single input, then generates
words combinations from them. 

I made this script mainly to fiddle with itertools and quickly generate custom lists for my CTFs

Wordlists are very useful in penetration testing operations. mostly bruteforce and dictionary attacks

Random mode will get you in little time:
- an alphabetical list (uppercase,lowercase,both), 
- a numerical list from 0 to any tolerable number (crack pins, directories, short numeric codes)
- an alphanumeric list mixed with some special characters...but the length is the limit here

Custom mode will get you:
- A password/directory bruteforce wordlist for a specific target
- Anything you want if you give it the right data (enumeration skills much)

## Usage

Run this script with python:

```$ python wordgen.py```

The output list will be created in the "output" folder
Note: The output file is re-written after each run, so grab your file after completion

the longer the length range of the data, the more time it will take 
(may take seconds... to millennia. not joking) 
the longer the length, the bigger the output file is
(we are talking about either kilobytes or Terabytes here)


## Requirements
- Python 3 (Tested with python 3.9)

## Legal Disclaimer

(Ah yes almost forgot!) 

your personal usage of this script is under your responsibility! Don't do bad stuff. 
It's for learning and having fun (to any legal extend) only!


