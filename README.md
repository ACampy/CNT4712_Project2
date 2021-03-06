# PAINT WITH FRIENDS - CLIENT AND SERVER 
Developer: Jorge Velez (@jorvel) & Alex Campaneria (@ACampy)

## Server
### Usage 
`server.py [-c <configFile>] [-p <port>] [-m <max_connections>] [-t <server_timeout>] [-l <state_file>]`
    
To use this chat server program, please use Python 3.6. You can execute it on a command line as shown above
To run the server without options, please type:
    `python server.py`
        
This will run the server with the following default settings:
```
    port:               8300
    Max Connections:    10
    Timeout:            3
    Config path:        "conf/drawserver.conf"
    Location of save:   NONE
```

A description of the individual command line arguments can be found below. Either a single letter
or the full option can be used for each option. As an example, both -c and --configfile have the
same functionality:

  Arguments:
```
-c, --configfile        - Specifies a config file to get default values from
-p, --port              - Specifies a default port for the server to use
-m, --max               - Specifies the maximum number of people that can connect to the server
-t, --timeout           - Specifies the default server timeout
-l, --load              - Load a stored canvas from a previous session
```


### Storing a canvas

As shown above, it is possible to specify a location to save the state of the canvas. If no data
is currently stored at the specified location, then a new file will be created at runtime. At the 
end of a session, the server will write the current state of the canvas to that file, allowing the
server operator to load it again the next time the server is run.

### Config

The default provided config file is found in conf/drawserver.conf
The parameters accepted in this .conf file are:
```
port                - default port to run the server with
max_connections     - the max number of connections the server will receive
timeout             - the default server timeout, given in seconds
```

## Client

   ### Usage 
`python PaintWithFriends.py`

To use this chat client program, please use Python 3.6.
    
  ### Basic usage

Paint with Friends is designed to be an online paint experience, and as such a user cannot draw on the 
canvas without being connected to a server. Upon opening it, you will find the drawing canvas in the 
center of the screen. The chat window is found to the left, and a selection of colors/drawing tools can 
be found around the perimiter of the canvas.

To connect to a server, use the dialog box on the top left. Once connected, you will be prompted to 
enter a username via the chat window. After entering this nickname, the client will pause and render all
the drawing that has already been done on the server by other users. This process may take some time, so 
please be patient. Once the canvas has been rendered, a user can use several drawing tools and colors to 
draw on the canvas. The rainbow button on the bottom left allows a user to use a more fleshed out color 
picker. Any drawings done by a user will be transmitted to all other users. A user can also communicate with 
other users on the same server by typing into the chat on the left.

If a user would like the entirely wipe the canvas clean, there is an option to do so on the top. This option
will ask for a user's confirmation before initiating the wipe, and will inform all other users via chat who 
deleted the canvas contents. This action is permanent and cannot be undone. 

To disconnect from a server, a user must click the Disconnect button on the top of the program. The program will
then prompt the user for confirmation before exiting.
