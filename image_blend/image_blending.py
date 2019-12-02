class Operation:

    def blend(self, image, logo, x=None, y=None, alpha=None):
        '''
        Use logo and blend it on the image at location (x, y)
        image: the original image
        logo: the logo to blend on to the image
        x: topleft coordinate x
        y: topleft coordinate y
        alpha: blend ratio to the logo

        returns the image blended with logo at location (x, y)
        '''

        blended = image.copy()
        overlay = image.copy()

        num_of_rows, num_of_cols = image.shape

        # shape = overlay.shape
        logo_rows = y + logo.shape[0]
        logo_cols = x + logo.shape[1]
        logo_row = None
        hit = False

        for row in range(num_of_rows):
            if x < 0:
                logo_col = abs(x)
            else:
                logo_col = 0
            if y < 0 and logo_row is None:
                logo_row = abs(y)
            elif y < 0:
                logo_row += 1
            elif logo_row is None:
                logo_row = 0
            if hit is True:
                logo_row += 1
            for col in range(num_of_cols):
                if x < 0:
                    range_of_x = 0
                else:
                    range_of_x = x
                if y < 0:
                    range_of_y = 0
                else:
                    range_of_y = y
                if (row in range(range_of_y, logo_rows)) and (col in range(range_of_x, logo_cols)):
                    hit = True
                    overlay[row, col] = logo[logo_row, logo_col]
                    logo_col += 1
        blended = overlay * (1.0 - alpha) + blended * alpha
        return blended  # Currently the original image is returned, please replace this with the blended image

