# -*- coding: utf-8 -*-
from PIL import Image


def fill_image(image):
    width, height = image.size
    # 选取长和宽中较大值作为新图片的尺寸
    new_image_length = width if width > height else height
    # 生成新图片[白底]
    new_image = Image.new(image.mode, (new_image_length, new_image_length),
                          color='white')
    # 将之前的图粘贴在新图上，居中
    if width > height:
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))
    return new_image


def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j*item_width, i*item_width,
                   (j+1)*item_width, (i+1)*item_width)
            box_list.append(box)
    image_list = [image.crop(b) for b in box_list]
    return image_list


def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('./result/python'+str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "python.jpg"
    image = Image.open(file_path)
    # image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)
