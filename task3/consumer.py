import pika
import os
import json
import time


def callback(ch, method, properties, body):
    files = json.loads(body)
    result = ''
    for file in files:
        with open(os.path.join('data', file), 'r') as f:
            result += f.read() + '\n'
        os.remove(os.path.join('data', file))
    print(result)
    with open(os.path.join('result', str(method.delivery_tag) + '.txt'), 'w') as f:
        f.write(result)
    time.sleep(35)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.basic_consume(queue='data_files', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
