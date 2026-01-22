#include <pybind11/pybind11.h>

namespace py = pybind11;

class Counter {
public:
    explicit Counter(int start) : value(start) {}
    int inc() { return ++value; }
private:
    int value;
};

PYBIND11_MODULE(_core, m) {
    m.doc() = "Example C++ extension (pybind11)";
    py::class_<Counter>(m, "Counter")
        .def(py::init<int>(), py::arg("start"))
        .def("inc", &Counter::inc, "Increment and return the counter");
}
