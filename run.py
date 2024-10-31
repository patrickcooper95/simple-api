import subprocess

from simple_api import create_app


if __name__ == "__main__":

    app = create_app()

    # If the database is newly created, add the `items` data
    if subprocess.run(
            ["flask", "--app", "simple_api", "init-db"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
    ).returncode == 0:
        subprocess.run(["flask", "--app", "simple_api", "seed-db"])

    app.run(host='0.0.0.0', port=8080)
