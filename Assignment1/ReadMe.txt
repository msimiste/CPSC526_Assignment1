Name: Mike Simister
StudentID: 10095107
Tutorial Section: T02

This program functions as a backdoor on a linux machine.

To run the program:

(1) From the directory containing the assign1.py file:

	(1a)From cmd line type: python assign1.py <ipaddress> <port>
	
	
(2)From the local machine or from another machine:
	
	(2a)From cmd line type: nc <ipaddress> <port> (Making sure that the <ipaddress> and <port> match in both cases.)
	
	(2b)From the password prompt, type CPSC526 so the cmd line looks like:
		Password:CPSC526

(3)Supported Commands:

	Commands
	
cat <file> 	 display a file
cd 		 change current working directory
help 		 shows a list of commands
ls [agrs] 	 list current directory contents
off 		 shuts down the program (server side)
who 		 lists the users who are currently logged in
ps 		 shows the current running processes
pwd 		 returns the current working directory
who 		 lists the users currently logged in

***NOTE*** 	This program will execute all linux commands


(4)Known bugs:

	(4a)The program does NOT support tab-completion. 

	(4b)Additionally, after entering a command and receiving output
	do NOT hit "enter". It is imperative that the user enters the next command without hitting the "enter" button
	on the keyboard.
