#!/bin/sh

# source this before you perform a distributed launch with a remote AutoRally chassis

# This is the Warthog main computer
## export ROS_MASTER_URI="http://cpr-lav07:11311"
COMPUTE_BOX_USERNAME="administrator"
COMPUTE_BOX_HOSTNAME="cpr-lav07"

# (Priority) todo:validate command
#     Pass: clearpath
#     $ssh cpr-lav07 ls /dev/
#     $ssh administrator@cpr-lav07 ls /dev/
#

export ROS_MASTER_URI=http://${COMPUTE_BOX_HOSTNAME}:11311
export MASTER_USER=${COMPUTE_BOX_USERNAME}
export MASTER_HOSTNAME=${COMPUTE_BOX_HOSTNAME}
export HOSTNAME=$(hostname)
export ROSLAUNCH_SSH_UNKNOWN=1
# Find directory of script file to avoid hard-coded paths
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source setupEnvVariables.sh

