#include <iostream>
#include <string>
#include <mpi.h>

int main(int argc, char *argv[]){
    int rank,length,size;
    char name[80];
    int k=100;
    std::cin>>k;
    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    MPI_Comm_size(MPI_COMM_WORLD, &size);

    MPI_Get_processor_name(name, &length);


    const int N=k,M=k;
    double matrix[N][M];
    MPI_Status status;
    if (rank == 0) {
        for (size_t i=0; i<M; ++i)
            for (size_t j=0; j<100; ++j)
                matrix[i][j] = 101;
        MPI_Send(matrix, N*M, MPI_DOUBLE, 1, 0, MPI_COMM_WORLD);
    }
    else if (rank == 1) {
        MPI_Recv(matrix, N*M, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        for (size_t i=0; i<M; ++i) {
            for (size_t j = 0; j < 100; ++j)
                std::cout<<matrix[i][j]<<" ";
            std::cout<<std::endl;
        }
    }
    std::cout<<rank<<": "<<0<<std::endl;
    return 0;
}
