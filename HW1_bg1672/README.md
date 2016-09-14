
I set up my environment I made a directory on compute called PUI2016_bg1672. Then I set the environmental variable called PUI2016 that would shorthand the entire path of this directory that I just made.

I was somewhat confused as to how to set this environmental variable.  I used the tutorial from this website to guide my process: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps

![Screenshot] (https://github.com/bfg2105/PUI2016_bg1672/blob/master/HW1_bg1672/Screen%20Shot%202016-09-14%20at%202.04.13%20PM.png)

![Screenshot] (https://github.com/bfg2105/PUI2016_bg1672/blob/master/HW1_bg1672/Screen%20Shot%202016-09-14%20at%202.04.50%20PM.png)



I experimented by following along this tutorial.  I was able to use the export command to set the variable name to the path.  I then was able to save this to the .bashrc file by opening that file using the VI text editor and adding the export command.  From my understanding, everytime I log in, that file will run, and since that line is written it, it will issue that command on its own, so that I have that variable established every time automatically.

I did the same thing with the alias.  I used the source command -based on the instructions from the above tutorial to establish the variable and alias in my current shell session.
