import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind
import os


def load_and_prep_data(file_path):
    df_control = pd.read_excel(file_path, sheet_name="Control Group")  #
    df_test = pd.read_excel(file_path, sheet_name="Test Group")  #
    return df_control, df_test


def visualize_data(df_control, df_test, base_dir):
    plt.figure(figsize=(10, 6))
    data_to_plot = [df_control["Purchase"], df_test["Purchase"]]
    sns.boxplot(data=data_to_plot)
    plt.xticks([0, 1], ['Control (Maximum Bidding)', 'Test (Average Bidding)'])
    plt.title('Purchase Distribution: Control vs Test')

    output_path = os.path.join(base_dir, 'outputs')
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    plt.savefig(os.path.join(output_path, 'purchase_comparison.png'))
    print(f"Grafik '{output_path}' klasörüne kaydedildi.")


def perform_ab_test(df_control, df_test):
    _, p_norm_c = shapiro(df_control["Purchase"])
    _, p_norm_t = shapiro(df_test["Purchase"])

    _, p_levene = levene(df_control["Purchase"], df_test["Purchase"])

    print(f"Normality P-Values: Control={p_norm_c:.4f}, Test={p_norm_t:.4f}")
    print(f"Levene P-Value: {p_levene:.4f}")

    if p_norm_c > 0.05 and p_norm_t > 0.05 and p_levene > 0.05:
        t_stat, p_val = ttest_ind(df_control["Purchase"], df_test["Purchase"], equal_var=True)
        print(f"\nIndependent T-Test Result: P-Value = {p_val:.4f}")  #
        return p_val
    else:
        print("Varsayımlar sağlanmadığı için alternatif testler (Mann-Whitney U) gerekebilir.")
        return None


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))

    BASE_DIR = os.path.dirname(current_dir)
    DATA_PATH = os.path.join(BASE_DIR, "data/ab_testing.xlsx")

    print(f"Aranan dosya yolu: {DATA_PATH}")

    control, test = load_and_prep_data(DATA_PATH)
    visualize_data(control, test, BASE_DIR)
    perform_ab_test(control, test)