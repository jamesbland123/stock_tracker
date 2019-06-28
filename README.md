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

If everything worked as expected you should see "¯\(◉‿◉)/¯"


