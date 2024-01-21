import serial
import time
BAUDRATE = 2400
NUM_BYTES_TO_RECEIVE = 1000  # Adjust as needed
ser = serial.Serial('COM2', BAUDRATE, timeout=1)
text_to_send = """Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one. In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently."""
ser.write(text_to_send.encode('utf-8'))
ser.write('\0'.encode('utf-8'))
start_time_receive = time.time()
received_data = ser.read(NUM_BYTES_TO_RECEIVE)
end_time_receive = time.time()
transmission_time_receive = end_time_receive - start_time_receive
transmission_speed_receive = (NUM_BYTES_TO_RECEIVE * 8) / transmission_time_receive
print("Data received:", received_data.decode('utf-8'))
print("Transmission speed: {:.2f} bits/second".format(transmission_speed_receive))
ser.close()
