//
// Created by paulo on 09.08.21.
//

#include <iostream>
#include <math.h>
#include <SFML/Graphics.hpp>

void C_to_rgb(const double Temperature, uint8_t &r, uint8_t &g, uint8_t &b, const double Temperature_limit);

void draw(const int rows, const int colums, double matrix[100][100],
          sf::RenderWindow& window,
          sf::RectangleShape picture[100][100],
          const double temperature_limit);

