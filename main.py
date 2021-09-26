from app import create_app

if __name__ == "__main__":
    # TODO: Add swagger integration
    app = create_app()
    app.run(host="0.0.0.0")
