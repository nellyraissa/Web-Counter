FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=capp.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY softrequirements.txt softrequirements.txt
RUN pip install -r softrequirements.txt 
EXPOSE 3030
COPY . .
CMD ["flask", "run"]
