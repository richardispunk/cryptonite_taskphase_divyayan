![image](https://github.com/user-attachments/assets/cc64268f-33f2-42b7-b45e-21bb609a058e)# SHELL VARIABLES

## Printing Variables
This challenge was a simple execution of the ```echo``` command to print out a variable. For that, I used the ```echo $FLAG``` and got the flag 
`pwn.college{AW_PAHdGOtvbbw6xsZuesojM4gf.ddTN1QDL0UTN0czW}`

![image](https://github.com/user-attachments/assets/7a02a55b-6172-4ab1-82a8-2610d99a988e)

## Setting Variables
This taught me how to assign values to variables. It is done by using the `=` operator. After executing ```PWN=COLLEGE```, I got the flag  
`pwn.college{YB9ySEJs3U0nJ_RPIIdZrzk0U_d.dlTN1QDL0UTN0czW}`

![image](https://github.com/user-attachments/assets/d06391e1-dbf7-4824-b497-cea7c9e8bbcb)

## Multi-word variables
In this one, we were taught to handle blankspaces in variable values. It is simply done by quoting `""`. I ran ```PWN="COLLEGE YEAH"``` to get the flag
`pwn.college{YgUxyvJwcvex4K5vodoPKX0zeQU.dBjN1QDL0UTN0czW}`

![image](https://github.com/user-attachments/assets/87e9384c-b56d-41ca-bfa4-805c57d8c380)

## Exporting variables
This challenge teaches about how the value of a variable is localised to the current session and has to be exported to be used in any other session. First, I executed 
```export PWN=COLLEGE``` followed by ```COLLEGE=PWN```, ultimately executing ```/challenge/run``` to get the flag 
`pwn.college{0QF8-SLzzUUld1x886JE5eTp5z3.dJjN1QDL0UTN0czW}`

![image](https://github.com/user-attachments/assets/a781e97f-7cb7-4b83-b155-80f891d46aed)

## Printing Exported variables
This challenge taught about the `env` command. upon running which, it returned a few lines of text, where the flag 
`pwn.college{obx4IDFYWgNzAEiZAg7eNwg6pBw.dhTN1QDL0UTN0czW}` was contained.

![image](https://github.com/user-attachments/assets/13551beb-5a45-4c5f-8f68-f412df9d97ca)

![image](https://github.com/user-attachments/assets/8230ca06-2623-4c57-a377-3afd13230cad)

## Storing Command Output
Here, I learnt how to store the output of a command into a variable. For that, I used ```PWN=$(/challenge/run)``` followed by ```echo $PWN```, which returned the flag
`pwn.college{orjU2cx_rzec68hy55EPsfaOgWv.dVzN0UDL0UTN0czW}`

![image](https://github.com/user-attachments/assets/1a883e89-c82b-4a58-aec6-8c1a7d29578d)

## Reading Input
