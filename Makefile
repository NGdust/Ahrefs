up:
	cd handlers && faas-cli build -f ahrefs.yml
	cd handlers && faas-cli deploy -f ahrefs.yml
	docker-compose up -d