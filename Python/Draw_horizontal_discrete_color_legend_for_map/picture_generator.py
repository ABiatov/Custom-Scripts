import pathlib
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = pathlib.Path("/Users/Alevtina/Documents/GitHub/Custom-Scripts/Python/Draw_horizontal_discrete_color_legend_for_map").resolve()
print("BASE_DIR: ", BASE_DIR)

font_path = BASE_DIR.joinpath("Roboto-Medium.ttf")
print("font_path: ", font_path)

legend_fnt = ImageFont.truetype(f"{font_path}", 25)


LEGEND_PATH = BASE_DIR.joinpath('result_image.png')
print('LEGEND_PATH: ', LEGEND_PATH)


def str_rgba_to_tuple_rgb(color_str):
    color_rgba_list = color_str.split()
    tuple_generator = (int(i) for i in color_rgba_list)
    color_rgb_tuple = tuple(tuple_generator)[0:3]
    return color_rgb_tuple


legend_width = 1502
legend_height = 45

range_list = ['0',  '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']


border_pixel = [
    0,
    150,
    300,
    450,
    600,
    750,
    900,
    1050,
    1200,
    1350,
    1500,
    1502
    ]

list_colors = [
    '48 18 59 255',
    '69 91 205 255',
    '62 156 254 255',
    '24 215 203 255',
    '72 248 130 255',
    '164 252 60 255',
    '226 220 56 255',
    '254 163 49 255',
    '239 89 17 255',
    '194 36 3 255',
    '122 4 3 255'
               ]

list_tuples_colors = [str_rgba_to_tuple_rgb(item) for item in list_colors]

# added generation picture legend

legend_img = Image.new(mode="RGBA", size=(legend_width, legend_height), color=(255, 255, 255, 255))
legend_img_draw = ImageDraw.Draw(legend_img)
legend_img_draw.rectangle([(border_pixel[0], 0), (border_pixel[1], 10)], fill=list_tuples_colors[0], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[1], 0), (border_pixel[2], 10)], fill=list_tuples_colors[1], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[2], 0), (border_pixel[3], 10)], fill=list_tuples_colors[2], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[3], 0), (border_pixel[4], 10)], fill=list_tuples_colors[3], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[4], 0), (border_pixel[5], 10)], fill=list_tuples_colors[4], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[5], 0), (border_pixel[6], 10)], fill=list_tuples_colors[5], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[6], 0), (border_pixel[7], 10)], fill=list_tuples_colors[6], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[7], 0), (border_pixel[8], 10)], fill=list_tuples_colors[7], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[8], 0), (border_pixel[9], 10)], fill=list_tuples_colors[8], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[9], 0), (border_pixel[10], 10)], fill=list_tuples_colors[9], outline=None, width=1)
legend_img_draw.rectangle([(border_pixel[10], 0), (border_pixel[11], 10)], fill=list_tuples_colors[10], outline=None, width=1)


legend_img_draw.text((border_pixel[0], 20), str(range_list[0]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[1]-12, 20), str(range_list[1]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[2]-12, 20), str(range_list[2]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[3]-12, 20), str(range_list[3]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[4]-12, 20), str(range_list[4]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[5]-12, 20), str(range_list[5]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[6]-12, 20), str(range_list[6]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[7]-12, 20), str(range_list[7]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[8]-12, 20), str(range_list[8]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[9]-12, 20), str(range_list[9]), font=legend_fnt, fill=(0, 0, 0))
legend_img_draw.text((border_pixel[10]-40, 20), str(range_list[10]), font=legend_fnt, fill=(0, 0, 0))

legend_img.save(f"{LEGEND_PATH}")
