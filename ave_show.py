import pandas as pd

# データをCSVファイルとして読み込む
file_path = "/home/mdxuser/sasaki/results_combined_norm.csv"  # データファイルのパスを指定
df = pd.read_csv(file_path)

# val_rmse と test_rmse の平均と分散をターゲットごとに計算
statistics = df.groupby('target').agg(
    val_rmse_mean=('val_rmse', 'mean'),
    val_rmse_variance=('val_rmse', 'var'),
    test_rmse_mean=('test_rmse', 'mean'),
    test_rmse_variance=('test_rmse', 'var')
).reset_index()

# 結果を表示
print("RMSEの平均と分散:")
print(statistics)

# 必要なら結果を新しいCSVファイルに保存
output_file = "rmse_statistics_nn_norm_0.4.csv"
statistics.to_csv(output_file, index=False)
print(f"RMSEの平均と分散を {output_file} に保存しました。")