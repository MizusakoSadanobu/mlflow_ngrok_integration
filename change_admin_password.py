import requests

if __name__ == "__main__":
    password_now = input("input current password: ")
    password_new = input("input new password: ")
    host = input("input host (ex. http://0.0.0.0:5000): ")

    response = requests.patch(
        f"{host}/api/2.0/mlflow/users/update-password",
        auth=("admin", "password"),
        json={"username": password_now, "password": password_new},
    )

    response.raise_for_status()
    print("パスワードが正常に変更されました。")