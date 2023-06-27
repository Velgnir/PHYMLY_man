
#include <iostream>
#include <string>
#include <vector>
#include <filesystem>
#include "formula.hpp"
#include "files/config_file.h"
#include "CImg.h"
#include "visualization.hpp"

namespace cimg = cimg_library;

ConfigFileOpt parse_args(int argc, char **argv);
//void assert_valid_config(const ConfigFileOpt &conf);

int main(int argc, char *argv[]) {
    std::string input_file_name;
    std::string config_file_name;
    if (argc > 2) {
        input_file_name = argv[2];
        config_file_name = argv[3];
    } else {
        input_file_name = "input.txt";
        config_file_name = "config.conf";
    }
//    assert_valid_config(config);

    if ((!std::filesystem::exists(input_file_name))) {
        std::cerr << "File " << input_file_name << " wasn't found" << std::endl;
        return -1;
    }
    ConfigFileOpt config = parse_args(argc, argv);

    if ((!std::filesystem::exists(config_file_name))) {
        std::cerr << "File " << config_file_name << " wasn't found" << std::endl;
        return -1;
    }
    std::ifstream input_file(input_file_name);
    auto dT = config.get_delta_t()/2.0;
    auto dx = config.get_delta_x();
    auto dy = config.get_delta_y();
    auto alpha = config.get_alpha();
    auto size_x = config.get_width();
    auto size_y = config.get_height();
    auto leftBorder = config.get_left_func_arg();
    auto rightBorder = config.get_right_func_arg();
    auto upBorder = config.get_up_func_arg();
    auto bottomBorder = config.get_bottom_func_arg();
    auto program_end_temp_limit = config.get_temperature_limit();
    auto cycle_limit = config.get_max_number_of_cycles();
    int size_z=1;
    int number_of_colour_threads = 3;
    double k1 = (alpha * dT) / (dx * dx);
    double k2 = (alpha * dT) / (dy * dy);
    double possible_dT;
    if (k1+k2>0.5){
        possible_dT = (dx*dx*dy*dy)/(2*alpha*(dx*dx+dy*dy));
        k1 = (alpha * possible_dT) / (dx * dx);
        k2 = (alpha * possible_dT) / (dy * dy);
    } else{
        possible_dT = dT;
    }
    double temperature_limit=-274;
    std::vector<std::vector<double>> matrix;
    std::vector<std::vector<double>> First_matrix;
    cimg::CImg<unsigned char> img(size_x,size_y,size_z,number_of_colour_threads);
    std::string filename;
    rgb_t colour_threads;

    First_matrix.resize(size_y);
    matrix.resize(size_y);
    for (size_t i = 0; i < size_y; ++i) {
        First_matrix[i].resize(size_x);
        matrix[i].resize(size_x);
    }

    for (auto &line: First_matrix)
        for (auto &number: line)
            input_file >> number;


    matrix = First_matrix;

    for (auto &line:matrix)
        for (auto number:line)
            if (number>temperature_limit)
                temperature_limit = number;
    size_t h=0;
    while(true){
        for (size_t i = static_cast<size_t>(upBorder); i < static_cast<size_t>(bottomBorder); ++i) {
            for (size_t j = static_cast<size_t>(leftBorder); j < static_cast<size_t>(rightBorder); ++j) {
                matrix[i][j] = get_formula_result(i,j,First_matrix,k1,k2,size_x,size_y);
            }
        }
        if (h % (100*static_cast<int>(dT/possible_dT)) == 0) {
            for (size_t i = 0; i < size_y; ++i) {
                for (size_t j = 0; j < size_x; ++j) {
                       colour_threads =  C_to_rgb(matrix[i][j], colour_threads, temperature_limit);
                        img(j, i, 0, 0) = colour_threads.r;
                        img(j, i, 0, 1) = colour_threads.g;
                        img(j, i, 0, 2) = colour_threads.b;
                    }
                }
        }
        First_matrix = matrix;
        size_t SavedJ;
        if (h % (100*static_cast<int>(dT/possible_dT)) == 0) {
            if(program_end_temp_limit > -274)
                for (size_t i = static_cast<size_t>(upBorder); i < static_cast<size_t>(bottomBorder); ++i) {
                    for (size_t j = static_cast<size_t>(leftBorder); j < static_cast<size_t>(rightBorder); ++j) {
                        if((matrix[i][j]<program_end_temp_limit-1) || (matrix[i][j] > program_end_temp_limit+1)){
                            SavedJ = j;
                            break;
                        }else if(i == bottomBorder && j == rightBorder){
                            for (size_t i = 0; i < size_y; ++i) {
                                for (size_t j = 0; j < size_x; ++j) {
                                    colour_threads =  C_to_rgb(matrix[i][j], colour_threads, temperature_limit);
                                    img(j, i, 0, 0) = colour_threads.r;
                                    img(j, i, 0, 1) = colour_threads.g;
                                    img(j, i, 0, 2) = colour_threads.b;
                                }
                            }
                            filename = "images/zEND.png";
                            img.save_png(filename.c_str());
                            return 0;
                        }
                    }
                    if((matrix[i][SavedJ]<program_end_temp_limit-1) || (matrix[i][SavedJ] > program_end_temp_limit+1)){
                        break;
                    }
                }

            filename = "images/im" + std::to_string(h / (100*static_cast<int>(dT/possible_dT)))+".png";
            img.save_png(filename.c_str());
        }
        if(cycle_limit>0)
            if(h>cycle_limit){
                for (size_t i = 0; i < size_y; ++i) {
                    for (size_t j = 0; j < size_x; ++j) {
                        colour_threads =  C_to_rgb(matrix[i][j], colour_threads, temperature_limit);
                        img(j, i, 0, 0) = colour_threads.r;
                        img(j, i, 0, 1) = colour_threads.g;
                        img(j, i, 0, 2) = colour_threads.b;
                    }
                }
                filename = "images/zEND.png";
                img.save_png(filename.c_str());
                return 0;
            }
        ++h;
    }
}

ConfigFileOpt parse_args(int argc, char **argv) {
    //  ##################### Program Parameter Parsing ######################
    std::string filename = "config.conf";
    if (argc == 2) {
        filename = argv[1];
    } else if (argc > 2) {
        std::cerr << "Too many arguments. Usage: \n"
                     "\tprogram [config-filename]\n" << std::endl;
        exit(1);
    }
    //  #####################    Config File Parsing    ######################
    ConfigFileOpt config;
    try {
        config.parse(filename);
    } catch (std::exception &ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        exit(3);
    }
    return config;
}

//void assert_valid_config(const ConfigFileOpt &config) {

//    if (!std::filesystem::exists(config.get_field_filename())) {
//        std::cerr << "Error: File or Directory '" << config.get_field_filename()
//                  << "' do not exist (or can not be created)!"
//                  << std::endl;
//        exit(21);
//    } else if (config.get_field_filename().empty()) {
//        std::cerr << "Error: Field file is empty or missing field file filename!" << std::endl;
//        exit(23);
//    } else if (config.get_delta_t() >=
//               std::pow(std::max(config.get_delta_x(), config.get_delta_y()), 2) / config.get_alpha() / 4) {
//        std::cerr << "Error: Violation of the Von Neumann criteria for input data." << std::endl;
//        exit(23);
//    } else if (config.get_width() < 1000 or config.get_height() < 1000) {
//        std::cerr << "Error: field must be at least 1000*1000" << std::endl;
//        exit(23);
//    }
//}
