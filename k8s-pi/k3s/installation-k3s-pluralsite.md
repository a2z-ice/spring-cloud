Burn image using Raspberry Pi Imager
Go to custom setting and enable ssh which will automatically enable ssh connection

The hootoo router information

# http://10.10.10.254/app/network/wifi.html
```sh
User: admin
Password: WtrwG6Y8ec6w

Wifi:
Network: assad
Password: hinds -> **051
```
# Using LanScan software get the necessary ip address with mac address
```sh
ssh node4d@10.10.10.3
```
# If any error occur during ssh run the following command to regenerate the ssh finger print for the ip 10.10.10.3
```sh
ssh-keygen -R 10.10.10.3
```
# To create ssh connection
```sh
Run ssh-keyge command on the pc from where you want to connect the raspberry pi
ssh-keygen
Copy ~/.ssh/id_rsa.pub file content to raspberry pi to do this run following command
cat ~/.ssh/id_rsa.pub | ssh node4d@10.10.10.3 “cat >>~/.ssh/authorized_keys”

```

# Installation

```sh
sudo apt-get update
# change host name and exit from raspberry pi then login and see the host name has changed
sudo hostnamectl set-hostname node25
# check is the swapon run following command
sudo swapon # if there is not output then swapon is disabled

sudo nano /boot/firmware/usercfg.txt
# To disable wifi. If you want to lan (wired) connection
dtoverlay=disable-wifi
dtoverlay=disable-bt


# Configure linux control group
sudo nano /boot/firmware/cmdline.txt #go to the end of the first line and add following in same line start with space
cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory swapaccount=1 # after adding this to cmdline.txt reboot raspberry pi
sudo reboot

```