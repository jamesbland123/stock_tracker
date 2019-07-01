# Sample Flask application with Docker, UWSGI, & NGINX

Requirements: docker

build the image
```
docker build -t stock_tracker .
```

run
```
docker run -d -p 8080:80 stock_tracker
```

Using your browser connect to http://localhost:80 or in Cloud9 preview

If everything worked as expected you should see a json response

##testing

Gets --
curl http://localhost:8080
curl http://localhost:8080/stock/1
curl http://localhost:8080/stock/2


Puts --
curl http://localhost:8080/stock/5 -d "data=WORK" -X PUT



