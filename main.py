'''
Removes barrel distortions from images (.bmp) in the /data.
Uses tqdm progress bar.
usage:
    main.py
'''
from tqdm import tqdm

# local modules
from remove_distortion import DistortionRemover
from utils import read_image, write_image, create_output_folder
from utils import load_config


def main():
    config = load_config()
    working_dir, output_path = create_output_folder()
    img_file_list = list(working_dir.glob('**/*.bmp'))

    for img_file in tqdm(img_file_list):
        src = read_image(img_file, config)
        dst = DistortionRemover(src, config).barrel_undist()
        out_file = str(output_path / (img_file.stem + "_undist.bmp"))
        write_image(dst, out_file)

    return True


if __name__ == "__main__":
    main()
