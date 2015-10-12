#!/bin/bash

# connect to your freifunk (ff) router, get clients 
# MAC Prefix: 18:fe:34=Espressif Inc.
macp="18:fe:34"
iwdev="client0"
pubkey="$HOME/.ssh/id_rsa.pub"
if [ -f "$pubkey" ] ; then 
	sshopts="-i $pubkey"
fi

# to find out the iw device:
# iwdev=$(ssh root@172.21.24.254 iwinfo | grep Freifunk| awk '{print $1}')

# ff next node IP: 172.21.24.254
# you need to have key-based ssh access to your ff router 
# https://wiki.freifunk-stuttgart.net/anleitungen:config_mode:start#fernzugriff

ssh $sshopts root@172.21.24.254 iw dev $iwdev station dump | grep $macp

