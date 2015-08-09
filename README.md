# xsession-chooser-pygtk
A GUI to choose what xsession (e.g., GNOME, GNOME Classic, KDE) to launch after an X server is started

# What problem does this solve

Typically when you login locally to a Linux system with X11, [the display manager lets you choose which xsession to launch.](http://dominique.leuenberger.net/blog/wp-content/uploads/2013/04/GDM38.png) Common examples of sessions are GNOME, GNOME Classic, GNOME Flashback, and KDE. Each desktop environment typically provides one or more xsession.

[Most remote desktop solutions for X11, such as TigerVNC, rely on scripts to launch the preferred xsession from a list of available xsessions, or a manually specified xsession.](https://rbgeek.files.wordpress.com/2012/06/nu4.jpg) However, if you want to launch an xsession other than the preferred/manual xsession, you have to edit a script.

[Some remote desktop solutions for X11, such as X2Go, let you pick the xsession before you connect via the client.](https://farm9.staticflickr.com/8730/16365755693_75f3d544e9_b.jpg) This approach has advantages, but the disadvantage is that the client usually lists xsessions that are not installed on the server.

xsession-chooser-pygtk solves this problem for the former group of remote desktop solutions, and is an alternative approach for the latter group of remote desktop solutions. With xsession-chooser-pygtk, the user selects an available session from a GUI after connecting to the remote desktop session with the client.
 
xsession-chooser-pygtk is not limited to remote desktop solutions. It is usable with local X server commands like `startx`.

# Status

**As the current version number implies, xsession-chooser-pygtk is very much incomplete and rough around the edges.**

At this time, it should be considered a proof of concept, and a useful tool for users who know the Linux OS well.

**Currently, you must edit your scripts (like ~/.Xclients for TigerVNC on Fedora) to launch xsession-chooser-pygtk.**

