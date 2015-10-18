# Learning PyGTK for Linux Apps

There is GTK2 and GTK3, both are compatible with Ubuntu, Debiant, Mint, XFCE, etc.

[Docs PyGTK2: http://www.pygtk.org/pygtk2reference/](http://www.pygtk.org/pygtk2reference/)
[Docs PyGTK3: http://www.pygtk.org/pygtk2reference/](https://python-gtk-3-tutorial.readthedocs.org/en/latest/)
[Docs PyGTK3: https://developer.gnome.org/gtk3/stable/](https://developer.gnome.org/gtk3/stable/)
[Windows PyGTK: http://www.pygtk.org/downloads.html](http://www.pygtk.org/downloads.html)

## GUI Developer
I would not recommend this to produce code because I won't learn the code as
well and it adds a LOT of extra code. It can be used to help understand certain commands if you want.

    sudo apt-get install glade

# Ubuntu: Quickly
You can create a GUI app this way also:

    sudo apt-get install quickly
    quickly create ubuntu-application your_app_name

### Edit the Quickly App
You can edit your application in glade with:

    cd your_app_name
    quickly design

### Edit the Quickly Python
If I created a project called `sackentosh`, to edit python I'd edit the `SackentoshWindow.py` (The name of your project) file to start with:

    vim sackentosh/sackentosh/SqlWindow.py


### Compiling

[Docs: https://wiki.gnome.org/action/show/Projects/PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject)