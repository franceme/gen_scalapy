installJava:
	curl -s "https://raw.githubusercontent.com/franceme/staticpy/master/sdk.sh" >> /tmp/sdk.sh
	chmod 777 /tmp/sdk.sh
	/tmp/sdk.sh eight
live:
	docker run  --rm -it -v "`pwd`:/sync"   frantzme/scalapy:lite /bin/bash
build:
	docker run  --rm -it -v "`pwd`:/sync"   frantzme/scalapy:lite /bin/bash -c 'cd /sync/ && ./gradlew clean build'
run:
	docker run  --rm -it -v "`pwd`:/sync"   frantzme/scalapy:lite /bin/bash -c 'cd /sync/ && ./gradlew clean build run'
lab:
	docker run  --rm -it -v "`pwd`:/sync" -p 8888:8888 frantzme/scalapy:lite /bin/bash
vs:
	docker run  --rm -it -v "`pwd`:/sync" -p 8912:8912 frantzme/scalapy:lite /bin/bash
clean_env:
	@- yes|rm -r __pycache__
	@- yes|rm -r CachedProfilesData/
	@- yes|rm -r CachedExtensions/
	@- yes|rm -r CachedExtensionVSIXs/
	@- yes|rm -r User/
	@- yes|rm -r Machine/
	@- yes|rm -r extensions/
	@- yes|rm -r logs/
	@- yes|rm -r coder.json
	@- yes|rm -r machineid
	@- yes|rm -r languagepacks.json
	@- yes|rm -r serve-web-key-half
format:
	python3 ruff format