from demo import load_checkpoints, make_animation
from skimage import img_as_ubyte
import imageio

def animate_face(source_image_path, driving_video_path, output_path="generated_video.mp4"):
    generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', checkpoint_path='models/first_order_motion_model.pth.tar')
    source_image = imageio.imread(source_image_path)
    driving_video = imageio.mimread(driving_video_path, memtest=False)

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True, adapt_movement_scale=True)

    imageio.mimsave(output_path, [img_as_ubyte(frame) for frame in predictions])
    return output_path
