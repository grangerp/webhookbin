# Webhookbin

Simple app that with 2 endpoints:

* POST /<bin_name> will store the request json to the bin_name
* GET /<bin_name> return json stored by POST

```sh
$ docker build . -t webhookbin
$ docker run -p 9000:9000 webhookbin
$ http :9000/qwerty a=1 b=2
ok
$ http :9000/qwerty
{
    "headers": {
        "Accept": "application/json, */*",
        ...
        "X-Waws-Unencoded-Url": "/test1"
    },
    request: {
        "a": "1",
        "b": "2"
    }
}
```

Options:

```sh
$ docker run -e PORT=8000 -e WORKERS=2 -e OUTDIR=/tmp -p 8000:8000 webhookbin
```

Docker image available at: https://hub.docker.com/r/grangerp/webhookbin

## Deployment with kustomize 

```sh
 k apply -k manifests/overlays/ENV_NAME
```
