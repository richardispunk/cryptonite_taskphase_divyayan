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

## Position thy self
Here, the objective was to, again, run a program `run` from the `challenge` directory. However, unlike earlier, we do not start from the root `/` directory. The starting directory is `position-thy-self/`. From here, I used the **c**hange **d**irectory command (cd) to go back to the root directory. The exact commands were ```cd /``` followed by ```/challenge/run```, which led me to the flag `AAj54A3AJ0P2ApvlSVoar1yVguz.dZDN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/f051b0ad-d83c-48da-9f97-8deecb397378)

## Position elsewhere
Very similar to the previous challenge. Only difference being that, instead of travelling to the `/` root directory, we have to change the directory to `/tmp`. The commands are ```cd /tmp``` followed by ```/challenge/run```, which returns the flag `Uzu-sfyINipzH2RAJ5EMXWqo7m3.ddDN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/b50543cc-9d0c-46ee-8a50-a6b0333ad998)

## Position yet elsewhere
Same as the others before this. This challenge had the path specified to a directory `kernel` inside another directory `sys`. The commands were ```cd /sys/kernel``` followed by  ```/challenge/run```, which returned the flag `0qNY6SbKbEZCdJ_S1zPLtRPq-_s.dhDN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/810463d4-d829-4663-b27b-480d3a7ffa72)

## implicit relative paths, from /
This took me a bit more time to grasp. The concept of relative paths was new, hence I had to read and re-read the problem statement with the explanation of the usage. From there, things clarified a bit. After that, the hands-on work on the terminal made it much more intuitive and sensible. First, I changed the directory to `/` by using the command ```cd /```. From there, the job was to get the program `run` from relative path `challenge`. For this, the code was ```challenge/run```, which led to the flag
`ojB3jY8hSPxkcwO6-sBiav1W9Wy.dlDN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/f23b5041-bcbb-436a-959a-f240296739a0)

## explicit relative paths, from /
Here, we were familiarized a bit more with using `.` in relative paths. Overall, not too difficult, just a bit tricky to get used to the problem statement. The commands were ```cd /```, followed by ```./challenge/run```, which gave me the flag `Ysrjkv2dr3aYAJ3UVPx9-Dw93JY.dBTN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/617dccc4-3d1b-4a01-90a0-55b0dece8fcb)

## implicit relative path
This was on the trickier side, however, due to using the `./` command in PPS lab classes, it cleared a lot of my would-be doubts. Once that was figured out, it was just a matter of changing the directory to `/challenge` via the ```cd /challenge```, followed by using ```./run``` to explicitly ask Linux to run the `run` program, leading to the flag `g2h7Cs4Xu7IhY9aFXRf22nvO1lz.dFTN1QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/e9ea9d94-a9ec-4e3d-9a05-6305ba3b5410)

## home sweet home
For me, this was one of the difficult challenges to get through, due to the fact that it required a broad understanding of relative paths and file specification while using `~` as a shorthand for `/home/hacker`. Naming the specified file as `d`, the command ```/challenge/run ~/d``` led me to the flag `EE4-e3_yU3n9-RR0yhrT_tPu5_5.dNzM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/c251fa74-e6cc-416e-9e4d-63aa0c03b3f5)
