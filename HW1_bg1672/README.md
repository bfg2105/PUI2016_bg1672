
I set up my environment I made a directory on compute called PUI2016_bg1672. Then I set the environmental variable called PUI2016 that would shorthand the entire path of this directory that I just made.

I was somewhat confused as to how to set this environmental variable.  I used the tutorial from this website to guide my process: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps

![Screenshot 1] (PUI2016_bg1672/HW1_bg1672/Screen Shot 2016-09-14 at 2.04.13 PM.png)

![Screenshot 2] (PUI2016_bg1672/HW1_bg1672/Screen Shot 2016-09-14 at 2.04.13 PM.png)



I experimented by following along this tutorial.  I was able to use the export command to set the variable name to the path.  I then was able to save this to the .bashrc file by opening that file using the VI text editor and adding the export command.  From my understanding, everytime I log in, that file will run, and since that line is written it, it will issue that command on its own, so that I have that variable established every time automatically.

I did the same thing with the alias.  I used the source command -based on the instructions from the above tutorial to establish the variable and alias in my current shell session.
