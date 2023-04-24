#!/bin/bash
# This script will check the selinux value in both bash and /etc/sysconfig/selinux

# This block checks selinux value in /etc/sysconfig/selinux
echo "=============================================================="
echo -e "Checking Selinux value in /etc/sysconfig/selinux:\n"

mode=$(grep ^SELINUX /etc/sysconfig/selinux | head -1 | cut -f2 -d'=')
case $mode in
        "permissive") echo "Selinux is in PERMISSIVE mode in /etc/sysconfig/selinux"; 
                  ;;
        "disabled") echo "Selinux is in DISABLED mode in /etc/sysconfig/selinux";
                  ;;
        "enforcing") echo "Selinux is in ENFORCING mode in /etc/sysconfig/selinux"; 
                     echo $(date) > /tmp/selinux-file;
                     echo "Selinux is in ENFORCING mode in /etc/sysconfig/selinux" >> /tmp/selinux-file;
                     echo "Updating Selinux value in /etc/sysconfig/selinux:";
                     echo "Updating Selinux value in /etc/sysconfig/selinux:" >> /tmp/selinux-file;
                     sed -i 's/^SELINUX=enforcing/SELINUX=permissive/' /etc/sysconfig/selinux;
                     echo "Value of selinux in /etc/sysconfig/selinux:" >> /tmp/selinux-file;
                     echo "Value of selinux in /etc/sysconfig/selinux:";
                     sed -n 7p /etc/sysconfig/selinux;
                     sed -n 7p /etc/sysconfig/selinux >> /tmp/selinux-file;                    
                  ;;
esac
echo "=============================================================="
echo "=============================================================="

# This block checks selinux value in bash
echo -e "Checking Selinux value in bash:\n"
case $(getenforce) in
        "Permissive") echo "Selinux is in PERMISSIVE mode in bash"; 
                  ;;
        "Disabled") echo "Selinux is in DISABLED mode in bash";
                  ;;
        "Enforcing") echo "Selinux is in ENFORCING mode in bash";
                     echo $(date) > /tmp/selinux-bash
                     echo "Selinux is in ENFORCING mode in bash" >> /tmp/selinux-bash;
                     echo "Updating Selinux value in bash";
                     echo "Updating Selinux value in bash" >> /tmp/selinux-bash;
                     setenforce 0;
                     echo "Value of selinux in bash:" >> /tmp/selinux-bash;
                     echo "Value of selinux in bash:";
                     getenforce;
                     getenforce >> /tmp/selinux-bash;                
                  ;;
esac
echo "=============================================================="
