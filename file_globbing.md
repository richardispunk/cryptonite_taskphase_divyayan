# FILE GLOBBING *️⃣
This module is teaches how to reduce work for the user by 'globbing' and reducing the need to typing out entire file paths. The challenges are as folllows:

## Matching with *
Here, I was taught that the `*` almost acts as a primitive autofill and returns the closest possible results which are present. For the challenge, I used ```cd /ch*```, followed by ```ls``` and ```./run``` to get the flag `oC6pYKqGBpRL5XhSXGSne8CCScM.dFjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/967366d0-8deb-4bab-b4bd-d34cb52db13d)

## Matching with ?
Similar to the previous problem, with the only difference being that `?` acts as a placeholder for only a single element. To solve, I used ```cd /?ha??enge``` followed by
```./run```, which returned the flag `kte4Ix4qkg-CaWjqPKcJjJBtglu.dJjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/2a93ef26-05c2-4fde-8648-7c1122aeb235)

## Matching with []
This taught me to use `[]` to almost *list* out the possible values that can be taken as placeholders. For solving, the first thing I did was run ```cd /challenge/files```, followed by ```/challenge/run file_[bash]``` which gave the flag `kyWcuc-k5Cg47KHQZNKckcRaZ4E.dNjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/fdea18df-a5e5-492d-acff-cb08d29981da)

## Matching paths with []
This one took me a while to grasp, since I skimmed through the instructions and made a mistake. However, after figuring it out, it was simple enough. Only difference between this and the previous problem was that for the argument here, I had to specify a file path, rather than the file itself. The commands are as follows, ```/challenge/run /challenge/files/file_[bash]```, which gave me the flag `EGy6VYuf5iQ-CLr2OxnXp0Hxhmv.dRjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/a922dd59-10e9-42f2-999f-31a972ffdbb9)

## Mixing globs
This took me quite some time to figure out, since I was trying to focus on finding an efficient combination of globs that would return the exact words, without focusing on the list of words present. Upon noticing that they all start with separate alphabets, it was an easy problem. First, I executed ```cd /challenge/files``` followed by ```../run [cep]*```, which gave me the flag `cZRGoYH-gWGkirQbQPzR9TYVHar.dVjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/e3f3926a-0133-4572-afa1-ddd640ec51e7)

## Exclusionary Globs
Compared to the previous problem, this was a much more intuitive and simple challenge. All I had to do was provide which characters *not* to use and the job was done. I used ```cd /challenge/files``` first, to get to the desired directory, followed by ```/challenge/run [^pwn]*``` to get the flag 
`grRsz4-3aWRYiLD-vcsokMTeqXy.dZjM4QDL0UTN0czW`

![image](https://github.com/user-attachments/assets/8367cd48-fdac-46f3-b31a-1928754bbbf7)
