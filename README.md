#CTF ENCRYPTION PROJECT

##OVERVIEW
This CTF project is an easy, encryption-based CTF challenge created using Python. The program will randomly generate and store a flag as encrypted text, and the user must figure out how to decrypt it.
The flag is different each time the program is run, and the encryption algorithm is randomized as well.

##SETUP
1. Make sure you have some version of Python 3 installed. If you need to install it, you can download it at www.python.org or through the Microsoft Store if you are on Windows.
2. To get started using this program, download the ctf.py file and save it in a directory of your choosing.
3. Start a terminal instance in the directory where the file is saved and run the program using the following command:
```
python3 ctf.py
```

##RUNNING THE PROGRAM
The program itself should be fairly intuitive. It prompts the user to enter one of the following three commands:
  ```
  solve
  hint
  quit
  ```
Note that these commands are case sensitive and must be typed exactly.

The 'solve' command allows the user to enter in the flag and will tell the user if it is correct or not. Note that you must enter the solve command before submitting the flag or it will not recognize the flag.
Upon a successful solve attempt, the program will ask the user if he or she wants to play again. Type 'yes' or 'y' to play again. Any other response will be interpreted as 'no', and the program will quit.

The 'hint' command generates a hint for the user. The first hint simply gives a clue as to what type of algorithm is being used. 
If a hint is requested again, the player will be given a more detailed clue that dynamically updates based on how the algorithm generated the flag.
There are only two hints and if the player repeatedly enters the 'hint' command the program will simply repeat the second clue.

The 'quit' command quits the program.

##TROUBLESHOOTING
There are not currently any bugs that the developer is aware of. If an issue does arise, try exiting the program and restarting it. If issues continue, contact the developer.

##Happy solving!


