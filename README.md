# Stress & Safety Factor Calculator

A Python tool to calculate axial stress and safety 
factor for mechanical components under load.

## What it does
- Takes force (N), cross-section area (m²), and 
  material yield stress (MPa) as input
- Calculates axial stress (σ = F/A)
- Calculates safety factor (yield stress / actual stress)
- Compares against a user-defined required safety factor
- Saves a complete analysis report to a text file

## How to run
python stress_calculator.py

## Example
Input:
- Force: 5000 N
- Area: 0.005 m²
- Yield Stress: 250 MPa
- Required Safety Factor: 2

Output:
- Calculated Stress: 1.00 MPa
- Safety Factor: 250.00
- Status: SAFE

## Built using
Python — functions, file handling, user input, 
conditional logic

## Author
Chanchal — M.Tech Mechanical System Design
