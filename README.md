# ce-demo

- docker run -d --name=webrouter -v /data/webrouter/nginx/nginx.conf:/etc/nginx/nginx.conf -v /data/webrouter/nginx/proxy.conf:/etc/nginx/proxy.conf -v /data/webrouter/nginx/conf.d:/etc/nginx/conf.d -v /data/webrouter/log:/var/log/nginx -p 80:80 nginx:1
- docker run -d --name=jenkins -p 8200:8080 jenkins:1.596.2
