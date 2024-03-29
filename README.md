# jupyterhub-kubernetes
Helm install jupyterhub and deploy mysql manually.

[![Build Status](https://travis-ci.org/davidh83110/jupyterhub-kubernetes.svg?branch=master)](https://travis-ci.org/davidh83110/jupyterhub-kubernetes)


`homepage` [https://homework.davidh83110.com](https://homework.davidh83110.com)

<br />

## Multiple Users

Support multiple users and corresponding rols.

![multuple-user](https://live.staticflickr.com/65535/48402303437_f0298b8da7_k.jpg)

<br />

## Auth

OAuth with Github.

![login](https://live.staticflickr.com/65535/48402303362_665bbc8761_k.jpg)

<br />

## Helm (install jupyterhub)

`Install` (Fork by zero-to-jupyterhub-k8s)
```
cd jupyterhub && helm install . --name david-jhub --values config.yaml
```

`Upgrade`
```
helm upgrade  --values config.yaml david-jhub .
```

`Delete`
```
helm delete david-jhub
```

<br />

## javascript support

![js_support](https://live.staticflickr.com/65535/48402303387_112e83cf16_k.jpg)


jupyterhub-singleuser use image below
```
davidh83110/jupyter-k8s-singleuser-javascript:0.7.0
```

`build`
```
docker build -t singleuser . -f Dockerfile_singleuser
```

<br />

## MySQL

`deploy`
```
cd mysql && kubectl apply -f mysql-deployment.yaml && \
    kubectl apply -f mysql-pv.yaml
```

`Create Database`
```
CREATE DATABASE us_congress;
CREATE DATABASE develop;
```

`us_congress.member Table Creation`
```
CREATE table members( `ID` bigint(20) NOT NULL AUTO_INCREMENT primary key, `name` varchar(64), `party` varchar(64), `state` varchar(64), `office_address` varchar(512), `office_phone` varchar(64), `start_date` varchar(64), `end_date` varchar(64) );
```

`develop.test Table Creation`
```
CREATE table test( `ID` bigint(20) NOT NULL AUTO_INCREMENT primary key, `name` varchar(64), `gender` varchar(64) ); 
```

`Show Columns`
```
show columns in TABLE_NAME;
```

Check example.py to know how to connect to MySQL in Python


<br />

## U.S. Congress Member to MySQL

`us_congress.members` (PK=ID, auto increment)

Get member json list from US github repo [LINK](https://theunitedstates.io/congress-legislators/legislators-current.json)

<br />

`python3 and pymysql`
```
python3 congress_cralwer.py
```

<br />

`columns`

||  ID(PK)  ||  Name ||  party ||  state ||  office address ||  office phone ||  start date ||  end date ||

<br />

## Terraform with EKS

Terraform to launch EKS nodes.

`Init`
```
make init
```

`Plan`
```
make plan
```

`Apply`
```
make apply
```

`AWS Auth ConfigMap to add node`
```
cd terraform && kubectl apply -f aws-auth-cm.yml
```

<br />

## Start EKS

A. Launch a EKS cluster on AWS console


B. Add nodes with Terraform
```
cd terraform && make init && make apply
```

C. Set auth to communicate with master
```
kubectl apply -f terraform/aws-auth-cm.yml
```

<br />

## How to start 

A. Set callback URL and homepage on Github


B. Generate an random token 
```
openssl rand -hex 32
```

C. Fill callback URL, server name and token as well as your client and secret to `jupyterhub/config.yaml`


D. Start JupyterHub with Helm chart.
```
cd jupyterhub && helm install . --name david-jhub --values config.yaml
```

E. Check the kubeternetes service status
```
kubectl get svc
```

F. Deploy MySQL
```
kubectl apply -f mysql/mysql-deployment.yaml

kubectl apply -f mysql/mysql-pv.yaml
```

G. Get MySQL service cluster ip
```
kubectl get svc
```

<br />



