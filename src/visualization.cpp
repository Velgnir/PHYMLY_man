//
// Created by paulo on 09.08.21.
//

#include "visualization.hpp"

void C_to_rgb(const double Temperature, uint8_t &r, uint8_t &g, uint8_t &b, const double Temperature_limit) {
    //0(blue)  --  biggest/4(sky-blue)  --  biggest*2/4(green)  --  biggest*3/4(yellow) -- biggest(red)
    if (Temperature+273 < (Temperature_limit+273)/4){
        r = 0;
        g = std::round((255/((Temperature_limit+273)/4)) * (Temperature+273));
        b = 255;
    } else if (Temperature+273<(Temperature_limit+273)/2){
        r = 0;
        g = 255;
        b = std::round((255/((Temperature_limit+273)/4)) * (((Temperature_limit+273)/2)-(Temperature+273)));
    } else if (Temperature+273 < 3*(Temperature_limit+273)/4){
        r = std::round((255/((Temperature_limit+273)/4)) * ((Temperature+273)-(Temperature_limit+273)/2));
        g = 255;
        b = 0;
    } else{
        r = 255;
        g = std::round((255/((Temperature_limit+273)/4)) * ((Temperature_limit+273) - (Temperature+273)));
        b = 0;
    }
}
