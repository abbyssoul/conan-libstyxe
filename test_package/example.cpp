#include "styxe/9p2000.hpp"
#include "styxe/version.hpp"


int main() {
    styxe::Protocol proc(1024);

    return (styxe::Protocol::headerSize() > 0 &&
            proc.maxPossibleMessageSize() < styxe::Protocol::headerSize())
                ? EXIT_SUCCESS
                : EXIT_FAILURE;
}
