# rosdepth2mp4
A simple tool to record ROS2 Depth topics to MP4.

```
pip install rosdepth2mp4
```

```
usage: rosdepth2mp4 [-h]
[-i DEPTH_TOPIC_NAME]
[-o OUTPUT_MP4_FILE_NAME]
[-de {16UC1,32FC1}]
[-ct {COLORMAP_JET,COLORMAP_HSV,COLORMAP_HOT,RAW}]
[-fs FRAME_SIZE FRAME_SIZE]
[-vf VIDEO_WRITER_FPS]

options:
  -h, --help
    show this help message and exit
  -i DEPTH_TOPIC_NAME, --depth_topic_name DEPTH_TOPIC_NAME
    Depth topic name.
    e.g.
    Realsense D435: /camera/aligned_depth_to_color/image_raw
    ZED2i: /zed2i/zed_node/depth/depth_registered
  -o OUTPUT_MP4_FILE_NAME, --output_mp4_file_name OUTPUT_MP4_FILE_NAME
    Output MP4 file name.
    e.g. output.mp4
  -de {16UC1,32FC1}, --depth_encoding_type {16UC1,32FC1}
    Depth encoding type.
    e.g. Realsense D435i: 16UC1, ZED2i: 32FC1
  -ct {COLORMAP_JET,COLORMAP_HSV,COLORMAP_HOT,RAW}, \
      --mp4_colormap_type {COLORMAP_JET,COLORMAP_HSV,COLORMAP_HOT,RAW}
    COLORMAP type.
  -fs FRAME_SIZE FRAME_SIZE, --frame_size FRAME_SIZE FRAME_SIZE
    Frame size.
    e.g.
    --frame-size {Width} {Height}
  -vf VIDEO_WRITER_FPS, --video_writer_fps VIDEO_WRITER_FPS
    Video writer FPS.
```

- ZED2i - RAW mode

  https://github.com/PINTO0309/rosdepth2mp4/assets/33194443/223291e2-2899-47fe-bd71-800cda8dd073

- ZED2i - JET mode

  https://github.com/PINTO0309/rosdepth2mp4/assets/33194443/82b235d3-b298-48d5-b30a-f2536fd2fcff

- Realsense D435 - RAW mode

  https://github.com/PINTO0309/rosdepth2mp4/assets/33194443/861576fd-aa63-4a16-afff-7a0473eff50d

- Realsense D435 - JET mode

  https://github.com/PINTO0309/rosdepth2mp4/assets/33194443/7bedd611-822c-4971-85c3-84fb9cdf33b5

https://github.com/PINTO0309/rosdepth2mp4
