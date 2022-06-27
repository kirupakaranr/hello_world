#include "fmt/color.h"

int main() {
    fmt::print(fg(fmt::terminal_color::cyan), "Hello World !!!\n");
    return 0;
}
