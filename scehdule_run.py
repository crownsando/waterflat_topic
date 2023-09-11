import schedule
import time
import os

def job():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print("Executing 'topic_final.py'")
    os.system(f"python {os.path.join(current_directory, 'topic_final.py')}")

schedule.every().day.at("00:01").do(job)

while True:
    schedule.run_pending()
    time.sleep(86400)  # 1분마다 스케줄 확인
