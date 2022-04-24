

## Task Lista

Tworzenie bazy postgre na azure:
```
az postgres flexible-server create --location northeurope --resource-group mmgroup \
  --name mmpostgreserver --admin-user taskadmin --admin-password password \
  --sku-name Standard_B1ms --tier Burstable --public-access all --storage-size 32 \
  --tags "app=micromanager" --version 13 --high-availability Disabled --zone 1 \
  --standby-zone 3
  ```
  
 Tworzenie klastera AKS \ ACR:
 ```
 az acr create -n MyRegistry -g MyResourceGroup --sku Standard
 
 az aks create --name myAKSCluster --resource-group mmgroup

 ```
 Docker build image \ k8s:
 
 ```
 docker build -f Dockerfile -t tasklist:latest

 kubectl apply -f “tasklistwsb\deployment.yml”
 
 kubectl get services --watch

 ```
 

**1. Założenia projektowe:**

- Do korzystania z aplikacji wymagane jest konto użytkownika.

- Istnieją dwa typy użytkowników (User, Admin).

- Każdy z użytkowników ma wgląd do własnej/własnych Task list/y.

- Administrator może zarządzać wszystkimi Task listami (wszystkich użytkowników), dodawać oraz usuwać z nich elementy.

  

**2. Wymagania funkcjonalne i niefunkcjonalne.**

- Funkcjonalne:

  - rejestracja użytkownika i ekran logowania

  - przyciski obok wpisu z zadaniem, które umożliwiają edytowanie wpisu, zaktualizowanie, usunięcie

  - przycisk z dodaniem wpisu

- Niefunkcjonalne:

  - aplikacja jest dostępna z poziomu przeglądarki internetowej

  - aplikacja jest dostępna w wersji mobilnej

  - aplikacja ma za zadanie pomóc w zaplanowaniu czynności do zrobienia

  

**3. Wybrane technologie**

- Python

- Flask

- Docker

- Kubernetes

  

**4. Środowiska chmurowe.**

- Azure

- Github

  

**5. Historyjki użytkownika**

- Jako użytkownik dodaję nowe zadanie do listy

- Jako administrator usuwam dowolnego użytkownika

- Jako administrator usuwam zadanie dowolnego użytkownika

- Loguję się do aplikacji za pomocą loginu i hasła

- Jako nowy użytkownik mogę się zarejestrować

- Jako użytkownik dodaję nową listę

  

Grupa: Michał Rewak, Andrzej Świtała, Leonid Stasyuk, Enrico Illiano


# Yolo Web APP
This is web application where you upload an image and get image with predicted bounding boxes. 
Using pretrained YOLO model by ultralytics https://ultralytics.com.

## Prerequisites
1. Ubuntu 18.04 OS
2. Installed:
   - azure-cli
   - kubectl
   - docker
## Application Deployment
### Setup Variables
   ```bash
    AKS=takslistwsb-aks
    ACR=takslistwsbegistry001
    GROUP=wsbgroup1
    LOCATION=westus
   ```
### Docker Image
Build docker image
   ```bash
   docker build -t takslistwsb .
   ```
Test docker image
   ```bash
    docker run -it --rm  takslistwsb:latest
   ```
### Initial Azure Setup
Login to azure
   ```bash
    az login
   ```
Create resource group
   ```bash
    az group create -l $LOCATION -n $GROUP
   ```
Debug: Check resource group
   ```bash
    az group list
   ```
Debug: Check if properly logon
   ```bash
    az account list    
   ```
### Create a container registry
   ```bash
    az acr create -n $ACR -g $GROUP --sku basic
    az acr login --name $ACR
   ```
### Push docker image to container registry
   ```bash
    docker tag takslistwsb:latest takslistwsbegistry001.azurecr.io/takslistwsb:v1
    docker push takslistwsbegistry001.azurecr.io/takslistwsb:v1
   ```
## Azure Kubernetes Deploy
Create Azure Kubernetes Service with acr attached to use our docker image
   ```bash
    az aks create -n $AKS -g $GROUP --generate-ssh-keys --attach-acr $ACR
    az aks get-credentials -g $GROUP -n $AKS
   ```
Setup kubectl service
   ```bash
    kubectl apply -f takslistwsb.yml
   ```
Get public ip and paste in browser
   ```bash
    kubectl get service takslistwsb-svc --watch
   ```






