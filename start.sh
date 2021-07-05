PYTHONPATH=/home/site/wwwroot/venv/lib/python3.7/site-packages:${PYTHONPATH}
export PYTHONPATH
apt update
apt-get install libgfortran3 -y
apt-get install gfortran -y
pip install numpy
pip install pybdf
gunicorn --bind=0.0.0.0 app:app