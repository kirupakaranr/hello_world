
cmake_minimum_required (VERSION 3.7)


project (helloworld VERSION 1.0.0)

if (CONAN_EXPORTED)
	include (${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup()
else()
	include (build/scripts/conan.cmake)
	conan_cmake_run (CONANFILE conanfile.py
		BASIC_SETUP
		BUILD missing
		UPDATE)
endif ()

set (CMAKE_MODULE_PATH ${CMAKE_CURRENT_BINARY_DIR})

find_package (fmt)

add_subdirectory (src)
