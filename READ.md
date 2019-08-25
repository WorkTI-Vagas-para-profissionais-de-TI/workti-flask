virtualenv -p python3 venv
venv/bin/pip3 install flask
venv/bin/pip3 freeze > requirements.txt
pip3 install -r requirements.txt

python3 run.py db init
python3 run.py db migrate

# Caso ocorra um erro ao procurar o móduo pymysql, digite o seguinte comando no seu terminal
`pip3 install pymysql`
