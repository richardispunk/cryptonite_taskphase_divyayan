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
I spent more time on this one, than I should have. The task was to locate an unknown file from the directory `/challenge`. That contents of the file held the flag.
However, after using the command ```ls /challenge```, followed by ```cat /challenge/13552-renamed-run-5651```, I ran into an issue, where the contents weren't displayed
entirely. I soon realized, however, that I had to the file. Hence, I changed the directory to `/challenge` using ```cd /challenge``` and then ran the required file by
using ```./13552-renamed-run-5651```, which led me to the flag `0-2-votFxLQ4FaNmA9_POGwuYkR.dhjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/e7e14eda-89bc-4a83-b233-57283fe3359f)

# touching files
Here, the main objective was to learn how to use the `touch` command and create files. First, I changed directory to `/tmp` by using ```cd /tmp```, followed by creating the files `pwn` and `college`, by using the commands ```touch pwn``` and ```touch college```. Just for verification, I listed the files in the `/tmp` directory, using ```ls``` command. From there, I changed directory to `root` by using ```cd /``` After that, the final task was to execute the command ```/challenge/run```, which led me to the flag `IYprDImKSAUm48SakrEEfj2HuNo.dBzM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/3df31ae3-811e-44bc-8277-838c668a3e64)

# removing files
As the title suggests, this challenge was pretty self-explanatory. The usage of `rm` command was taught here. The task was to delete a file named `delete_me` from the home directory. Just to check whether the file was even present or not, I used the ```ls ~``` command to check the contents of the `home` directory. Once confirmed about the file's presence, I used the command ```rm ~/delete_me``` to delete the file, finally executing the command ```/challenge/check``` to get the flag `gGgaiOzEcQi4ZGZqnJhG9W0u14q.dZTOwUDL0UTN0czW`

![image](https://github.com/user-attachments/assets/71bfe758-39dd-4eec-a051-28c323cd57f3)

# hidden files
This challenge showed me how to make hidden files (files which are named in the following manner `.[filename]`) visible by appending a `-a` to the `ls` command. The task was to find a hidden file in the root `/` directory, which had the flag in it. Hence, I used the command ```ls -a /``` to display the contents of the directory. From there, I proceeded to change directory to root, by using the ```cd /``` command, followed by using ```cat .flag-29022313054015``` to display the flag `EngNlxx7Wh7hEzJ9718MNxue-SI.dBTN4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/3989248e-bd12-4a1b-81d4-4ac87b158bcf)

# An Epic Filesystem Quest
As the name suggests, it was more of a game than a challenge. Here, I had to search through multiple directories, reading files, to get to the flag `AxBNYaJB6pI6roDtG5NGg2HVI0H.dljM4QDL0UTN0czW`. The following snippets show exactly what I did to find the flag.

![image](https://github.com/user-attachments/assets/51b6f948-38ce-47c6-b369-7aef75bd5bb4)

![image](https://github.com/user-attachments/assets/3538cfc9-9e45-460d-8929-23f93f3c8d10)

![image](https://github.com/user-attachments/assets/bbe8b7f5-9125-4345-ab8a-af10c70cb51d)

# making directories
This challenge was quite familiar to me due to the extensive use of the required command `mkdir` in the PPS labs. Here, I had to create a new directory `/pwn` in `/tmp`, for which, I used the command ```mkdir /tmp/pwn```. After that, I had to create the file `college` in the new directory, for which I used ```touch /tmp/pwn/college```. Once done, I executed ```/challenge/run```, which led me to the flag `UxJEEHzjEDcrMQICxgM6Y32A1RX.dFzM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/037ae029-7c0c-4147-a177-599ff28e5701)

# finding files
