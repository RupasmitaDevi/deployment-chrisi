FROM python:3.6-alpine
ADD src /usr/app/src/
COPY requirements.txt /usr/app/src/

RUN pip install --no-cache-dir -r /usr/app/src/requirements.txt

EXPOSE 5000

CMD ["python", "/usr/app/src/app.py"]