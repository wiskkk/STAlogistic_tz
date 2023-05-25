import os
import time
import uuid

start_time = time.time()
while time.time() - start_time < 120:
    filename = str(uuid.uuid4()) + '.txt'
    with open(os.path.join('data', filename), 'w') as f:
        f.write(filename)
    time.sleep(5)
