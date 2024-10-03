# PONDERING PATHS 🛣️
The second module of the Linux Luminarium. Here, the basic control and handling of the *tree* filesystem has been taught. Details about the challenges are as follows:
## The Root
In this challenge, the objective was to locate the program `pwn` via the changing the directory using `/`. A simple implementation of ```/pwn``` yielded in successful capturing of the flag
`0aDK2jPBH3rcTPnFpKRleGTCOTA.dhzN5QDL0UTN0czW`. Pretty straightforward, so far, not much to think about.

![image](https://github.com/user-attachments/assets/798530c3-5f1d-44cb-a7c4-4c61d2dbce8b)

## Program and Absolute Paths
This one took me a couple of tries to get it correct. The semantics threw me off, somewhat. Going through the problem statements multiple times helped me understand that the task was to simply run a program via the 
absolute path of the file `run` through the directory `challenge` which is in the root directory `/`. In short, the command ```/challenge/run``` led me to the flag `AWCmMkn4jGYXHugepb1nKMJRaKC.dVDN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/0f1639e1-2e17-4cce-abd0-becdffa6c778)

