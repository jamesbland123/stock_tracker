# Sample Flask application with Docker, UWSGI, & NGINX

Requirements: docker

build the image
```
docker build -t flask_image .
```

run
```
docker run -d -p 8080:80 flask_image
```

Using your browser connect to http://localhost:80 or in Cloud9 preview

If everything worked as expected you should see a json response

##testing

Gets --
curl http://localhost:8080
curl http://localhost:8080/car/1
curl http://localhost:8080/car/2


Puts --
curl http://localhost:8080/car/5 -d "data=camry" -X PUT



