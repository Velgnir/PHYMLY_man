// This is a personal academic project. Dear PVS-Studio, please check it.
// // PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com
//

//
// Created by paulo on 15.09.21.
#include <iostream>
#include <vector>

double get_formula_result(const int i, const int j,std::vector<std::vector<double>> First_matrix,
                          const double k1, const double k2, const size_t width, const size_t height){
    if (i == 0 && j == static_cast<int>(width-1)){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j - 1] - First_matrix[i][j]));

    } else if (i == static_cast<int>(height-1) && j== static_cast<int>(width-1)){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i - 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j - 1] - First_matrix[i][j]));

    } else if (i == 0){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j + 1] + First_matrix[i][j - 1] - 2 * First_matrix[i][j]));

    } else if (i == static_cast<int>(height-1)){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i - 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j + 1] + First_matrix[i][j - 1] - 2 * First_matrix[i][j]));

    }else if (j == static_cast<int>(width-1)){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] + First_matrix[i - 1][j] - 2 * First_matrix[i][j])) +
               (k2 * (First_matrix[i][j - 1] - First_matrix[i][j]));

    } else {
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] + First_matrix[i - 1][j] - 2 * First_matrix[i][j])) +
               (k2 * (First_matrix[i][j + 1] + First_matrix[i][j - 1] - 2 * First_matrix[i][j]));
    }
}
