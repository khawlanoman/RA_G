install:
	uv sync

run:
	uv run python -m src

clean:
	rm -rf .src/__pycache__
	rm -rf .mypy_cache
	rm -rf ./data/processed/output

fclean: clean
	rm -rf data/processed/output

lint:
	-python -m mypy ./src\
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs
	python -m flake8 ./src