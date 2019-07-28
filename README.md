# jupyterhub-kubernetes
Helm install jupyterhub and deploy mysql manually

### Auth
OAuth with Github.

### Helm (install jupyterhub)

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

### javascript support

jupyterhub-singleuser use image below
```
davidh83110/jupyter-k8s-singleuser-javascript:0.7.0
```

build
```
docker build -t singleuser . -f Dockerfile_singleuser
```

### MySQL

`deploy`
```
cd mysql && kubectl apply -f mysql-deployment.yaml && \
    kubectl apply -f mysql-pv.yaml
```

### U.S. Congress Member to MySQL

us_congress.members (PK=ID, auto increment)
Get member json list from US github repo [LINK](https://theunitedstates.io/congress-legislators/legislators-current.json)

`python3 and pymysql`
```
python3 congress_cralwer.py
```

`columns`
||ID(PK)  ||Name ||party ||state ||office address ||office phone ||start date ||end date ||


### Terraform with EKS

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









