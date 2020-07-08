{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Mary\n",
      "Access granted.\n"
     ]
    }
   ],
   "source": [
    "name = 'Mary'\n",
    "password = 'swordfish'\n",
    "if name == 'Mary':\n",
    "    print('Hello, Mary')\n",
    "    if password == 'swordfish':\n",
    "        print('Access granted.')\n",
    "    else:\n",
    "        print('Wrong password.')        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unlike you Alice is not an undead, immortal vampire.\n"
     ]
    }
   ],
   "source": [
    "name = 'Carol'\n",
    "age = 3000\n",
    "if name == 'Alice':\n",
    "    print('Hi, Alice.')\n",
    "elif age < 12:\n",
    "    print('You are not Alice, kiddo.')\n",
    "elif age > 2000:\n",
    "    print('Unlike you Alice is not an undead, immortal vampire.')\n",
    "elif age > 100:\n",
    "    print('You are not Alice, grannie.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
