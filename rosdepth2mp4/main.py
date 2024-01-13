#!/usr/bin/python

from argparse import ArgumentParser
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from datetime import datetime
from typing import Tuple

RED="\033[31m"
YELLOW="\033[33m"
GREEN="\033[32m"
BLUE="\033[34m"
RESET="\033[0m"

COLORMAP_TYPES = {
    'COLORMAP_JET': cv2.COLORMAP_JET,
    'COLORMAP_HSV': cv2.COLORMAP_HSV,
    'COLORMAP_HOT': cv2.COLORMAP_HOT,
    'RAW': None,
}

class ImageSaverNode(Node):
    def __init__(
        self,
        depth_topic_name: str,
        depth_encoding_type: str,
        mp4_colormap_type: str,
        frame_size: Tuple[int, int],
        video_writer_fps: float,
        output_mp4_file_name: str,
    ):
        super().__init__('image_saver')
        self.subscription = \
            self.create_subscription(
                msg_type=Image,
                topic=depth_topic_name,
                callback=self.depth_callback,
                qos_profile=10,
            )
        self.bridge = CvBridge()
        self.video_writer = \
            cv2.VideoWriter(
                filename=output_mp4_file_name \
                    if output_mp4_file_name else f'output_{datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")}.mp4',
                fourcc=cv2.VideoWriter_fourcc(*'mp4v'),
                fps=video_writer_fps,
                frameSize=frame_size,
            )
        self.depth_encoding_type = depth_encoding_type
        self.mp4_colormap_type = COLORMAP_TYPES[mp4_colormap_type]
        self.frame_size = frame_size

    def depth_callback(self, depth_data: Image):
        # RAW
        self.depth_image_raw: np.ndarray = \
            self.bridge.imgmsg_to_cv2(depth_data, self.depth_encoding_type) \
                if depth_data is not None and self.depth_encoding_type is not None else None
        if self.depth_encoding_type == '32FC1':
            self.depth_image_raw: np.ndarray = np.nan_to_num(self.depth_image_raw)
            self.depth_image_raw: np.ndarray = self.depth_image_raw * 1000.0 # mm

        # COLORMAP
        if self.mp4_colormap_type is None:
            if self.depth_image_raw is not None:
                if self.depth_encoding_type == '16UC1':
                    self.depth_image_raw = \
                        np.concatenate(
                            [
                                self.depth_image_raw[..., np.newaxis] / 65535 * 6.0 * 255,
                                self.depth_image_raw[..., np.newaxis] / 65535 * 6.0 * 255,
                                self.depth_image_raw[..., np.newaxis] / 65535 * 6.0 * 255,
                            ],
                            axis=-1,
                        ).astype(np.uint8)
                elif self.depth_encoding_type == '32FC1':
                    self.depth_image_raw = \
                        np.concatenate(
                            [
                                self.depth_image_raw[..., np.newaxis] / 10000 * 1.5 * 255,
                                self.depth_image_raw[..., np.newaxis] / 10000 * 1.5 * 255,
                                self.depth_image_raw[..., np.newaxis] / 10000 * 1.5 * 255,
                            ],
                            axis=-1,
                        ).astype(np.uint8)

            self.depth_image_raw_color_map: np.ndarray = self.depth_image_raw \
                    if self.depth_image_raw is not None else None
        else:
            self.depth_image_raw_color_map: np.ndarray = \
                cv2.applyColorMap(cv2.convertScaleAbs(self.depth_image_raw, alpha=0.03), self.mp4_colormap_type) \
                    if self.depth_image_raw is not None else None
        # Resize
        if self.depth_image_raw_color_map is not None:
            resized_cv_image = cv2.resize(self.depth_image_raw_color_map, self.frame_size)
            self.video_writer.write(resized_cv_image)
        else:
            self.video_writer.write(np.zeros((self.frame_size[1], self.frame_size[0], 3), dtype=np.uint8))

    def destroy_node(self):
        self.video_writer.release()
        super().destroy_node()

def main():
    parser = ArgumentParser()
    parser.add_argument(
        '-i',
        '--depth_topic_name',
        type=str,
        default='/camera/aligned_depth_to_color/image_raw',
        help=\
            'Depth topic name. ' +
            'e.g. Realsense D435: /camera/aligned_depth_to_color/image_raw, ZED2i: /zed2i/zed_node/depth/depth_registered',
    )
    parser.add_argument(
        '-o',
        '--output_mp4_file_name',
        type=str,
        default='',
        help='Output MP4 file name. e.g. output.mp4',
    )
    parser.add_argument(
        '-de',
        '--depth_encoding_type',
        type=str,
        default='16UC1',
        choices=['16UC1', '32FC1'],
        help='Depth encoding type. e.g. Realsense D435: 16UC1, ZED2i: 32FC1',
    )
    parser.add_argument(
        '-ct',
        '--mp4_colormap_type',
        type=str,
        default='COLORMAP_JET',
        choices=['COLORMAP_JET', 'COLORMAP_HSV', 'COLORMAP_HOT', 'RAW'],
        help='COLORMAP type.',
    )
    parser.add_argument(
        '-fs',
        '--frame_size',
        type=int,
        nargs=2,
        default=(896, 512),
        help='Frame size. e.g. --frame-size {Width} {Height}',
    )
    parser.add_argument(
        '-vf',
        '--video_writer_fps',
        type=float,
        default=15.0,
        help='Video writer FPS.',
    )
    args = parser.parse_args()

    rclpy.init()
    image_saver = \
        ImageSaverNode(
            depth_topic_name=args.depth_topic_name,
            depth_encoding_type=args.depth_encoding_type,
            mp4_colormap_type=args.mp4_colormap_type,
            frame_size=args.frame_size,
            video_writer_fps=args.video_writer_fps,
            output_mp4_file_name=args.output_mp4_file_name,
        )
    try:
        print(f'{GREEN}Start recording... Ctrl+C to end recording.{RESET}')
        while rclpy.ok():
            rclpy.spin_once(image_saver)
    except KeyboardInterrupt:
        pass
    finally:
        image_saver.destroy_node()
        print('')
        print(f'{GREEN}Stop recording.{RESET}')
    try:
        rclpy.shutdown()
    except:
        pass

if __name__ == '__main__':
    main()
