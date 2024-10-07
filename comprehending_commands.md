# COMPREHENDING COMMANDS 🎞️
The third module of the Linux Luminarium. This teaches the use of ```cat``` command and basic file usages. Details about the challenges are as follows:

## cat: not the pet, but the command!
Here, we were introduced to the ```cat``` command and showed how it displays the contents of a file when provided an argument. The task was simple, to go to the root `/`
directory and find the flag in the file named `flag`. For this, I first used ```cd /```, followed by ```cat flag``` to get the flag 
`4-YHlpoKUJwgBE79YmQqb64TrSC.dFzN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/b9a18695-2b97-4ddd-b185-b2e7986b7f66)

# catting absolute paths
In this challenge, there wasn't much deviation from the problem statement of the previous one. Only difference being that, here, we had to handle relative file paths. For
this, I used the command ```cat /flag```, which resulted in the flag `wVfzklSFAw0SwqdRQFCvdts_yqB.dlTM5QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/6e560940-cc36-46e9-abc7-233eee9f6e11)

# more catting practice
This challenge, much like the previous one, was to use the `cat` function via specifying the absolute path of the file. It was quite intuitive and simple to grasp, after the
prior problems. I used the command ```cat /lib/x86_64-linux-gnu/gconv/flag``` to find the flag `Ex3NZkMxyZ7ul5WwxFI2NwEfw8S.dBjM5QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/b8bc3319-a5f3-4f95-a99a-d3e508696a44)

# grepping for a needle in a haystack
Here, we were basically taught to use the *search* function via terminal, which is essentially `grep`. Once that idea was cleared, it was a straightforward challenge
provided with the fact that every flag starts with `pwn.college`, it was just a matter of searching for it through the text provided in `/challenge/data.txt`
I used the command ```grep pwn.college /challenge/data.txt```, which gave me the flag `Uz1in2AbgbsrAP0XAfxYd0BZGuS.ddTM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/fd7778ae-d90d-470b-8c50-a13f4dbb6122)

# listing files
