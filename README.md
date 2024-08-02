# DBSCAN Clustering on Wholesale Customers Dataset

This project demonstrates the application of the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm on the Wholesale Customers Dataset. The goal is to identify distinct clusters of customers based on their spending habits.

## Project Overview

The project involves the following steps:

1. **Data Preprocessing**: Standardizing the dataset to ensure fair distance measurements.
2. **DBSCAN Clustering**: Applying the DBSCAN algorithm to the standardized data.
3. **Visualization**: Creating scatter plots and pair plots to visualize the clustering results.

## Dataset

The dataset used is the [Wholesale Customers Dataset](https://archive.ics.uci.edu/ml/datasets/wholesale+customers) from the UCI Machine Learning Repository. It contains the following features:

- Fresh
- Milk
- Grocery
- Frozen
- Detergents_Paper
- Delicassen

## Installation

To run the code, ensure you have the following libraries installed:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
