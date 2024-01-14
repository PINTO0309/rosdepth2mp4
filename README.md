# rosimg2mp4
A simple tool to record ROS2 Image topics to mp4v, MP4V, MP4S, DIV3, DIVX, IYUV, MJPG, XVID. https://github.com/PINTO0309/simple-ros2-processing-tools

[![Downloads](https://static.pepy.tech/personalized-badge/rosdepth2mp4?period=total&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/rosdepth2mp4)

## 1. Install ROS2
```bash
DISTRO=humble

sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt install software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install -y \
ros-${DISTRO}-rosbag2 \
ros-${DISTRO}-vision-opencv \
ros-${DISTRO}-vision-msgs \
ros-${DISTRO}-image-pipeline
```
## 2. Install rosdepth2mp4
```
pip install rosdepth2mp4
```
## 3. Usage
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

https://github.com/PINTO0309/rosimg2mp4
