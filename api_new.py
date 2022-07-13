{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74a3b7fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "from src import covid_dash, hospitals_tb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,

   "id": "acc3c5bd",
   "metadata": {},
   "outputs": [],
   "source": []

   "id": "162348db",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/dashboard\")\n",
    "def dashboard():\n",
    "return render_template('dashboard.html')\n",
    "@app.route(\"/map\")\n",
    "def map():\n",
    "return render_template('map.html')"
   ]

  },
  {
   "cell_type": "code",
   "execution_count": null,

   "id": "163476d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "@app.route(\"/\")\n",
    "def landing_page():\n",
    "return render_template('index.html')\n",
    "if __name__ == '__main__':\n",
    "app.run(host='0.0.0.0',port=1991, debug=True)"

   "id": "a85d67d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/dashboard\")\n",
    "def dashboard():\n",
    "return render_template('ÑAÑAAÑÑAÑAÑAÑAÑÑA.html')\n",
    "@app.route(\"/map\")\n",
    "def map():\n",
    "return render_template('map.html')"

   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
print("lo hicimos")
