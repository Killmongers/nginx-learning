FROM python:3.11

WORKDIR /app

copy app.py .
copy requirements.txt .

Run apt-get update && apt-get install 

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
