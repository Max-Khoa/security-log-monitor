#!/bin/bash

systemctl start ssh
systemctl start ssh.socket
echo "SSH started"