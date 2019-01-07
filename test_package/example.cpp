#include "styxe/9p2000.hpp"
#include "styxe/version.hpp"
#include <cstdlib>  // EXIT_SUCCESS/EXIT_FAILURE


int main() {
    styxe::Protocol proc(1024);

    return (styxe::Protocol::headerSize() > 0 &&
            styxe::Protocol::headerSize() < proc.maxPossibleMessageSize())
                ? EXIT_SUCCESS
                : EXIT_FAILURE;
}
