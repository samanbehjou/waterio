cmake_minimum_required(VERSION 3.20)
project(solsysgen_native LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Make pybind11 find the active Python (venv/conda) automatically
set(PYBIND11_FINDPYTHON ON)

find_package(pybind11 CONFIG REQUIRED)

# Build a Python extension module named "solsysgen_native"
# It will be importable in Python as: import solsysgen_native
pybind11_add_module(solsysgen_native
    cpp/core.cpp
)

# Warnings
if (MSVC)
    target_compile_options(solsysgen_native PRIVATE /W4)
else()
    target_compile_options(solsysgen_native PRIVATE -Wall -Wextra -Wpedantic)
endif()

# Install to current directory (useful for local testing / editable installs)
install(TARGETS solsysgen_native
    LIBRARY DESTINATION .
    RUNTIME DESTINATION .
    ARCHIVE DESTINATION .
)

