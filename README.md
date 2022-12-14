# ML Assignment
Please implement a translation inference service that runs on Kubernetes and provides a RESTful API on port 9527.

The translation model is `M2M100`, and the example can be found in `app/translation_example.py`.

You should first fork this repository, and then send us the code or the url of your forked repository via email. 

**Please do not submit any pull requests to this repository.**

## Prerequisite
Minikube, Kubenetes, Docker

## Start Project
Start Minikube
```bash
minikube start --cpus 4 --memory 6144MB
```
Create translation-service and translation-app deployment
```bash
kubectl apply -f k8s/deployment.yaml
```
To examine whether the service has successfuly starts, you can use
```bash
kubectl get pods
kubectl logs -f deployment/translation-app
```
After the service completely starts, port forward to port 9527
```bash
kubectl port-forward service/translation-service 9527:8000
```

## Delivery
- **app/Dockerfile**: To generate an application image
- **k8s/deployment.yaml**: To deploy image to Kubernetes
- Other necessary code

## Input/Output

When you execute this command:
```bash
curl --location --request POST 'http://127.0.0.1:9527/translation' \
--header 'Content-Type: application/json' \
--data-raw '{
    "payload": {
        "fromLang": "en",
        "records": [
            {
                "id": "123",
                "text": "Life is like a box of chocolates."
            }
        ],
        "toLang": "ja"
    }
}'
```

Should return:
```bash
{
   "result":[
      {
         "id":"123",
         "text":"人生はチョコレートの箱のようなものだ。"
      }
   ]
}
```

## Bonus points
- Clean code
- Scalable architecture
- Good inference performance
- Efficient CPU/GPU utilization
