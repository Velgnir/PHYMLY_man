#include <iostream>
#include <fstream>
#include <string>
#include <iostream>
#include <fstream>
#include <filesystem>
#include "formula.hpp"

int main(int argc, char *argv[]) {
    std::string input_file_name;
    if (argc > 1) {
        input_file_name = argv[2];
    } else {
        input_file_name = "input.txt";
    }
    double First_matrix[100][100];
    if ((!std::filesystem::exists("input.txt")))
        return -1;
    /*
    int lx = 1, ly = 1;
    double dX = 0.01, dY = 0.01;
     */
    int all_time = 6000;
    double dT = 0.1;
    std::ifstream input_file(input_file_name);
    if (input_file) {
        std::cout << "file was open" << std::endl;
    } else {
        std::cout << "file wasn't open" << std::endl;
    }
    for (auto &line: First_matrix)
        for (auto &number: line)
            input_file >> number;
    double matrix[100][100];

    for (int j = 0; j < 100; ++j) {
        for (int k = 0; k < 100; ++k) {
            matrix[j][k] = First_matrix[j][k];
        }
    }

    double dx = 0.01010101010101;
    double dy = dx;
    double alpha = 0.000244;
    double k1 = (alpha * dT) / (dx * dx);
    double k2 = (alpha * dT) / (dy * dy);
    double temperature_limit;

    for (auto &line:matrix)
        for (auto number:line)
            if (number>temperature_limit)
                temperature_limit = number;

    for (int h = 0; h < all_time * 10; ++h) {
        for (int i = 0; i < 100; ++i) {
            for (int j = 1; j < 100; ++j) {
                matrix[i][j] = get_formula_result(i,j,First_matrix,k1,k2);
            }
        }
        for (int j = 0; j < 100; ++j) {
            for (int k = 0; k < 100; ++k) {
                First_matrix[j][k] = matrix[j][k];
            }
        }
        std::cout << "time " << (h / 10) << "." << h % 10 << " s" << std::endl;

    }


    for (auto &line: matrix) {
        for (auto number: line)
            std::cout << number << "  ";
        std::cout << std::endl;
    }
    return 0;
}