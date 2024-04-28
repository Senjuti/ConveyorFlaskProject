init:
	make venv hooks

.PHONY: venv
venv:
	bin/setup_venv.sh

hooks:
	pre-commit install --install-hooks

rmhooks:
	rm .git/hooks/pre-commit