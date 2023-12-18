FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install  --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org cache -r requirements.txt


EXPOSE 8000
#copy all the files from current directory to app folder
COPY . /app