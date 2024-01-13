# rosdepth2mp4
A simple tool to record ROS2 Depth topics to MP4.

```
pip install rosdepth2mp4
```

```
usage: rosdepth2mp4 [-h]
[-i RGB_IMAGE_TOPIC_NAME]
[-o OUTPUT_MP4_FILE_NAME]
[-fs FRAME_SIZE FRAME_SIZE]
[-vf VIDEO_WRITER_FPS]

options:
  -h, --help
    show this help message and exit
  -i RGB_IMAGE_TOPIC_NAME, --rgb_image_topic_name RGB_IMAGE_TOPIC_NAME
    RGB image topic name.
  -o OUTPUT_MP4_FILE_NAME, --output_mp4_file_name OUTPUT_MP4_FILE_NAME
    Output MP4 file name. e.g. output.mp4
  -fs FRAME_SIZE FRAME_SIZE, --frame_size FRAME_SIZE FRAME_SIZE
    Frame size. e.g. --frame-size {Width} {Height}
  -vf VIDEO_WRITER_FPS, --video_writer_fps VIDEO_WRITER_FPS
    Video writer FPS.
```

https://github.com/PINTO0309/rosdepth2mp4
