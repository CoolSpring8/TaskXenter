FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --upgrade pip && \
    pip install --no-cache-dir tortoise-orm asyncpg pyjwt passlib[bcrypt] loguru databases python-multipart celery sentry-sdk httpx

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

CMD [ "sh", "-c", "sleep 5 && python /app/app/setup_db.py && /start.sh" ]