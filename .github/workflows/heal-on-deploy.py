import sys
import langchain


def main(build_output_file):
    with open(build_output_file, "r") as f:
        build_output = f.read()

    # Process the build_output as needed
    print(build_output)


if __name__ == "__main__":
    build_output_file = sys.argv[1]
    main(build_output_file)
