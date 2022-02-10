FROM python:3.9-slim

WORKDIR app

RUN pip install flask numpy

COPY predict.py averages.csv coefficients.csv ./

CMD python ./predict.py