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
sudo apt-get upgrade
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

# backup raspberry pi image from sd card us dd command from mac or linux and use Win32 Disk Imager from windows

# to check memory run 
htop

# Go to k3s.io and follow the instruction there like followings
curl -sfL https://get.k3s.io | sh -  # First copy this on control panel then go for other
# Check for Ready node, takes ~30 seconds 
sudo k3s kubectl get node 

sudo kubectl cluster-info

# configure kubectl from other pc to pi-cluster 
# Go to kubernetes document to install kubectl on the mac kubernetes.io/docs
# After kubectl installation do the necessary to connect the install kubectl with pi clauster
# Create .kube folder to home 

mkdir ~/.kube

# run following command to get the kubectl configuration detail
kubectl get pods # This will show error with specific configuration kubectl configuration which the following

/etc/rancher/k3s/k3s.yaml

# Now copy the k3d kubectl config file to mac
ssh node4d@10.10.10.3 "sudo cat /etc/rancher/k3s/k3s.yaml" > ~/.kube/config

# After copying the config file try to access 
kubectl get nodes # which will show error . See the content of config you will noticed that https://127.0.0.1:6443 will be there which is for localhost so you have to replace the if of https://127.0.0.1:6443 with raspberry pi controll panel ip like https://10.10.10.3:6443 

# Now try to run kubectl command from mac
kubectl get nods

# To install kubernetes dashboard follow the kubernetes dashboard instruction
https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/

# Now create service account and  cluster role bindings with cluster-admin role which created by default
sudo kubectl create serviceaccount dashboard-admin --namespace-kubernetes-dashboard
sudo kubectl create clusterrolebinding dashboard-admin --clusterrole=cluster-admin --serviceaccount=kubernetesh-dashboard:dashboard-admin
# Now describe newly created service account
sudo kubectl describe serviceaccount dashboard-admin --namespace=kubernetes-dashboard
# Now describe the secret from the service account like following example
sudo kubectl describe secret dashboard-admin-token-n4fh # describe secret with your specific secret name
# To run dashboard without Nodeport or LB use kubectl proxy

kubectl proxy

```

# Prepare More raspberry pi to add more pi to the cluster

```sh
# To check each worker node can access the kube-api server do telnet
telnet ${ip_address_of_control_panel}
# To get the secrete token from control panel to join the other node to the cluster
sudo cat /var/lib/rancher/k3s/server/node-token
# Now from each worker not run the following command to join to k3s cluster
curl -sfL https://get.k3s.io | K3S_URL=https://$IP_ADDRESS_OF_CONTROL_PANEL:6443 K3S_TOKEN=$VALUE_OF_TOKEN_GET_FROM_CONTROL_PANEL sh -

# To automate adding nodes to cluster
# k3sup which use to faster installation of k3s docs : https://github.com/alexellis/k3sup
# Go to your mac and install/download k3sup then run following command
k3sup join --ip $IP_ADDRESS_OF_WORKER_NODE --server-ip $IP_ADDRESS_OF_CONTROL_PANEL --user ubuntu
```