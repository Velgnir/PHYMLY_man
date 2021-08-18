//
// Created by myralllka on 3/25/20.
//

#ifndef COUNT_NUMBER_OF_ALL_WORDS_CONFIG_FILE_H
#define COUNT_NUMBER_OF_ALL_WORDS_CONFIG_FILE_H

#include <boost/program_options.hpp>
#include <string>
#include <iostream>
#include <fstream>


#include "exceptions/parser_exeption.h"

class ConfigFileOpt {
public:
    ConfigFileOpt();

    ~ConfigFileOpt() = default;

    void parse(const std::string &file_name);

    // make getters
    [[nodiscard]] const double &get_specific_heat_capacity() const { return specific_heat_capacity; }

    [[nodiscard]] const double &get_thermal_conduction() const { return thermal_conduction; }

    [[nodiscard]] const double &get_density() const { return density; }

    [[nodiscard]] const size_t &get_height() const { return height; }

    [[nodiscard]] const size_t &get_width() const { return width; }

    [[nodiscard]] const double &get_delta_x() const { return delta_x; }

    [[nodiscard]] const double &get_delta_y() const { return delta_y; }

    [[nodiscard]] const double &get_delta_t() const { return delta_t; }

    [[nodiscard]] const size_t &get_data_cycles() const { return data_cycles; };

    [[nodiscard]] const std::string &get_field_filename() const { return field_filename; };

    [[nodiscard]] const double &get_alpha() const { return alpha; };

    [[nodiscard]] const double &get_epsilon() const { return epsilon; };

    [[nodiscard]] const size_t &get_max_number_of_cycles() const { return max_number_of_cycles; };

private:
    void init_opt_description();

    static std::string assert_file_exist(const std::string &f_name);

    // declare all parameters
    double specific_heat_capacity = 0;
    double thermal_conduction = 0;
    double density = 0;
    size_t height = 1000;
    size_t width = 1000;
    double delta_x = 1;
    double delta_y = 1;
    double delta_t = 1;
    size_t data_cycles = 10;
    std::string field_filename{};
    double alpha = 0;
    std::string up_func{};
    double up_func_arg = 0;
    double up_func_arg2 = 0;
    std::string left_func{};
    double left_func_arg = 0;
    double left_func_arg2 = 0;
    std::string right_func{};
    double right_func_arg = 0;
    double right_func_arg2 = 0;
    std::string bottom_func{};
    double bottom_func_arg = 0;
    double bottom_func_arg2 = 0;
    double temp = 0;
    double epsilon = 0.0001;
    size_t max_number_of_cycles = 0;

    boost::program_options::options_description opt_conf{"Config File Options"};
    boost::program_options::variables_map var_map{};
};

#endif //COUNT_NUMBER_OF_ALL_WORDS_CONFIG_FILE_H
