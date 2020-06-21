'''
Removes distortions from images (.bmp) using config.json
Uses a simpler progress bar (without tqdm).
usage:
    main_simple.py
'''

# local modules
from remove_distortion import DistortionRemover
from utils import read_image, write_image, create_output_folder
from utils import load_config


def main():
    config = load_config()
    working_dir, output_path = create_output_folder()
    img_file_list = list(working_dir.glob('**/*.bmp'))

    img_num = len(img_file_list)    # For progress bar

    for i, img_file in enumerate(img_file_list):
        src = read_image(img_file, config)
        dst = DistortionRemover(src, config).image_undist()
        out_file = str(output_path / (img_file.stem + "_undist.bmp"))
        write_image(dst, out_file)
        print("Processed:" + str(i+1) + "/" + str(img_num))

    return True


if __name__ == "__main__":
    main()
