setup-config:
	ln -sF $$(pwd)/nautobot_config.py $$NAUTOBOT_ROOT/nautobot_config.py

run:
	nautobot-server runserver 0.0.0.0:$$NAUTOBOT_PORT

loaddata:
	nautobot-server loaddata ./fixtures/status.json
	nautobot-server loaddata ./fixtures/brm.json
	nautobot-server loaddata ./fixtures/devices.json
	nautobot-server runscript seeddata

nuke:
	docker compose down -v
	docker compose up -d
	nautobot-server migrate
	make loaddata

format:
	ruff check --fix
	ruff format .

