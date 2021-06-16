all: showcase

.ONESHELL:

PYTEST_OPTIONS := -v
VENV_DIR := venv
NODE_DEP := @c4dt/angular-components
NODE_DEP_VER := 3.0.1-p20210614124421.0

COMMON_CSS := c4dt.css
CSS_DIR := resources

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
$(VENV_DIR)/%: | $(VENV_DIR)
	@: nothing

.PHONY: env
env: requirements.txt $(VENV_DIR)
	. $(VENV_DIR)/bin/activate
	pip3 install -r $<
	npm install $(NODE_DEP)@$(NODE_DEP_VER)
	ln -sf $$( realpath --relative-to $(CSS_DIR) \
		node_modules/$(NODE_DEP)/src/$(COMMON_CSS) ) $(CSS_DIR)

.PHONY: showcase
showcase: env showcase.py
	. $(VENV_DIR)/bin/activate
	./showcase.py

.PHONY: env-test
env-test: requirements-test.txt $(VENV_DIR)
	. $(VENV_DIR)/bin/activate
	pip3 install -r $<

.PHONY: test
test: env-test
	. $(VENV_DIR)/bin/activate
	python3 -m pytest $(PYTEST_OPTIONS)

.PHONY: clean
clean:
	rm -rf $(VENV_DIR) node_modules $(CSS_DIR)/$(COMMON_CSS)
