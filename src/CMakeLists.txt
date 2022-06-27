
set (TARGET helloworld)

add_executable ( ${TARGET} main.cpp )

target_link_libraries ( ${TARGET} fmt::fmt)

install (TARGETS ${TARGET} DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)
