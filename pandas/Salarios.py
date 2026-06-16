import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings #para ignorar los warnings de sklearn
warnings.filterwarnings("ignore")
df = pd.read_csv("salary.csv")
print(df.head(6))
plt.scatter(df["YearsExperience"], df["Salary"])
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")
plt.show()
model = LinearRegression()
model.fit(df[["YearsExperience"]], df["Salary"])
# Aquí creas bien el array de NumPy
salary_15_years_experience = np.array([[15]]) #para predecir el salario de una persona con 15 años de experiencia
#tiene que ser un array de 2 dimensiones, por eso usamos doble corchete
prediction = model.predict(salary_15_years_experience)


