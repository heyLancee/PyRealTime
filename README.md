# PyRealTime

## Introduction

PyRealTime is a Python module for real-time simulation. It provides a simple interface for creating and managing real-time simulations.

## Installation

the module has not been published to pypi, so you need to install it manually. The subdirectory pyflywheel is the module, which should be moved to the python module path or working directory.

## Usage

The `RealTimeSimulation` class provides a `sample_time` parameter, which is the sampling time of the simulation. The simulation will run with the period of `sample_time`. Therefore, the callback function is necessary when starting the simulation.
