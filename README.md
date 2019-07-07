# Sample Flask application with Docker, UWSGI, & NGINX

Requirements: docker and docker-compose

build and run the image
```
docker-compose up web
```


Using your browser connect to http://localhost:8080 or in Cloud9 preview

If everything worked as expected you should see a table flip 

##testing

```
./test_runner.sh
```

***To test manually***
Gets --
curl http://localhost:8080/api/v1
curl http://localhost:8080/api/v1/stock/AMZN
curl http://localhost:8080/api/v1/stock/NFLX

Puts --
curl http://localhost:8080/api/v1/stock -d "ticker_symbol=WORK" -X PUT

***swagger UI***
browse to /api/vi/ui/  <- don't forget the trailing slash



