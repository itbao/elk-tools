echo """get
post
put
"""|xargs -i ln -s `pwd`/es_curl ~/bin/{}
