// This is a personal academic project. Dear PVS-Studio, please check it.
// // PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
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
    if (input_file) {
        std::cout << "file was open" << std::endl;
    } else {
        std::cout << "file wasn't open" << std::endl;
    }
    auto dT = config.get_delta_t();
    auto dx = config.get_delta_x();
    auto dy = config.get_delta_y();
    auto alpha = config.get_alpha();
    auto size_x = config.get_width();
    auto size_y = config.get_height();
    auto program_end_temp_limit = config.get_temperature_limit();
    int size_z=1;
    int number_of_colour_threads = 3;
    double k1 = (alpha * dT) / (dx * dx);
    double k2 = (alpha * dT) / (dy * dy);
    double temperature_limit;
    std::vector<std::vector<double>> matrix;
    std::vector<std::vector<double>> First_matrix;
    cimg::CImg<unsigned char> img(size_x,size_y,size_z,number_of_colour_threads);
    char filename[128];
    uint8_t r,g,b;

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
        for (size_t i = 0; i < size_y; ++i) {
            for (size_t j = 1; j < size_x; ++j) {
                matrix[i][j] = get_formula_result(i,j,First_matrix,k1,k2,size_x,size_y);
            }
        }
        if (h % 100 == 0) {
            for (size_t i = 0; i < size_y; ++i) {
                for (size_t j = 0; j < size_x; ++j) {
                        C_to_rgb(matrix[i][j], r,g,b, temperature_limit);
                        img(j, i, 0, 0) = r;
                        img(j, i, 0, 1) = g;
                        img(j, i, 0, 2) = b;
                    }
                }
        }
        First_matrix = matrix;
        if (h % 100 == 0) {
            sprintf(filename, "images/f-%06d.png", h / 100);
            img.save_png(filename);
        }
        for (int i = 0; i < size_y*size_x; ++i) {
            if (matrix[i/size_x][i%size_x]<program_end_temp_limit){
                break;
            } else if(i/size_x == size_x-1 && i%size_x == size_y-1){
                return 0;
            };
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
