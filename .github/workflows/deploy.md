az login
az aks create --name myAKSCluster --resource-group myResourceGroup
az acr create -n MyRegistry -g MyResourceGroup --sku Standard
az aks install-cli
docker build -f Dockerfile -t tasklist:latest
kubectl apply -f “tasklistwsb\deployment.yml”
kubectl get services --watch
