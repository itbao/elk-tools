# elk-tools
#

Config:
	pip install faker-factory
	pip install elaticsearch
	git clone git@github.com:itbao/elk-tools.git

Example:
	python fake_data.py -i logs-000001  -t type3 --data  name email phone_number -s 192.168.36.100 -n 100 

