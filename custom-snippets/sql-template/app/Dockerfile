FROM python:latest
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Copy student submission to container
COPY ../submission.txt .
CMD ["pytest"]
