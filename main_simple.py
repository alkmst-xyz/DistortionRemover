# Simple progress bar - Does not use tqdm

# local modules
from remove_distortion import DistortionRemover
from utils import read_image_file, write_image_file, create_output_folder


def main():
    working_dir, output_path = create_output_folder()
    img_file_list = list(working_dir.glob('**/*.bmp'))

    img_num = len(img_file_list)

    for i, img_file in enumerate(img_file_list):
        src = read_image_file(img_file)
        dst = DistortionRemover(src).barrel_undist()
        out_file = str(output_path / (img_file.stem + "_undist.bmp"))
        write_image_file(dst, out_file)
        print("Processed:" + str(i+1) + "/" + str(img_num))

    return True


if __name__ == "__main__":
    main()
