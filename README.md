Rotor Control Webinterface
==========================

## Requirements

- Debian 7.x mit
 - python-flask
 - python-libhamlib2
 - Webserver nach Wahl
- Client-PC mit Browser

## Instructions

1. Start [Rotor Control](http://gitlab.stefan-urban.de/stefan.urban/rotor-control) as a daemon
2. Start `server-side/server.py` script on the same machine
3. Install a webserver (apache, nginx) and make the content of `client-side` available for client users
4. On a client computer, open browser and navigate to server directory from step 3


## To-Dos:

- Configuration in general
- Implement set position
- Is the orientation of the compass really correct?
