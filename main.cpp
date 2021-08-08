#include <SFML/Graphics.hpp>
#include <iostream>
#include <fstream>
#include <unistd.h>
#include "visualization.hpp"

int main(int argc, char *argv[]) {

    std::string file_path;
    if (argc > 1) {
        file_path = argv[2];
    } else {
        file_path = "../input.txt";
    }
    double First_matrix[100][100];
    /*
    int lx = 1, ly = 1;
    double dX = 0.01, dY = 0.01;
     */
    int all_time = 10000;
    double dT = 0.1;
    std::ifstream input_file(file_path);
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

    sf::RenderWindow window(sf::VideoMode(100, 100), "2D Heat");
    sf::RectangleShape picture[100][100];
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j < 100; ++j) {
            picture[i][j].setPosition(sf::Vector2f(j, i));
            picture[i][j].setSize(sf::Vector2f(1, 1));
        }
    }
    int r, g, b;

    for (int h = 0; h < all_time * 10; ++h) {
        for (int i = 1; i < 100; ++i) {
            for (int j = 1; j < 100; ++j) {
                matrix[i][j] = First_matrix[i][j] +
                               (k1 * (First_matrix[i + 1][j] + First_matrix[i - 1][j] - 2 * First_matrix[i][j])) +
                               (k2 * (First_matrix[i][j + 1] + First_matrix[i][j - 1] - 2 * First_matrix[i][j]));
                C_to_rgb(matrix[i][j], r, g, b);
                picture[i][j].setFillColor(sf::Color(r, g, b, 255));
                window.draw(picture[i][j]);
            }
            for (int j = 0; j < 100; ++j) {
                matrix[j][99] = matrix[j][98];
                matrix[0][j] = matrix[1][j];
                matrix[99][j] = matrix[98][j];
            }
        }
        for (int j = 0; j < 100; ++j) {
            for (int k = 0; k < 100; ++k) {
                First_matrix[j][k] = matrix[j][k];
            }
        }
        window.clear();
        for (auto &line: picture)
            for (auto &pixel: line)
                window.draw(pixel);
        window.display();
        std::cout << "time " << (size_t) (h / 10) << "." << h % 10 << " s" << std::endl;

    }


    for (auto &line: matrix) {
        for (auto number: line)
            std::cout << number << "  ";
        std::cout << std::endl;
    }
    return 0;
}