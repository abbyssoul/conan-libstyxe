#include "styxe/styxe.hpp"
#include <cstdlib>  // EXIT_SUCCESS/EXIT_FAILURE


int main() {
    styxe::Parser proc{1024};

    return (styxe::headerSize() > 0 &&
            styxe::headerSize() < proc.maxPossibleMessageSize())
                ? EXIT_SUCCESS
                : EXIT_FAILURE;
}
