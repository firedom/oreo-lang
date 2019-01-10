# oreo-lang

Someday I found a quite funny demo about OREO[1],  and translate the OREO to morsecode seems a good idea[2].

So let's set:

奥 -> ·

利 -> -

与 -> / （used for isolated every character）

And this is encode table for OREO code.

| character | morse code | OREO code |
| ------ | ------ | ------ |
| A|  ·－  |奥利 | 
| B|  －···  |利奥奥奥 | 
| C|  －·－·  |利奥里奥| 
| D|  －··  |利奥奥|
| E|  ·   |奥|
| F|  ··－·  | 奥奥利奥| 
| G|  －－·  |利利奥|
| H|  ····  | 奥奥奥奥| 
| I|  ··   |奥奥| 
| J|  ·－－－ |奥利利利 | 
| K|  －·－  | 利奥利|
| L|  ·－··  | 奥利奥奥|
| M|  －－ | 利利|
| N|  －·  | 利奥|
| O|  －－－  | 利利利   |
| P|  ·－－·  |  奥利利奥|
| Q|  －－·－  |   利利奥利|
| R|  ·－·   |  奥利奥|
| S|  ···   | 奥奥奥 |
| T|  －  | 利 |
| U|  ··－  |   奥奥利|
| V|  ···－  |   奥奥奥利|
| W|  ·－－  |   奥利利|
| X|  －··－  |   利奥奥利|
| Y|  －·－－  |  利奥利利|
| Z|  －－··  |    利利奥奥|
| 0|  －－－－－  |  利利利利利|
| 1|  ·－－－－ |   奥利利利利|
| 2|  ··－－－ | 奥奥利利利|
| 3|  ···－－ |  奥奥奥利利|
| 4|  ····－ |   奥奥奥奥利|
| 5|  ·····  |   奥奥奥奥奥|
| 6|  －···· |   利奥奥奥奥|
| 7| －－···  |   利利奥奥奥|
| 8| －－－··  | 利利利奥奥|
| 9| －－－－· |   利利利利奥|

# How to use
oreo.py

If you want translate words, input:  
python3 oreo.py nyanya~
The Terminal will return:  
<p>利奥与利奥利利与奥利与利奥与利奥利利与奥利与~</p>    

Or translate sentence, input:  
python3 oreo.py "Author by firedom"  
The Terminal will return:  
<p>奥利与奥奥利与利与奥奥奥奥与利利利与奥利奥与  利奥奥奥与利奥利利与  奥奥利奥与奥奥与奥利奥与奥与利奥奥与利利利与利利与</p>  

jsoreo.py

This python file is designed for OREO cookie pages[3], open this site and run jsoreo.py in Terminal to get morsecode format list.

e.g.:
Input this command in Terminal:

$ python3 jsoreo.py abcd

Termianl will return this:

app.oreoArr =  ['O', 'R', '-', 'R', 'O', 'O', 'O', '-', 'R', 'O', 'R', 'O', '-', 'R', 'O', 'O', '-']


next, copy result and paste it to Console of Explorer.

finally click Generate and this site will return a picture like this:

!(Ore-reooo-reoreo-reoo.png)

Also you can do any thing you want, enjoy.

------------

If you want translate words, input:\
python3 jsoreo.py nyanya\
The Terminal will return:\
app.oreoArr =  ['R', 'O', '-', 'R', 'O', 'R', 'R', '-', 'O', 'R', '-', 'R', 'O', '-', 'R', 'O', 'R', 'R', '-', 'O', 'R', '-']

Or translate sentence, input:\
python3 jsoreo.py "Author by firedom"\
The Terminal will return:\
app.oreoArr =  ['O', 'R', '-', 'O', 'O', 'R', '-', 'R', '-', 'O', 'O', 'O', 'O', '-', 'R', 'R', 'R', '-', 'O', 'R', 'O', '-', 'R', 'O', 'O', 'O', '-', 'R', 'O', 'R', 'R', '-', 'O', 'O', 'R', 'O', '-', 'O', 'O', '-', 'O', 'R', 'O', '-', 'O', '-', 'R', 'O', 'O', '-', 'R', 'R', 'R', '-', 'R', 'R', '-']



# Reference:
[1]https://www.v2ex.com/t/525308

[2]https://www.v2ex.com/t/525308#reply7

[3]https://ddiu.site/oreooo/
