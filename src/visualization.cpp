// This is a personal academic project. Dear PVS-Studio, please check it.
// // PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com
//

//
// Created by paulo on 09.08.21.
//

#include "visualization.hpp"

rgb_t C_to_rgb(const double Temperature, rgb_t colour_threads, const double Temperature_limit) {
    //-273(blue)  --  biggest/4(sky-blue)  --  biggest*2/4(green)  --  biggest*3/4(yellow) -- biggest(red)

    if(Temperature <= 0){
        colour_threads.r = 0;
        colour_threads.g = std::round((255.0/273.0) * (Temperature+273));
        colour_threads.b = 255;
    }else if(Temperature <= Temperature_limit/3){
        colour_threads.r = 0;
        colour_threads.g = 255;
        colour_threads.b = std::round((255.0 / (Temperature_limit / 3)) * ((Temperature_limit / 3.0) - Temperature));
    }else if(Temperature <= ((2*Temperature_limit)/3)){
        colour_threads.r = std::round((255.0/((Temperature_limit)/3.0)) * (Temperature - Temperature_limit/3.0));
        colour_threads.g = 255;
        colour_threads.b = 0;
    } else{
        colour_threads.r = 255;
        colour_threads.g = std::round((255.0 / (Temperature_limit / 3.0)) * (Temperature_limit - Temperature));
        colour_threads.b = 0;
    }
    /*if (Temperature+273 < (Temperature_limit+273)/4){
        colour_threads.r = 0;
        colour_threads.g = std::round((255/((Temperature_limit+273)/4)) * (Temperature+273));
        colour_threads.b = 255;
    } else if (Temperature+273<(Temperature_limit+273)/2){
        colour_threads.r = 0;
        colour_threads.g = 255;
        colour_threads.b = std::round((255/((Temperature_limit+273)/4)) * (((Temperature_limit+273)/2)-(Temperature+273)));
    } else if (Temperature+273 < 3*(Temperature_limit+273)/4){
        colour_threads.r = std::round((255/((Temperature_limit+273)/4)) * ((Temperature+273)-(Temperature_limit+273)/2));
        colour_threads.g = 255;
        colour_threads.b = 0;
    } else{
        colour_threads.r = 255;
        colour_threads.g = std::round((255/((Temperature_limit+273)/4)) * ((Temperature_limit+273) - (Temperature+273)));
        colour_threads.b = 0;
    }*/
    return colour_threads;
}