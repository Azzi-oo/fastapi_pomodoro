_DEFAULT_GDAL := help

HOST ?= 0.0.0.0
PORT ?= 8000

run:
	poetry run uvicorn main:app --host $(HOST) --port $(PORT)

install:
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall:
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST)
