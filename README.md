# KubernetesIris

Déploiement avec Kubernetes

## Architecture des dossiers
├── client/ │ ├── app.py │ ├── Dockerfile │ ├── requirements.txt │ └── k8s/ │ ├── deployment.yaml │ └── service.yaml ├── server/ │ ├── model.pkl │ ├── train.ipynb │ ├── k8s/ │ │ ├── deployment.yaml │ │ └── service.yaml │ ├── v0.1.0/ │ │ ├── app.py │ │ ├── Dockerfile │ │ ├── model_v1.pkl │ │ └── requirements.txt │ ├── v0.2.0/ │ │ ├── app.py │ │ ├── Dockerfile │ │ ├── model_v2.pkl │ │ ├── model_v3.pkl │ │ └── requirements.txt │ └── v0.3.0/ │ ├── app.py │ ├── Dockerfile │ └── requirements.txt

## Instructions pour lancer l'application

### Étape 1 : Construire les images Docker

#### Client
1. Se placer dans le dossier `client` :
   ```bash
   cd client
   ```
2. Construire l'image Docker :
   ```bash
  docker build -t mlops-client:latest .
   ```

#### Server
1. Se placer dans le dossier de chaque version (v0.1.0, v0.2.0, v0.3.0) :
   ```bash
   cd server/v0.2.0
   ```
2. Construire l'image Docker pour chaque version en changeant le tag :
   ```bash
   docker build -t mlops-server:0.2.0 .
   ```
Répétez ces étapes pour chaque version du serveur (`v0.1.0`, `v0.2.0`, `v0.3.0`).  
Pour déployer une version spécifique, indiquez l'image correspondante dans votre fichier `deployment.yaml` :

```yaml
spec:
    containers:
        - name: mlops-server
            image: mlops-server:0.2.0  # Remplacez par la version souhaitée
            imagePullPolicy: Always
```

### Étape 2 : Déployer avec Kubernetes

#### Server
1. Se placer dans le dossier `server/k8s` :
    ```bash
    cd server/k8s
    ```
2. Appliquer les fichiers de déploiement et de service :
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

#### Client
1. Se placer dans le dossier `client/k8s` :
    ```bash
    cd client/k8s
    ```
2. Appliquer les fichiers de déploiement et de service :
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

### Étape 3 : Accéder à l'application

- **Interface utilisateur** : [http://localhost:30002/](http://localhost:30002/)
- **Documentation de l'API** : [http://localhost:30001/docs](http://localhost:30001/docs)

Le déploiement utilise une stratégie de mise à jour continue (*RollingUpdate*) pour garantir une disponibilité constante pendant les mises à jour. Consultez les fichiers YAML dans les dossiers `k8s` pour plus de détails.


