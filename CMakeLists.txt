cmake_minimum_required(VERSION 3.18)
project(waterio_core LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE cpp/core.cpp)

# install INTO the waterio package directory
install(TARGETS _core
  LIBRARY DESTINATION waterio
  RUNTIME DESTINATION waterio
)

