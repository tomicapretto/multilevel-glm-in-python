import arviz as az

from bambi import Model
from pandas import read_csv

if __name__ == '__main__':
    # Requires to set the working directory to the project directory
    gaussian_data = read_csv("./data/Gaussian_identity_data.csv")
    gamma_data = read_csv("./data/Gamma_log_data.csv")

    model = Model("y ~ x1 + x2 + x3 + (1 | group_index)", gaussian_data)
    model_result = model.fit()

    # Print model summary
    print(model)

    # Print posterior summary
    print(az.summary(model_result))

    model = Model("y ~ x1 + x2 + x3 + (1 | group_index)", gamma_data, family="gamma", link="log")
    model_result = model.fit()

    # Print model summary
    print(model)

    # Print posterior summary
    print(az.summary(model_result))