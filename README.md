

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
