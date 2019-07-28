#cloud-config
output : { all : '| tee -a /var/log/cloud-init-output.log' }

repo_update: true
repo_upgrade: all


packages:
  - htop
  - tcpdump
  - telnet

runcmd:
 - echo "*       hard  nofile 65535" >> /etc/security/limits.conf
 - echo "*       soft  nofile 65535" >> /etc/security/limits.conf
 - echo "*       hard  nproc 65535" >> /etc/security/limits.conf
 - echo "*       soft  nproc 65535" >> /etc/security/limits.conf
 - /etc/eks/bootstrap.sh --apiserver-endpoint '${eks_cluster_endpoint}' --b64-cluster-ca '${eks_cluster_ca}' '${eks_cluster_name}'
