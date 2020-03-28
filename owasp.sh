#!/bin/bash
for i in $(ps aux | grep zap | grep -v grep | awk '{print $2}'); do kill -9 $i; done
cd /usr/share/owasp-zap
./zap.sh -daemon -config api.key="6ojksn3a4nnepjm4ju03hh7rio" -port 8089 -config api.addrs.addr.name=".*" -config api.addrs.addr.regex=true
sleep 5
