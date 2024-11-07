```sh
docker build -t flask-smorest-api .


docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api

# test url
http://localhost:5000/item
```