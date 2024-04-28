init:
	make venv hooks

.PHONY: venv
venv:
	bin/setup_venv.sh

.PHONY: test
test:
	pytest tests/

hooks:
	pre-commit install --install-hooks

rmhooks:
	rm .git/hooks/pre-commit
