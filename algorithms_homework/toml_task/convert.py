import argparse
import json
from pathlib import Path
import tomllib  # Входит в стандартную библиотеку Python 3.11+


def convert_file(input_path, output_path, array_field="scores"):
    source = Path(input_path)
    destination = Path(output_path)
    with source.open("rb") as stream:
        data = tomllib.load(stream)

    if len(data) < 3:
        raise ValueError("В TOML должно быть минимум 3 поля верхнего уровня")
    if array_field not in data or not isinstance(data[array_field], list):
        raise ValueError(f"Поле {array_field!r} должно быть массивом")

    try:
        data[array_field] = sorted(data[array_field])
    except TypeError as error:
        raise ValueError("Элементы массива должны быть взаимно сравнимы") from error

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return data


def main():
    parser = argparse.ArgumentParser(description="Преобразовать TOML в JSON")
    parser.add_argument("--input", default="toml_task/example.toml")
    parser.add_argument("--output", default="toml_task/result.json")
    parser.add_argument("--array-field", default="scores")
    args = parser.parse_args()
    result = convert_file(args.input, args.output, args.array_field)
    print(f"JSON записан в {args.output}: {result}")


if __name__ == "__main__":
    main()
