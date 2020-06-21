from pathlib import Path


from remove_distortion import DistortionRemover
from utils import read_image_file, write_image_file


def main():
    working_dir = Path.cwd() / 'data'
    img_file_list = list(working_dir.glob('**/*.bmp'))
    img_num = len(img_file_list)

    output_path = Path.cwd() / 'output'
    if output_path.is_dir():
        print("Output folder exists")
        try:
            output_path.rmdir()
        except OSError as err:
            print("Error: %s : %s" % (output_path, err.strerror))
            print("Overwriting...")
    else:
        print("Output folder created")
        output_path.mkdir()

    for i, img_file in enumerate(img_file_list):
        src = read_image_file(img_file)
        dst = DistortionRemover(src).barrel_undist()
        out_file = str(output_path / (img_file.stem + "_undist.bmp"))
        write_image_file(dst, out_file)
        print("Processed:" + str(i+1) + "/" + str(img_num))
    return True


if __name__ == "__main__":
    main()
