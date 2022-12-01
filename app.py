from flask import Flask, render_template
import os
from io import BytesIO
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/task')
def task():
    connection_string = 'DefaultEndpointsProtocol=https;AccountName=mystorageaccount11917;AccountKey=b3QGLoNtwtkKKXzkwzXjTfj+7k4N7nk8IL8RVvdLMfK+AYOEnur/3QGFgIl50JyH35GqoXQmW0Tp+AStl21efg==;EndpointSuffix=core.windows.net'
    container_name = 'inovices'
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    file_name = 'e0bb9606f50adcc4b5ca3071f310aa9e.pdf'
    blob_client = container_client.get_blob_client(file_name)
    stream_downloader = blob_client.download_blob()
    file = BytesIO()
    stream_downloader.download_to_stream(file)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    return ROOT_DIR + ' 1 ' + str(file)