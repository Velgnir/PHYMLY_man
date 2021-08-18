//
// Created by myralllka on 3/25/20.
//

#include <filesystem>
#include "files/config_file.h"

namespace po = boost::program_options;

ConfigFileOpt::ConfigFileOpt() {
    init_opt_description();
}

void ConfigFileOpt::init_opt_description() {
    opt_conf.add_options()
            ("main.specific_heat_capacity", po::value<double>(&specific_heat_capacity), "specific heat capacity ")
            ("main.thermal_conduction", po::value<double>(&thermal_conduction), "thermal conduction")
            ("main.density", po::value<double>(&density), "density")
            ("main.epsilon", po::value<double>(&epsilon), "the acceptable temperature error for equality condition")
            ("field-properties.height", po::value<size_t>(&height), "field height")
            ("field-properties.width", po::value<size_t>(&width), "field width")
            ("main.delta_x", po::value<double>(&delta_x), "delta_x")
            ("main.delta_y", po::value<double>(&delta_y), "delta_y")
            ("main.delta_t", po::value<double>(&delta_t), "delta_t")
            ("main.data_cycles", po::value<size_t>(&data_cycles), "data_cycles")
            ("field-properties.output_file", po::value<std::string>(&field_filename), "field filename")
            ("field-properties.up_func", po::value<std::string>(&up_func),"up_func")
            ("field-properties.up_func_arg", po::value<double>(&up_func_arg),"up_func_arg")
            ("field-properties.up_func_arg2", po::value<double>(&up_func_arg2),"up_func_arg2")
            ("field-properties.left_func", po::value<std::string>(&left_func),"left_func")
            ("field-properties.left_func_arg", po::value<double>(&left_func_arg),"left_func_arg")
            ("field-properties.left_func_arg2", po::value<double>(&left_func_arg2),"left_func_arg2")
            ("field-properties.right_func", po::value<std::string>(&right_func),"right_func")
            ("field-properties.right_func_arg", po::value<double>(&right_func_arg),"right_func_arg")
            ("field-properties.right_func_arg2", po::value<double>(&right_func_arg2),"right_func_arg2")
            ("field-properties.bottom_func", po::value<std::string>(&bottom_func),"bottom_func")
            ("field-properties.bottom_func_arg", po::value<double>(&bottom_func_arg),"bottom_func_arg")
            ("field-properties.bottom_func_arg2", po::value<double>(&bottom_func_arg2),"bottom_func_arg2")
            ("field-properties.temp", po::value<double>(&temp),"temp")
            ("main.max_number_of_cycles", po::value<size_t>(&max_number_of_cycles),"max_number_of_cycles");
}

void ConfigFileOpt::parse(const std::string &file_name) {
    try {
        std::ifstream conf_file(assert_file_exist(file_name));
        po::store(po::parse_config_file(conf_file, opt_conf), var_map);
        po::notify(var_map);
    } catch (std::exception &E) {
        std::cerr << E.what() << std::endl;
        throw OptionsParseException();
    }
    alpha = get_thermal_conduction() / get_density() / get_specific_heat_capacity();
}

std::string ConfigFileOpt::assert_file_exist(const std::string &f_name) {
    if (!std::filesystem::exists(f_name)) {
        throw std::invalid_argument("File " + f_name + " not found!");
    }
    return f_name;
}
