# TaskXenter

## About

This is a *semi-finished* project, and *probably abandoned*. 

**For its originally designed purpose:** 

Built upon **FastAPI, Tortoise-ORM, Celery, HTTPX, PostgreSQL, RabbitMQ, Docker, Sentry, Vue and Nginx**, this project was meant for **"a platform that allows users to send periodic HTTP(s) requests, cron-like-ly"**. 

**For the name:** 

X is pronounced the same as "ks". (So at first it was called "TasXenter", but later got its name changed to "TaskXenter" for legibility.)

**For why I've pushed the semi-finished one into this repo:** 

I left it here as an example of integrating these technologies, as when I searched for information I realized that some of them get little usages to refer to currently, thus making it potentially more difficult to develop applications with them. 

**Hope this will help anyone who comes here accidentally!** 

## To Run

```
docker-compose up -d
cd frontend
npm run dev
```

## Known Issues

There are simply too many to be documented, including but not limited to the following ones: 

- Core features not functional actually, especially celery-related functions. 
- Frontend user verification not handled correctly. 
- Not optimized for production, but for local development only. 
- ...

## Credit

For project structure and more: 

- https://github.com/watsy0007/fastapi_demo
- https://github.com/tiangolo/full-stack-fastapi-postgresql
- https://github.com/nsidnev/fastapi-realworld-example-app
- https://github.com/PanJiaChen/vue-element-admin

