import cv2
import sys
from datetime import datetime
from image_blend import image_blending


def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the appropriate
     method and writes the images image"""

    #   PARSE INPUT ARGUMENTS
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-l", "--logo", dest="logo",
                        help="use the name of the logo/blending image", metavar="LOGO_IMAGE")

    parser.add_argument("-x", "--topleft_x", dest="topleft_x",
                        help="specify location of x", metavar="X")
    parser.add_argument("-y", "--topleft_y", dest="topleft_y",
                        help="specify location of y", metavar="Y")

    parser.add_argument("-a", "--alpha", dest="alpha",
                        help="specify blend ratio to LOGO image", metavar="ALPHA")
    
    args = parser.parse_args()

    #   LOAD IMAGE
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    if args.logo is None:
        print('Please use a blending image')
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        logo = cv2.imread(args.logo, 0)

    # CHECK IF BLENDING IMAGE IS SMALLER THAN BACKGROUND IMAGE
    
    r1, c1 = input_image.shape
    r2, c2 = logo.shape
    
    if r1 < r2 or c1 < c2:
        print('The image should be larger than the blending image')
        sys.exit(2)

    # Check the location to blend
    if args.topleft_x is None:
        print("Location X not specified using default (0)")
        print("use the -h option to see usage information")
        x = 0
    else:
        x = int(args.topleft_x)

    if args.topleft_y is None:
        print("Location Y not specified using default (0)")
        print("use the -h option to see usage information")
        y = 0
    else:
        y = int(args.topleft_y)

    # IS ALPHA BETWEEN 0 to 1
    if args.alpha is None:
        print('ALPHA not specified using default (0)')
        alpha = 0
    else:
        if 0 <= float(args.alpha) <= 1:
            alpha = float(args.alpha)
        else:
            print('The weight should be within 0 to 1')
            sys.exit(2)

    operation_obj = image_blending.Operation()
    operation_image = operation_obj.blend(input_image, logo, x=x, y=y, alpha=alpha)

    #   OUTPUT DIRECTORY
    outputDir = 'images/'

    output_image_name = outputDir+image_name+datetime.now().strftime("%m%d-%H%M%S%f")+".jpg"
    cv2.imwrite(output_image_name, operation_image)



if __name__ == "__main__":
    main()







