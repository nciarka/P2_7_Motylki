import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/data1.csv")
#Filtrowanie lat 2000-2016
df_filtered = df[(df["year"] >= 2000) & (df["year"] <= 2016)]


#Wykres i zmiana dla wszystkich gatunków

yearly_total = df_filtered.groupby("year")["count"].sum()

plt.figure(figsize=(10, 5))
plt.plot(yearly_total.index, yearly_total.values, marker='o', color='black', linewidth=2)
plt.title("Laczna liczebnosc wszystkich motyli (2000-2016)")
plt.xlabel("Rok")
plt.ylabel("Liczba motyli")
plt.xticks(range(2000, 2017, 2))
plt.grid(True)
plt.show()

# Zmiana procentowa dla wszystkich gatunków
start_total = yearly_total.loc[2000]
end_total = yearly_total.loc[2016]

change_total = ((end_total - start_total) / start_total) * 100

print(f"ZMIANA PROCENTOWA DLA OGOLNEJ LICZBY MOTYLI (2000-2016): {change_total:.2f}%\n")

#Porównanie i zmiana poszczególnych gatunków

top_5_species = df_filtered.groupby("genus_species")["count"].sum().nlargest(5).index
df_top5 = df_filtered[df_filtered["genus_species"].isin(top_5_species)]

pivot_data = df_top5.pivot_table(index="year",
                                 columns="genus_species",
                                 values="count",
                                 aggfunc="sum",
                                 fill_value=0)

pivot_data.plot(figsize=(12, 6), marker='o')

plt.title("Zmiany liczebnosci 5 najpopularniejszych gatunkow (2000-2016)")
plt.xlabel("Rok")
plt.ylabel("Liczba motyli")
plt.xticks(range(2000, 2017, 2))
plt.grid(True)
plt.legend(title="Gatunek", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Zmiana procentowa dla poszczególnych gatunków
print("ZMIANA DLA TOP 5 GATUNKOW")

for species in pivot_data.columns:
    start_val = pivot_data.loc[2000, species]
    end_val = pivot_data.loc[2016, species]

    if start_val > 0:
        change_species = ((end_val - start_val) / start_val) * 100
        print(f"- {species}: {change_species:.2f}%")
    else:
        print(f"- {species}: Niemożliwe do obliczenia (początkowa wartość w 2000 to 0)")

#Współczynnik zmienności
yearly_species_sum = df_filtered.pivot_table(index="year",
                                             columns="genus_species",
                                             values="count",
                                             aggfunc="sum",
                                             fill_value=0)

species_cv = (yearly_species_sum.std() / yearly_species_sum.mean()) * 100

# Filtrowanie nieskończoności i sortowanie
species_cv = species_cv.replace([float('inf'), -float('inf')], pd.NA).dropna()
species_cv = species_cv.sort_values(ascending=False)

print("\nTOP 5 GATUNKÓW O NAJWIĘKSZYCH WAHANIACH POPULACJI W LATACH 2000-2016")
for species, cv in species_cv.head(5).items():
    print(f"- {species}: Współczynnik zmienności = {cv:.2f}%")

print("\nTOP 5 NAJBARDZIEJ STABILNYCH GATUNKÓW W LATACH 2000-2016")
for species, cv in species_cv.tail(5).items():
    print(f"- {species}: Współczynnik zmienności = {cv:.2f}%")
