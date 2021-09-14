//
// Created by paulo on 15.09.21.
//

double get_formula_result(const int i, const int j, double First_matrix[100][100], const double k1, const double k2){
    if (i == 0 && j == 99){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j - 1] - First_matrix[i][j]));

    } else if (i == 99 && j== 99){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i - 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j - 1] - First_matrix[i][j]));

    } else if (i == 0){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j + 1] + First_matrix[i][j - 1] - 2 * First_matrix[i][j]));

    } else if (i == 99){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i - 1][j] - First_matrix[i][j])) +
               (k2 * (First_matrix[i][j + 1] + First_matrix[i][j - 1] - 2 * First_matrix[i][j]));

    }else if (j == 99){
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] + First_matrix[i - 1][j] - 2 * First_matrix[i][j])) +
               (k2 * (First_matrix[i][j - 1] - First_matrix[i][j]));

    } else {
        return First_matrix[i][j] +
               (k1 * (First_matrix[i + 1][j] + First_matrix[i - 1][j] - 2 * First_matrix[i][j])) +
               (k2 * (First_matrix[i][j + 1] + First_matrix[i][j - 1] - 2 * First_matrix[i][j]));
    }
}