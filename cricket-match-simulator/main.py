from series_generator import generate_series, save_to_json

if __name__ == "__main__":
    series_data = generate_series(4545)  # Change number as needed
    save_to_json(series_data)

