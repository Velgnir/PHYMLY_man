#include <iostream>
#include <string>
#include <vector>
#include <filesystem>
#include <mpi.h>
#include "files/config_file.h"
#include "formula.hpp"
#include "CImg.h"
#include "visualization.hpp"

namespace cimg = cimg_library;

ConfigFileOpt parse_args(int argc, char **argv);
//void assert_valid_config(const ConfigFileOpt &conf);

int main(int argc, char *argv[]){
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
        input_file_name = "input.txt";
    }
    ConfigFileOpt config = parse_args(argc, argv);

    if ((!std::filesystem::exists(config_file_name))) {
        std::cerr << "File " << config_file_name << " wasn't found" << std::endl;
        config_file_name = "config.conf";
    }
    std::ifstream input_file(input_file_name);
    auto size_x = config.get_width();
    auto size_y = config.get_height();
    auto dT = config.get_delta_t()/2.0;
    auto dx = config.get_delta_x();
    auto dy = config.get_delta_y();
    auto alpha = config.get_alpha();
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

    int rank,length,size;
    char name[80];

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    MPI_Comm_size(MPI_COMM_WORLD, &size);

    MPI_Get_processor_name(name, &length);

    const size_t N=size_x,M=size_y;
    int T=size;
    double matrix[M][N];
    double bufferST[static_cast<size_t>(N*M/T)], bufferEnd[static_cast<size_t>(N*M/T)+N*M -static_cast<size_t>(N*M/T)*T];
    //std::cout<<static_cast<size_t>(N*M/T)<<"\n"<<static_cast<size_t>(N*M/T)+N*M -static_cast<size_t>(N*M/T)*T<<"\n";
    size_t start,i,j;
    if (rank == 0) {
        cimg::CImg<unsigned char> img(size_x,size_y,size_z,number_of_colour_threads);
        std::string filename;
        rgb_t colour_threads;

        for (size_t m2=0; m2<M; ++m2)
            for (size_t n2=0; n2<N; ++n2)
                input_file >> matrix[m2][n2];
        /*for (size_t m2=0; m2<350; ++m2) {
            for (size_t n2 = 0; n2 < 700; ++n2)
                std::cout<<matrix[m2][n2]<<" ";
            std::cout<<"\n\n\n";
        }*/

        for (size_t m2=0; m2<M; ++m2)
            for (size_t n2=0; n2<N; ++n2)
                if(matrix[m2][n2]>temperature_limit)
                    temperature_limit=matrix[m2][n2];
        /*for (size_t m2=0; m2<M; ++m2) {
            for (size_t n2 = 0; n2 < N; ++n2)
                std::cout<<matrix[m2][n2]<<" ";
            std::cout<<"\n";
        }*/
        start=static_cast<int>(N*M/T)*(T-1);
        for(size_t z=0; z<cycle_limit;++z){

            for (int threads=1; threads<T; ++threads) {
                MPI_Send(matrix, N * M, MPI_DOUBLE, threads, 0, MPI_COMM_WORLD);
            }
            for (int l=0; l<size_x*size_y-start;++l){
                i = (l+start)/size_x;
                j = (l+start)%size_x;
                if(((j<leftBorder) || (j>rightBorder-1) || (i<upBorder) || (i>bottomBorder))){
                    bufferEnd[l]=matrix[i][j];
                }else if (i == 0 && j == static_cast<size_t>(size_x-1)){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i + 1][j] - matrix[i][j])) +
                    (k2 * (matrix[i][j - 1] - matrix[i][j]));

                }else if (j == 0 && i == 0){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i+ 1][j] - matrix[i][j])) +
                    (k2 * (matrix[i][j + 1]  -  matrix[i][j]));

                } else if (i == static_cast<size_t>(size_y-1) && j== static_cast<size_t>(size_x-1)){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i - 1][j] - matrix[i][j])) +
                    (k2 * (matrix[i][j - 1] - matrix[i][j]));

                } else if (i == 0){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i + 1][j] - matrix[i][j])) +
                    (k2 * (matrix[i][j + 1] + matrix[i][j - 1] - 2 * matrix[i][j]));

                }else if (j == 0 && i == static_cast<size_t>(size_y-1)){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i - 1][j] - matrix[i][j])) +
                    (k2 * (matrix[i][j + 1] - matrix[i][j]));

                } else if (i == static_cast<size_t>(size_y-1)){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i - 1][j] - matrix[i][j])) +
                    (k2 * (matrix[i][j + 1] + matrix[i][j - 1] - 2 * matrix[i][j]));

                }else if (j == static_cast<size_t>(size_x-1)){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i + 1][j] + matrix[i - 1][j] - 2 * matrix[i][j])) +
                    (k2 * (matrix[i][j - 1] - matrix[i][j]));

                }else if (j == 0){
                    bufferEnd[l] = matrix[i][j] +
                    (k1 * (matrix[i + 1][j] + matrix[i - 1][j] - 2 * matrix[i][j])) +
                    (k2 * (matrix[i][j + 1] - matrix[i][j]));

                }else {
                    bufferEnd[l] = matrix[i][j] +
                                  (k1 * (matrix[i + 1][j] + matrix[i - 1][j] - 2 * matrix[i][j])) +
                                  (k2 * (matrix[i][j + 1] + matrix[i][j - 1] - 2 * matrix[i][j]));
                }
            }

            for (int l=0; l<size_x*size_y-start;++l) {
                i = (l + start) / size_x;
                j = (l + start) % size_x;

                matrix[i][j]=bufferEnd[l];
            }

                //std::cout<<"END OF THE WORlD\n";
            for (int m=0; m<T-1; ++m){
                MPI_Recv(bufferST, N*M, MPI_DOUBLE, m+1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
                for (int n=0; n<static_cast<int>(N * M / T); ++n){
                        matrix[(m*static_cast<int>(N * M / T)+n)/size_x][(m*static_cast<int>(N * M / T)+n)%size_x]=bufferST[n];
                        //std::cout<<(m*static_cast<int>(N * M / T)+n)/size_x<<"  "<<(m*static_cast<int>(N * M / T)+n)%size_x<<"  -  i  j - "<<bufferST[n]<<"\n";
                    }
            }
            if (z % (100*static_cast<int>(dT/possible_dT)) == 0) {
                for (size_t i = 0; i < size_y; ++i) {
                    for (size_t j = 0; j < size_x; ++j) {
                        colour_threads =  C_to_rgb(matrix[i][j], colour_threads, temperature_limit);
                        img(j, i, 0, 0) = colour_threads.r;
                        img(j, i, 0, 1) = colour_threads.g;
                        img(j, i, 0, 2) = colour_threads.b;
                    }
                }
                filename = "images/im" + std::to_string(z / (100*static_cast<int>(dT/possible_dT)))+".png";
                img.save_png(filename.c_str());
            }
        }
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
    } else{
        start=static_cast<int>(N*M/T)*(rank-1);
        for(size_t z=0; z<cycle_limit; ++z){
            MPI_Recv(matrix, N*M, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            /*for (size_t m2=0; m2<N; ++m2) {
                for (size_t n2 = 0; n2 < M; ++n2)
                    std::cout<<matrix[m2][n2]<<" ";
                std::cout<<"\n";
            }*/
            for(size_t l = 0; l<static_cast<int>(N*M/T); ++l){
                i = (l+start)/size_x;
                j = (l+start)%size_x;
                if(((j<leftBorder) || (j>rightBorder-1) || (i<upBorder) || (i>bottomBorder))){
                    bufferST[l]=matrix[i][j];
                }else if (i == 0 && j == static_cast<size_t>(size_x-1)){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i + 1][j] - matrix[i][j])) +
                           (k2 * (matrix[i][j - 1] - matrix[i][j]));

                }else if (j == 0 && i == 0){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i+ 1][j] - matrix[i][j])) +
                           (k2 * (matrix[i][j + 1]  -  matrix[i][j]));

                } else if (i == static_cast<size_t>(size_y-1) && j== static_cast<size_t>(size_x-1)){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i - 1][j] - matrix[i][j])) +
                           (k2 * (matrix[i][j - 1] - matrix[i][j]));

                } else if (i == 0){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i + 1][j] - matrix[i][j])) +
                           (k2 * (matrix[i][j + 1] + matrix[i][j - 1] - 2 * matrix[i][j]));

                }else if (j == 0 && i == static_cast<size_t>(size_y-1)){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i - 1][j] - matrix[i][j])) +
                           (k2 * (matrix[i][j + 1] - matrix[i][j]));

                } else if (i == static_cast<size_t>(size_y-1)){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i - 1][j] - matrix[i][j])) +
                           (k2 * (matrix[i][j + 1] + matrix[i][j - 1] - 2 * matrix[i][j]));

                }else if (j == static_cast<size_t>(size_x-1)){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i + 1][j] + matrix[i - 1][j] - 2 * matrix[i][j])) +
                           (k2 * (matrix[i][j - 1] - matrix[i][j]));

                }else if (j == 0){
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i + 1][j] + matrix[i - 1][j] - 2 * matrix[i][j])) +
                           (k2 * (matrix[i][j + 1] - matrix[i][j]));

                }else {
                    bufferST[l] = matrix[i][j] +
                           (k1 * (matrix[i + 1][j] + matrix[i - 1][j] - 2 * matrix[i][j])) +
                           (k2 * (matrix[i][j + 1] + matrix[i][j - 1] - 2 * matrix[i][j]));
                }
                //if(j==0)
                 //   std::cout<<"\n\n\n";
                //std::cout<<i<<" "<<j<<" "<<l<<" - i j l"<<bufferST[l]<<"\n";
            }

            MPI_Send(bufferST, static_cast<int>(N*M/T), MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
        }

    }
    MPI_Finalize();
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
