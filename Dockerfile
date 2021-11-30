FROM python:3.7.12-buster
COPY . /.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD streamlit run app.py --server.port $PORT%
