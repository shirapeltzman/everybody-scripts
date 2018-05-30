#!/usr/bin/env python3

# Import modules we need
    # What should we import to get the job(s) done?

# Rule: Does every file have an extension?
# Rule: Every file is at least zero bytes
# Rule: There are no hidden files here
# Rule: No filename has any sort of whitespace
    # What input does this need?
    # What should the output be?

# Output report
    # What input should this get to produce a report?
    # Does it produce the whole report or does it output line by line?

# Main function
def validator():
    pass
    # Some things we might want to do here:
        # Gather and check user input
        # Set up output filename (see if we're overwriting anything?)
        # Get a list of files we're working with
        # Run some rules and get feedback
        # Generate a report
    # Other things to think about
        # How should we handle unexpected input?
        # How do we write/run tests on this?

if __name__ == '__main__':
    validator()
    
import os

def getDirectory():
    targetDirectory = ('Enter the directory path: ')
    return targetDirectory

def validateExtension(filename):
    print("All files have extensions")

def validateFileSize(filename):
    print("All files bigger than 0 bytes")

def findHiddenFiles(filename):
    print("No hidden files found")
    
def findWhiteSpace(filename):
    print("No filenames contain whitespace")
    
targetDirectory = getDirectory()

filenames = os.listdir(targetDirectory)
print(filenames)

for filename in filenames:
    validateExtension(filename)
    validateFileSize(filename)
    findHiddenFiles(filename)
    findWhiteSpace(filename)
print("Done!")
