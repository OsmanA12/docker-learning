FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install flask redis 
EXPOSE 7777
CMD ["python", "count.py"] 