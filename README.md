# Flask Restful API Quick Start
---

A quick project to create restful api with flask

## Usage

1. Bulid docker image

```shell
docker build -t flask-rest-test .
```

2. Run image

```shell
docker run  -p 5000:5000  flask-rest-test
```

3. Access [Swagger Document](http://localhost:5000/apidocs)

``` shell
http://localhost:5000/apidocs
```