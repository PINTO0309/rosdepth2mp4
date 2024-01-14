# rosimg2mp4
A simple tool to record ROS2 Image topics to mp4v, MP4V, MP4S, DIV3, DIVX, IYUV, MJPG, XVID.

```
pip install rosimg2mp4
```

```
usage: rosimg2mp4 [-h]
[-i DEPTH_TOPIC_NAME]
[-o OUTPUT_FILE_NAME]
[-cd {mp4v,MP4V,DIV3,DIVX,IYUV,MJPG,XVID}]
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
    Realsense D435i: /camera/aligned_depth_to_color/image_raw
    ZED2i: /zed2i/zed_node/depth/depth_registered
  -o OUTPUT_FILE_NAME, --output_file_name OUTPUT_FILE_NAME
    Output file name. e.g. output.mp4
  -cd {mp4v,MP4V,DIV3,DIVX,IYUV,MJPG,XVID}, \
      --output_codec_type {mp4v,MP4V,DIV3,DIVX,IYUV,MJPG,XVID}
    CODEC type. e.g. mp4v, MP4V, MP4S, DIV3, DIVX, IYUV, MJPG, XVID, H263
  -de {16UC1,32FC1}, --depth_encoding_type {16UC1,32FC1}
    Depth encoding type.
    e.g.
    Realsense D435i: 16UC1, ZED2i: 32FC1
  -ct {COLORMAP_JET,COLORMAP_HSV,COLORMAP_HOT,RAW}, \
      --colormap_type {COLORMAP_JET,COLORMAP_HSV,COLORMAP_HOT,RAW}
    COLORMAP type.
  -fs FRAME_SIZE FRAME_SIZE, --frame_size FRAME_SIZE FRAME_SIZE
    Frame size. e.g. --frame-size {Width} {Height}
  -vf VIDEO_WRITER_FPS, --video_writer_fps VIDEO_WRITER_FPS
    Video writer FPS.
```

https://github.com/PINTO0309/mp42ros
