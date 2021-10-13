#include <iostream>
#include <fstream>
#include <string>
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
    int all_time = 600;
    std::ifstream input_file(input_file_name);
    if (input_file) {
        std::cout << "file was open" << std::endl;
    } else {
        std::cout << "file wasn't open" << std::endl;
    }
    double dT = config.get_delta_t();
    double dx = config.get_delta_x();
    double dy = config.get_delta_y();
    double alpha = config.get_alpha();
    double k1 = (alpha * dT) / (dx * dx);
    double k2 = (alpha * dT) / (dy * dy);
    double temperature_limit;


    //int lx = config.get_width()/dx;
    //int ly = config.get_height()/dy;
    cimg::CImg<unsigned char> img(100,100,1,3);
    char filename[128];
    uint8_t r,g,b;
    double First_matrix[100][100];
    for (auto &line: First_matrix)
        for (auto &number: line)
            input_file >> number;
    double matrix[100][100];

    for (int j = 0; j < 100; ++j) {
        for (int k = 0; k < 100; ++k) {
            matrix[j][k] = First_matrix[j][k];
        }
    }

    for (auto &line:matrix)
        for (auto number:line)
            if (number>temperature_limit)
                temperature_limit = number;

    for (int h = 0; h < all_time * (1/dT); ++h) {
        for (int i = 0; i < 100; ++i) {
            for (int j = 1; j < 100; ++j) {
                matrix[i][j] = get_formula_result(i,j,First_matrix,k1,k2);
                if (h % 100 == 0) {
                    C_to_rgb(matrix[i][j], r,g,b, temperature_limit);
                    img(j, i, 0, 0) = r;
                    img(j, i, 0, 1) = g;
                    img(j, i, 0, 2) = b;
                }
            }
        }
        for (int j = 0; j < 100; ++j) {
            for (int k = 0; k < 100; ++k) {
                First_matrix[j][k] = matrix[j][k];
            }
        }
        if (h % 100 == 0) {
            sprintf(filename, "images/f-%06d.png", h / 100);
            img.save_png(filename);
        }
    }

    for (auto &line: matrix) {
        for (auto number: line)
            std::cout << number << "  ";
        std::cout << std::endl;
    }
    return 0;
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
