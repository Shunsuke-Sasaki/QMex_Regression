import pandas as pd
from sympy import sympify, expand

# CSVファイルを読み込む
file_path = "/home/mdxuser/sasaki/rmse_sr.csv"  # ファイルパスを指定してください
data = pd.read_csv(file_path)

# SymPyで式を展開
def expand_equation(equation):
    try:
        sympy_expr = sympify(equation)  # 式をSymPyオブジェクトに変換
        expanded_expr = expand(sympy_expr)  # 多項式展開
        return str(expanded_expr)  # 結果を文字列として返す
    except Exception as e:
        return f"Error: {e}"  # エラーの場合はエラー内容を返す

# 新しい列を作成して展開した式を格納
data["Expanded Equation"] = data["Simplified Equation"].apply(expand_equation)

# 結果を保存または表示
output_file = "expanded_equations.csv"
data.to_csv(output_file, index=False)
print(f"展開した式を保存しました: {output_file}")