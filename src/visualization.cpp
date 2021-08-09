//
// Created by paulo on 09.08.21.
//

#include "visualization.hpp"

void C_to_rgb(const double temp_here, int &r, int &g, int &b) {
    //-170(blue)  --  -70(sky-blue)  --  30(green)  --  130(yellow) -- 230(red)
    if (temp_here < -70) {
        r = 0;
        g = (size_t) (2.55 * (temp_here + 170));
        b = 255;
    } else if (temp_here < 30) {
        r = 0;
        g = 255;
        b = (size_t) (2.55 * abs(temp_here - 30));
    } else if (temp_here < 130) {
        r = (size_t) (2.55 * (temp_here - 30));
        g = 255;
        b = 0;
    } else {
        r = 255;
        g = (size_t) (2.55 * (230 - temp_here));
        b = 0;
    }
}
