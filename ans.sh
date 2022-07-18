#!/usr/bin/expect -f

set user [lindex $argv 0]
set pswd [lindex $argv 1]
set path [lindex $argv 2]
    
set timeout -1

spawn ./rep.sh $path

for {set i 0} {$i < 80} {incr i 1} {

expect {
    "Username " { send -- "$user\r" }
    "Password " { send -- "$pswd\r" }
	}
}

exit
expect eof


