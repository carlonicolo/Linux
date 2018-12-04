#!/bin/bash      
#title           	: update.sh
#description     	: This script will execute the command: apt update,upgrade,dist-upgrade and autoremove
#					  with the colored title of the command					  
#author		 		: Carlo Nicolò aka Karlitos
#usage		 		: ./update.sh
#==============================================================================

# Constant
RED="\033[0;31m"
LGREEN="\033[1;32m"
YELLOW="\033[1;33m"
PURPLE="\033[0;35m"
NC="\033[0m"

echo "\n"
echo "${RED}********** UPDATE **********${NC}"
apt update
echo "${RED}******** END UPDATE ********${NC}"

echo "\n"
echo "${LGREEN}********** UPGRADE **********${NC}"
apt upgrade
echo "${LGREEN}******** END UPGRADE ********${NC}"

echo "\n"
echo "${YELLOW}********** DIST-UPGRADE **********${NC}"
apt dist-upgrade
echo "${YELLOW}******** END DIST-UPGRADE ********${NC}"

echo "\n"
