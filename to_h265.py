import ffmpeg
import os

def convert_to_h265(input_file, output_file, crf_value=23):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, vcodec='libx265', acodec='copy')
        .run()
    )

path = r'/Users/ggvis/Desktop/VSCode/Python/video/h264'
os.chdir(path)

if not os.path.exists("h265"):
    os.makedirs("h265")
    
for file_name in os.listdir(path):
    if file_name.endswith('.mp4'):
        input_file = file_name
        output_file = os.path.join("h265", file_name)
        convert_to_h265(input_file, output_file)
        print(f"Conversion completed for {input_file}")
