from enum import IntEnum
from collections import Counter


class Settings(IntEnum):
    # width and height given by Advent of Code
    width = 25
    height = 6
    max_int = 999999


class Frame:
    def __init__(self, total_pixels):
        self.data = total_pixels
        self.width = Settings.width
        self.length = Settings.height
        self.image_frame = []
        self.num_images = int(len(total_pixels) / (self.width * self.length))
        self.image_size = self.width * self.length
        self.create_frame()

    def create_frame(self):
        for i in range(0, self.num_images):
            image = Image(self.data[i * self.image_size:(i + 1) * self.image_size])
            self.image_frame.append(image.pixels_used)

    def generate_checksum(self):
        min_zero = Settings.max_int
        checksum = None
        for image in self.image_frame:
            if image[0] < min_zero:
                min_zero = image[0]
                checksum = image[1] * image[2]
        return checksum

    def decode_image(self):
        answer_layer = self.data[0:150] # set to first layer
        for i in range(0,len(self.data), 150):
            layer = self.data[i:i+150]
            for pixel_index in range(len(layer)):
                if answer_layer[pixel_index] == 2:
                    answer_layer[pixel_index] = layer[pixel_index]

        # make image easier to read
        for i in range(len(answer_layer)):
            if answer_layer[i] == 1:
                answer_layer[i] = '#'
            elif answer_layer[i] == 0:
                answer_layer[i] = ' '

        # print image
        for i in range(self.length):
            for j in range(self.width):
                print(answer_layer[i*self.width + j], end='')
            print()


class Image(Frame):
    # a frame consists of many images
    def __init__(self, pixels):
        self.pixels = pixels
        self.pixels_used = Counter(self.pixels)


def main():
    pass
    file = open("day_8_input", "r")
    data = list(map(int, file.readline().strip()))

    bios = Frame(data)
    print(bios.generate_checksum())
    bios.decode_image()


if __name__ == '__main__':
    main()
