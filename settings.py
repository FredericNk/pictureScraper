class Settings:
    def __init__(self):
        self.num_files = 0
        self.starting_row = 0
        self.limit_x = 350  # Limits how many pictures in the x direction are to be downloaded
        self.limit_y = 350  # Limits how many pictures in the y direction are to be downloaded
        self.save_path = "image/"  # Path to the directory to save the downlaoded pictures

        # For Example if your url to the first File is: https://this.com/should/be/the/url/trunc/0_0.jpg
        # The following will be your config
        self.separator = "_"
        self.file_type = ".jpg"
        self.url_trunc = 'https://this.com/should/be/the/url/trunc/'
