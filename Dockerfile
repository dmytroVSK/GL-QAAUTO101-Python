FROM python:3.13.1-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "tests/database"]

# docker build . -t pytest_db_img
# docker run -it --rm -v $(pwd)/:/app pytest_db_img



