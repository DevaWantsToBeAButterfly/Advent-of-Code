with open('data_files\day_8_input.txt') as input_file:
    data_dump = input_file.read().replace('\n','')


def build_layers(pixel_data):
    layers_list = []
    layer_width = 25
    layer_height = 6
    current_pixel_index = 0

    while current_pixel_index < len(pixel_data):

        new_layer = []
        for row in range(0, layer_height):
            new_layer.append(pixel_data[current_pixel_index:current_pixel_index + layer_width])
            current_pixel_index += layer_width

        layers_list.append(new_layer)

    return layers_list


def count_digit_occurrences(layers_list):

    for n in range(len(layers_list)):

        current_layer = layers_list[n]
        zero_count, one_count, two_count = 0, 0, 0

        for row in current_layer:
            zero_count += row.count('0')
            one_count += row.count('1')
            two_count += row.count('2')

        layers_list[n] = {'Layer map': current_layer, 'Pixel counts': {'Zeroes': zero_count, 'Ones': one_count,
                                                                       'Twos': two_count}}


def get_layer_zeroes_count(layer):

    return layer['Pixel counts']['Zeroes']


def get_layer_product(layers_list):

    least_zeroes_layer = sorted(layers_list, key=get_layer_zeroes_count)[0]
    print(least_zeroes_layer['Pixel counts']['Ones'] * least_zeroes_layer['Pixel counts']['Twos'])


def draw_image(layers_list):

    for row_i in range(0, 6):
        image_row = ''

        for pixel_i in range(0, 25):
            for layer in layers_list:
                if layer['Layer map'][row_i][pixel_i] == '0':
                    image_row += ' '
                    break

                elif layer['Layer map'][row_i][pixel_i] == '1':
                    image_row += '*'
                    break

        print(image_row)


layers = build_layers(data_dump)
count_digit_occurrences(layers)
get_layer_product(layers)
draw_image(layers)
