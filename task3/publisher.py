import os
import time
import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.queue_declare(queue='data_files')

while True:
    data_files = os.listdir('data')
    message = json.dumps(data_files)
    channel.basic_publish(exchange='', routing_key='data_files', body=message)
    time.sleep(1)

connection.close()
