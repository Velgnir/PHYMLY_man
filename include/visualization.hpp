//
// Created by paulo on 09.08.21.
//

#include <iostream>
#include <math.h>

struct rgb_t{
    uint8_t r;
    uint8_t g;
    uint8_t b;
};
rgb_t C_to_rgb(const double Temperature, rgb_t colour_threads, const double Temperature_limit);