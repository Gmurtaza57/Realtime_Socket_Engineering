import json
import socket
import time
import pandas as pd

def handle_date(obj):
    if isinstance(obj, pd.Timestamp):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

def send_data_over_socket(file_path, host='spark-master', port=9999, chunk_size=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Listening for connections on {host}:{port}")

    last_sent_index = 0
    while True:
        conn, addr = s.accept()
        print(f"Connection established from {addr}")

        try:
            with open(file_path, 'r') as file:
                # skip lines that were already sent
                for _ in range(last_sent_index):
                    next(file)

                records = []
                for line in file:
                    records.append(json.loads(line))

                    if len(records) == chunk_size:
                        chunk = pd.DataFrame(records)
                        print(f"Sending data chunk: \n{chunk}")
                        for record in chunk.to_dict(orient='records'):
                            serialized_data = json.dumps(record, default=handle_date).encode('utf-8')
                            conn.send(serialized_data + b'\n')
                            time.sleep(87)  # Throttle sending rate
                            last_sent_index += 1

                        records = []

        except (BrokenPipeError, ConnectionResetError) as e:
            print(f"Client disconnected unexpectedly: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
            print("Connection closed")

if __name__ == "__main__":
    send_data_over_socket("datasets/yelp_academic_dataset_review.json")
