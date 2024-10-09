# DIGESTING DOCUMENTATION 📄

## Learning from Documentation
This challenge aimed to get the user more comfortable with using arguments for certain tasks. Here, for example, simply running ```/challenge/challenge``` would not fetch the flag, it needed an argument ```--giveflag```. The total command ends up as ```/challenge/challenge --giveflag```, which gave me the flag 
`Y-Nc2j_Z6ORmuDLYw6B-GLVKFlm.dRjM5QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/35cdf88d-a3e5-440b-9d24-ef970f17afeb)

## Learning Complex Usage
Here too, the task was to pay attention to the documentation of the command. This challenge got me more used-to with arguments taking arguments themselves. Although seemingly complex, the task was simple enough. All I had to implement was ```/challenge/challenge --printfile /flag``` to fetch the flag `EYO2Gm7g_K3o1dHEsySnnhCb0Ih.dVjM5QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/5c4e5be3-decc-4ef8-b25c-7020b59a54d3)

## Reading Manuals
This was perhaps the most important challenge till now (basically teaching me to RTFM). It was fun and made the work feel less of a task, and more of a real-world implementation of commands. After running ```man challenge```, I went through the manual, which showed that the challenge had quite a few fun little tricks. But, the most essential argument was the one required to find the flag ```--cmcmng NUM```. Hence, I executed ```/challenge/challenge --cmcmng 840```, which gave me the flag 
`cVGRm8HcmnN4Lgqe0m5hKV4kjqP.dRTM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/6bb3606d-2fdb-4d67-8878-afeee1be0a71)

![image](https://github.com/user-attachments/assets/50bb1cc7-fa53-4d00-87a6-392a28842cc4)

## Searching Manuals
This was similar to the previous challenges, however, this focused more on searching through a given manual, since they tend to be quite detailed and overwhelming when trying to go through each of the statements. Here, after opening the `challenge` manual by running ```man challenge```, I used ```/flag``` to search through the manual, until I came across the arguement `--vpa`, which was marked as the correct one. From there, I pressed ```q``` to exit the manual and ran ```/challenge/challenge --vpa``` to get the flag `A7rWnythzgOOMNtAJavtjrY1xvF.dVTM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/21f900e3-fb4d-4984-be04-dbda87541582)

## Searching for Manuals
This challenge was not entirely different from Nolan's 'Inception'. First, I had to go through the manual of the `man` function by using ```man man```, to learn more about it. There, I noticed `man -k [apropos options] regexp ...` returned a search based on keywords. Following that, I executed ```man -k challenge```, which gave me a random command `wafcxcnuns`. Reading its manual by ```man wafcxcnuns```, I finally had to implement the command ```/challenge/challenge --wafcxc 407``` to get the flag `w4_aNfcH0FxHcQNnO7u3XLn5JQs.dZTM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/ca5f4e96-e2bc-4d02-8a38-1f5cdf35ffe2)

![image](https://github.com/user-attachments/assets/77c06a60-9261-49b9-83ea-748a741f32ac)

![image](https://github.com/user-attachments/assets/48af5a26-f90d-48e8-b90f-08412cd1b654)

## Helpful Programs
In this challenge, initially, I struggled to understand which program they referred to, in order to find the flag. Then, I executed ```/challenge/challenge --help```, which gave me more details about the challenge. From there, it was a simple task of getting a value (password) by running ```/challenge/challenge -p``` followed by ```/challenge/challenge -g 730```, which led to the flag `kcL7gLfB3kCbs0SEcE4UZqk2z1g.ddjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/99b25e14-260f-4d8d-82f0-67cda64a6e6f)

## Help for Builtins
This taught me about builtin programs and how they are implemented directly from the shell itself. Here, `challenge` was a builtin, for which I executed ```help challenge```. From there, the work was simple to find the correct value to be used with the correct argument, which ended up being ```challenge --secret QDXxaHnC```, resulting in the flag `QDXxaHnCFyRSD85iiUaaBUlPinF.dRTM5QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/72816b56-b44f-44a7-a079-6b247f4d434c)
